#!/usr/bin/env python3
"""
GitHub 项目图片处理工具
用于 github-wechat-article skill 的图片预处理：
  下载 → 裁剪封面 → 压缩 GIF → Base64 编码

用法:
  python process_images.py download --repo owner/repo --out-dir ./images/
  python process_images.py crop-cover --input cover.png --output cover-cropped.png
  python process_images.py compress-gif --input demo.gif --output demo_compressed.gif
  python process_images.py base64-encode --input image.png
  python process_images.py process-all --repo owner/repo --out-dir ./images/ --html template.html
"""

import argparse
import base64
import os
import sys
import urllib.request
from pathlib import Path

try:
    from PIL import Image
    HAS_PILLOW = True
except ImportError:
    HAS_PILLOW = False
    print("⚠ Pillow 未安装，请运行: pip install Pillow", file=sys.stderr)


COVER_WIDTH = 900
COVER_HEIGHT = 383
GIF_MAX_SIZE_MB = 5


# ─── 下载 ───────────────────────────────────────────────

def download_images(image_urls: list[str], out_dir: str) -> list[str]:
    """下载图片到指定目录，返回本地文件路径列表"""
    out_path = Path(out_dir)
    out_path.mkdir(parents=True, exist_ok=True)

    local_paths = []
    for i, url in enumerate(image_urls):
        try:
            ext = url.rsplit(".", 1)[-1].split("?")[0] or "png"
            if ext not in ("png", "jpg", "jpeg", "gif", "webp"):
                ext = "png"
            fname = f"image_{i:02d}.{ext}"
            fpath = out_path / fname

            if not fpath.exists():
                print(f"⬇ 下载: {url}")
                urllib.request.urlretrieve(url, str(fpath))
            else:
                print(f"✓ 已存在: {fname}")
            local_paths.append(str(fpath))
        except Exception as e:
            print(f"✗ 下载失败 {url}: {e}", file=sys.stderr)
    return local_paths


# ─── 封面裁剪 ───────────────────────────────────────────

def crop_cover(input_path: str, output_path: str = None,
               width: int = COVER_WIDTH, height: int = COVER_HEIGHT):
    """将图片裁剪为微信公众号封面尺寸 900×383（2.35:1）"""
    if not HAS_PILLOW:
        print("✗ 需要 Pillow 库", file=sys.stderr)
        return None

    img = Image.open(input_path)
    tw, th = width, height

    # 计算裁剪区域（中心裁剪到目标比例）
    target_ratio = tw / th
    iw, ih = img.size
    current_ratio = iw / ih

    if current_ratio > target_ratio:
        # 图片太宽，裁左右
        new_w = int(ih * target_ratio)
        new_h = ih
        left = (iw - new_w) // 2
        top = 0
    else:
        # 图片太高，裁上下
        new_w = iw
        new_h = int(iw / target_ratio)
        left = 0
        top = (ih - new_h) // 2

    cropped = img.crop((left, top, left + new_w, top + new_h))
    cropped = cropped.resize((tw, th), Image.LANCZOS)

    if output_path is None:
        stem = Path(input_path).stem
        output_path = str(Path(input_path).parent / f"{stem}-cover-{tw}x{th}.png")

    cropped.save(output_path, "PNG", optimize=True)
    print(f"✓ 封面已裁剪: {output_path} ({tw}×{th})")
    return output_path


# ─── GIF 压缩 ───────────────────────────────────────────

def compress_gif(input_path: str, output_path: str = None,
                 max_size_mb: float = GIF_MAX_SIZE_MB,
                 frame_skip: int = 2, scale: float = 0.7,
                 colors: int = 192):
    """
    压缩 GIF 以适应微信公众号限制（<5MB）。
    - frame_skip: 每隔 N 帧取一帧（2 = 隔帧取样）
    - scale: 缩放比例
    - colors: 调色板颜色数
    """
    if not HAS_PILLOW:
        print("✗ 需要 Pillow 库", file=sys.stderr)
        return None

    if output_path is None:
        stem = Path(input_path).stem
        output_path = str(Path(input_path).parent / f"{stem}_compressed.gif")

    im = Image.open(input_path)

    # 收集缩放后的帧
    frames = []
    duration = im.info.get("duration", 100)
    frame_idx = 0

    try:
        while True:
            if frame_idx % frame_skip == 0:
                # 缩放
                new_w = int(im.width * scale)
                new_h = int(im.height * scale)
                resized = im.resize((new_w, new_h), Image.LANCZOS)

                # 安全转换到调色板模式
                f_rgb = resized.convert("RGB")
                f_p = f_rgb.quantize(colors=colors)
                frames.append(f_p)
            frame_idx += 1
            im.seek(im.tell() + 1)
    except EOFError:
        pass

    if not frames:
        print("✗ GIF 中没有有效帧", file=sys.stderr)
        return None

    # 保存（使用 disposal=0 避免透明通道 bug，optimize=False 避免损坏）
    frames[0].save(
        output_path,
        save_all=True,
        append_images=frames[1:],
        duration=duration * frame_skip,
        loop=0,
        disposal=0,
        optimize=False,
    )

    size_mb = os.path.getsize(output_path) / (1024 * 1024)
    print(f"✓ GIF 已压缩: {output_path} "
          f"（{len(frames)} 帧, {size_mb:.1f}MB）")

    if size_mb > max_size_mb:
        print(f"⚠ 仍然超过 {max_size_mb}MB，建议进一步降低 scale/colors")

    return output_path


# ─── Base64 编码 ────────────────────────────────────────

def base64_encode_image(image_path: str) -> str:
    """将图片编码为 Base64 Data URI 字符串"""
    ext = Path(image_path).suffix.lower().lstrip(".")
    mime_map = {"png": "image/png", "jpg": "image/jpeg", "jpeg": "image/jpeg",
                "gif": "image/gif", "webp": "image/webp"}
    mime = mime_map.get(ext, "image/png")

    with open(image_path, "rb") as f:
        data = base64.b64encode(f.read()).decode("ascii")

    return f"data:{mime};base64,{data}"


def generate_img_tag(image_path: str, alt: str = "") -> str:
    """生成内嵌 Base64 的 HTML img 标签"""
    uri = base64_encode_image(image_path)
    if alt:
        return (f'<p style="text-align:center;margin:18px 0;">\n'
                f'  <img src="{uri}" alt="{alt}" '
                f'style="max-width:100%;display:block;margin:0 auto;">\n'
                f'  <span style="font-size:12px;color:#999;display:block;'
                f'margin-top:4px;">▲ {alt}</span>\n</p>')
    return (f'<p style="text-align:center;margin:18px 0;">\n'
            f'  <img src="{uri}" alt="" '
            f'style="max-width:100%;display:block;margin:0 auto;">\n</p>')


# ─── 全流程 ────────────────────────────────────────────

def process_all(repo_owner: str, repo_name: str,
                out_dir: str, html_path: str = None):
    """一键处理：下载 → 裁剪 → 压缩 → 编码 → 替换 HTML"""
    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)

    # 1. 封面图
    og_url = (f"https://opengraph.githubassets.com/1/"
              f"{repo_owner}/{repo_name}")
    print(f"📷 获取 OpenGraph 封面: {og_url}")
    cover_path = out / "cover-github-banner.png"
    try:
        urllib.request.urlretrieve(og_url, str(cover_path))
        crop_cover(str(cover_path))
    except Exception as e:
        print(f"⚠ OpenGraph 封面获取失败: {e}")

    # 2. 处理 HTML 中的图片（如果有 HTML 模板）
    if html_path:
        with open(html_path, "r", encoding="utf-8") as f:
            html = f.read()

        # 收集本地图片并替换为 Base64
        import re
        for img_match in re.finditer(
            r'<img\s+src="(?!data:)([^"]+\.(?:png|jpg|jpeg|gif|webp))"',
            html, re.IGNORECASE
        ):
            img_file = img_match.group(1)
            img_path = out / img_file
            if img_path.exists():
                uri = base64_encode_image(str(img_path))
                html = html.replace(img_file, uri)
                print(f"✓ 内嵌: {img_file}")

        output_html = str(Path(html_path).parent / f"{repo_name}-wechat-article.html")
        with open(output_html, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"✓ HTML 已生成: {output_html}")


# ─── CLI ────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="GitHub 项目图片处理工具（github-wechat-article skill）")
    sub = parser.add_subparsers(dest="command", required=True)

    # download
    p_dl = sub.add_parser("download", help="下载图片")
    p_dl.add_argument("--urls", nargs="+", required=True, help="图片 URL 列表")
    p_dl.add_argument("--out-dir", default="./images", help="输出目录")

    # crop-cover
    p_cc = sub.add_parser("crop-cover", help="裁剪封面为 900×383")
    p_cc.add_argument("--input", required=True, help="输入图片路径")
    p_cc.add_argument("--output", default=None, help="输出路径（可选）")
    p_cc.add_argument("--width", type=int, default=900)
    p_cc.add_argument("--height", type=int, default=383)

    # compress-gif
    p_cg = sub.add_parser("compress-gif", help="压缩 GIF")
    p_cg.add_argument("--input", required=True, help="输入 GIF 路径")
    p_cg.add_argument("--output", default=None, help="输出路径（可选）")
    p_cg.add_argument("--max-size-mb", type=float, default=5.0)
    p_cg.add_argument("--frame-skip", type=int, default=2)
    p_cg.add_argument("--scale", type=float, default=0.7)
    p_cg.add_argument("--colors", type=int, default=192)

    # base64-encode
    p_be = sub.add_parser("base64-encode", help="Base64 编码单张图片")
    p_be.add_argument("--input", required=True, help="输入图片路径")

    # process-all
    p_pa = sub.add_parser("process-all", help="一键全流程处理")
    p_pa.add_argument("--repo", required=True, help="owner/repo")
    p_pa.add_argument("--out-dir", required=True, help="输出目录")
    p_pa.add_argument("--html", default=None, help="HTML 模板路径（可选）")

    args = parser.parse_args()

    if args.command == "download":
        download_images(args.urls, args.out_dir)

    elif args.command == "crop-cover":
        crop_cover(args.input, args.output, args.width, args.height)

    elif args.command == "compress-gif":
        compress_gif(args.input, args.output,
                     args.max_size_mb, args.frame_skip,
                     args.scale, args.colors)

    elif args.command == "base64-encode":
        uri = base64_encode_image(args.input)
        print(uri)

    elif args.command == "process-all":
        parts = args.repo.split("/")
        if len(parts) != 2:
            print("✗ --repo 格式应为 owner/repo", file=sys.stderr)
            sys.exit(1)
        process_all(parts[0], parts[1], args.out_dir, args.html)


if __name__ == "__main__":
    main()
