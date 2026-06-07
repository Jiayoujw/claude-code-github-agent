##### ③ LAYOUT_DASHBOARD — 仪表盘式布局（配对 PRAGMATIC）

```
核心原则：像打开一个监控仪表盘，一眼看到关键数字。紧凑、高效率、零废话。

【段落顺序】
h1 标题
├─ p 开篇钩子（痛点场景，1-2 段）
├─ p 封面图（痛点铺垫后、方案揭晓前——"就是它"的揭示感）
├─ table 2×2 紧凑数据网格（Star / 许可证 / 语言 / 一句话）
├─ p 一句话总结（1 段，不超过 50 字）
├─ h2 "硬核拆解：为什么它这么强？"
├─ table 功能 1：前后对比（2 行 2 列：没有它时 vs 有了它之后）
├─ table 功能 2：前后对比
├─ table 功能 3：前后对比
├─ h2 "上手门槛？实测给你看"
├─ blockquote 实测数据
├─ pre 安装命令（必须有，因为读者是开发者）
├─ h2 "这个工具适合你吗？"
├─ table ✅/⚠ 二分清单（高对比：绿色 ✅ vs 灰色 ⚠）
├─ hr
└─ CTA：工具对比投票

【数据卡格式】2×2 网格：4 个关键数字并排展示，每个 cell 一个指标+数值
【功能展示】前后对比表：每项功能用 2 行 table 展示「没有它时」→「有了它之后」
【「适合谁用」格式】二分清单：左侧 ✅ 适合人群，右侧 ⚠ 不适合场景
【封面位置】痛点铺垫后、方案揭晓前
【间距密/疏】极紧凑：h2 margin 20px/10px，段间距 10px，行高 1.6
【分割线】仅在 CTA 前加一条：<hr style="border:0;border-top:1px solid #fecaca;">
【h2 装饰】border-left:4px solid {{主题色}} + padding-left:12px

【完整 HTML 模板】
<h1 style="font-size:24px;color:#1a1a1a;text-align:center;margin:0 0 20px;line-height:1.5;">标题</h1>
<p style="font-size:15px;color:#333;line-height:1.6;margin:0 0 10px;">痛点钩子第一段……</p>
<p style="font-size:15px;color:#333;line-height:1.6;margin:0 0 10px;">痛点钩子第二段，引出项目……</p>
<p style="text-align:center;margin:14px 0;"><img src="data:image/png;base64,..." alt="" style="max-width:100%;"></p>
<table width="100%" cellpadding="8" cellspacing="0" border="0" style="background:{{数据卡底色}};margin:14px 0;">
  <tr style="text-align:center;">
    <td style="padding:10px 6px;"><p style="font-size:13px;color:#666;margin:0;">⭐ Stars</p><p style="font-size:22px;font-weight:700;color:{{主题色}};margin:4px 0 0;">72.8k</p></td>
    <td style="padding:10px 6px;"><p style="font-size:13px;color:#666;margin:0;">📝 协议</p><p style="font-size:16px;font-weight:600;color:#059669;margin:4px 0 0;">MIT</p></td>
    <td style="padding:10px 6px;"><p style="font-size:13px;color:#666;margin:0;">🔧 语言</p><p style="font-size:16px;font-weight:600;color:#333;margin:4px 0 0;">Python</p></td>
    <td style="padding:10px 6px;"><p style="font-size:13px;color:#666;margin:0;">⚡ 效率</p><p style="font-size:16px;font-weight:600;color:{{强调色}};margin:4px 0 0;">提升3x</p></td>
  </tr>
</table>
<p style="font-size:15px;color:#333;line-height:1.6;margin:0 0 10px;">一句话总结项目……</p>
<h2 style="font-size:19px;color:#1a1a1a;margin:20px 0 10px;border-left:4px solid {{主题色}};padding-left:12px;">硬核拆解：为什么它这么强？</h2>
<table width="100%" cellpadding="10" cellspacing="0" border="0" style="background:{{功能卡底色}};margin:10px 0;">
  <tr><td style="font-size:13px;color:#999;padding:6px 10px;">❌ 没有它时</td></tr>
  <tr><td style="font-size:14px;color:#333;padding:6px 10px;">旧方案的痛点描述……</td></tr>
  <tr><td style="font-size:13px;color:{{主题色}};padding:6px 10px;font-weight:600;">✅ 有了 [项目名]</td></tr>
  <tr><td style="font-size:14px;color:#333;padding:6px 10px;">新方案的改善描述……</td></tr>
</table>
<!-- 功能 2、3 同上复制 -->
<h2 style="font-size:19px;color:#1a1a1a;margin:20px 0 10px;border-left:4px solid {{主题色}};padding-left:12px;">上手门槛？实测给你看</h2>
<blockquote style="border-left:4px solid {{主题色}};background:{{数据卡底色}};margin:10px 0;padding:10px 14px;">
  <p style="font-size:14px;color:{{主题色}};font-weight:600;margin:0 0 4px;">⚡ 实测数据</p>
  <p style="font-size:14px;color:#333;line-height:1.6;margin:0;">具体效果数据……</p>
</blockquote>
<pre style="background:#1e1b4b;color:#e2e8f0;padding:12px;font-size:14px;line-height:1.6;"><code>pip install project-name</code></pre>
<h2 style="font-size:19px;color:#1a1a1a;margin:20px 0 10px;border-left:4px solid {{主题色}};padding-left:12px;">这个工具适合你吗？</h2>
<table width="100%" cellpadding="10" cellspacing="0" border="0" style="background:{{数据卡底色}};margin:10px 0;">
  <tr><td style="font-size:14px;color:#333;padding:6px 10px;">✅ 适合 [场景A] 的 [角色]</td></tr>
  <tr><td style="font-size:14px;color:#333;padding:6px 10px;">✅ 想要 [效果] 但不想 [麻烦] 的人</td></tr>
  <tr><td style="font-size:14px;color:#999;padding:6px 10px;">⚠ [不适用场景]，这个工具不太合适</td></tr>
</table>
<hr style="border:0;border-top:1px solid #fecaca;margin:20px 0;">
<table width="100%" cellpadding="14" cellspacing="0" border="0" style="background:{{数据卡底色}};text-align:center;">
  <tr><td>
    <p style="font-size:16px;font-weight:600;color:{{主题色}};margin:0 0 12px;">{{CTA 问题}}</p>
    <p style="font-size:14px;color:#666;margin:0 0 6px;">A. 已经在用了，效率提升明显 💪</p>
    <p style="font-size:14px;color:#666;margin:0 0 6px;">B. 还在用 [竞品]，看完想试试 🔥</p>
    <p style="font-size:14px;color:#666;margin:0 0 12px;">C. 第一次听说，马上去试 🚀</p>
  </td></tr>
</table>
<p style="font-size:13px;color:#999;text-align:center;margin:16px 0 0;">🧡 欢迎<strong style="color:{{主题色}};">点赞、收藏、转发</strong>～</p>
<p style="font-size:13px;color:#999;text-align:center;margin:8px 0 0;">{{关注引导语}}</p>
```
