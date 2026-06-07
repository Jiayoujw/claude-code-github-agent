##### ⑤ LAYOUT_MANIFESTO — 宣言式布局（配对 FUTURIST）

```
核心原则：像一份未来宣言，用视觉冲击制造震撼。大图、大字、大数字。

【段落顺序】
h1 标题
├─ p 封面图（文章最前面——"先看这张图"）
├─ p 开篇钩子（"你花了 X 个月训练……机械臂直接把杯子捏碎了"——直接制造认知冲击）
├─ table 巨型数字卡：单行单列（一条最震撼的数据，字号巨大）
├─ h2 "它是什么？不是工具，是世界观"
├─ p 项目本质描述
├─ h2 "拆解：重新定义 [领域] 的 N 个维度"
├─ table 维度 1：双栏（左：传统认知 | 右：[项目名] 的做法）——打破认知
├─ table 维度 2：同上
├─ table 维度 3：同上
├─ hr
├─ h2 "这意味着什么？"
├─ blockquote 引用行业大牛或媒体评论（放大格局）
├─ p 展望未来，写得像一段迷你科幻
├─ hr
└─ CTA：预测式投票

【数据卡格式】巨型单数字：一个 table cell，里面用超大字号的 Star 数或关键数字
【功能展示】认知对比表：每行一个 2 列 table（传统认知 vs 项目突破），制造认知冲突
【「适合谁用」格式】融入"这意味着什么"段落，不单独列出
【封面位置】文章最前面
【间距密/疏】戏剧化反差：段落间 margin 有大有小，制造节奏。行高 1.7
【分割线】粗实线：<hr style="border:0;border-top:2px solid {{主题色}};margin:32px 0;">
【h2 装饰】无 border-left；改用全宽浅色背景条 + 居中文字，强调宣言感

【完整 HTML 模板】
<h1 style="font-size:24px;color:#1a1a1a;text-align:center;margin:0 0 20px;line-height:1.5;">标题</h1>
<p style="text-align:center;margin:0 0 16px;"><img src="data:image/png;base64,..." alt="" style="max-width:100%;"></p>
<p style="font-size:15px;color:#333;line-height:1.7;margin:0 0 14px;">开篇钩子——制造认知冲击……</p>
<p style="font-size:15px;color:#333;line-height:1.7;margin:0 0 14px;">钩子收束句——引出项目……</p>
<table width="100%" cellpadding="20" cellspacing="0" border="0" style="background:{{数据卡底色}};margin:18px 0;text-align:center;">
  <tr><td><p style="font-size:48px;font-weight:800;color:{{主题色}};margin:0;">9.4k</p><p style="font-size:14px;color:#666;margin:8px 0 0;">GitHub Stars &nbsp;|&nbsp; 重新定义物理 AI 的开源力量</p></td></tr>
</table>
<h2 style="font-size:18px;color:#1a1a1a;text-align:center;margin:28px 0 16px;padding:8px 0;background:{{数据卡底色}};">它是什么？不是工具，是世界观</h2>
<p style="font-size:15px;color:#333;line-height:1.7;margin:0 0 14px;">项目本质描述……</p>
<h2 style="font-size:18px;color:#1a1a1a;text-align:center;margin:28px 0 16px;padding:8px 0;background:{{数据卡底色}};">拆解：重新定义 [领域] 的 N 个维度</h2>
<table width="100%" cellpadding="10" cellspacing="0" border="0" style="background:{{功能卡底色}};margin:12px 0;">
  <tr><td style="font-size:13px;color:#999;padding:6px 10px;">以前</td><td style="font-size:13px;color:{{主题色}};font-weight:600;padding:6px 10px;">现在</td></tr>
  <tr><td style="font-size:14px;color:#555;padding:6px 10px;">传统做法的问题……</td><td style="font-size:14px;color:#333;padding:6px 10px;">[项目名] 的突破……</td></tr>
</table>
<!-- 维度 2、3 同上复制 -->
<hr style="border:0;border-top:2px solid {{主题色}};margin:32px 0;">
<h2 style="font-size:18px;color:#1a1a1a;text-align:center;margin:28px 0 16px;padding:8px 0;background:{{数据卡底色}};">这意味着什么？</h2>
<blockquote style="border-left:4px solid {{主题色}};background:{{数据卡底色}};margin:14px 0;padding:12px 16px;">
  <p style="font-size:14px;color:#555;line-height:1.7;margin:0;">「[引用行业大牛或媒体的评论]」</p>
</blockquote>
<p style="font-size:15px;color:#333;line-height:1.7;margin:0 0 14px;">展望未来的描述……</p>
<hr style="border:0;border-top:2px solid {{主题色}};margin:32px 0;">
<table width="100%" cellpadding="14" cellspacing="0" border="0" style="background:{{数据卡底色}};text-align:center;">
  <tr><td>
    <p style="font-size:16px;font-weight:600;color:{{主题色}};margin:0 0 12px;">{{CTA 问题}}</p>
    <p style="font-size:14px;color:#666;margin:0 0 6px;">A. 2 年内，机器人管家进入普通家庭 🤖</p>
    <p style="font-size:14px;color:#666;margin:0 0 6px;">B. 5 年内，工厂全面物理 AI 化 🏭</p>
    <p style="font-size:14px;color:#666;margin:0 0 12px;">C. 还要 10 年以上，路还很长 🧐</p>
  </td></tr>
</table>
<p style="font-size:13px;color:#999;text-align:center;margin:16px 0 0;">🧡 欢迎<strong style="color:{{主题色}};">点赞、收藏、转发</strong>给对未来好奇的朋友～</p>
<p style="font-size:13px;color:#999;text-align:center;margin:8px 0 0;">{{关注引导语}}</p>
```
