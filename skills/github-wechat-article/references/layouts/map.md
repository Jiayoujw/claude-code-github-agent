##### ② LAYOUT_MAP — 地图式布局（配对 EXPLORER）

```
核心原则：像探险家展开一张地图，每次往下翻都有新发现。节奏跳跃、信息点密集。

【段落顺序】
h1 标题
├─ p 封面图（文章最前面——视觉冲击优先，让读者先看到"地图全貌"）
├─ p 开篇钩子（1 段短段落，制造好奇）
├─ h2 "它能搜什么？"
├─ table 横向标签云（3-4 列，每列一个搜索源 + 说明，紧凑展示覆盖范围）
├─ h2 "发现了什么？拆开看这 N 个维度"
├─ blockquote "🔍 搜索维度 1" → p 发现内容
├─ blockquote "🔍 搜索维度 2" → p 发现内容
├─ blockquote "🔍 搜索维度 3" → p 发现内容
├─ hr 虚线分割
├─ h2 "搜索背后的秘密"
├─ p 技术亮点（比传统方案好在哪，用段落叙述）
├─ pre 安装命令（如果有 CLI，画风像一个探索工具的命令行入口）
├─ hr
└─ CTA：平台投票表格

【数据卡格式】横向标签云：3 列紧凑 table，每列 emoji 图标 + 平台名 + 一句话
【功能展示】探索日志式：每个功能以 blockquote 标记搜索维度，后面跟 p 展开
【「适合谁用」格式】融入"它能搜什么"中，不再单独列出
【封面位置】文章最前面（第 1 个视觉元素）
【间距密/疏】紧凑跳跃：h2 margin 20px/12px，段间距 12px，行高 1.7
【分割线】虚线：<hr style="border:0;border-top:1px dashed {{主题色}};margin:24px 0;">
【h2 装饰】border-left:4px solid {{主题色}} + padding-left:12px

【完整 HTML 模板】
<h1 style="font-size:24px;color:#1a1a1a;text-align:center;margin:0 0 20px;line-height:1.5;">标题</h1>
<p style="text-align:center;margin:0 0 16px;"><img src="data:image/png;base64,..." alt="" style="max-width:100%;"></p>
<p style="font-size:15px;color:#333;line-height:1.7;margin:0 0 12px;">开篇钩子段落……</p>
<h2 style="font-size:19px;color:#1a1a1a;margin:20px 0 12px;border-left:4px solid {{主题色}};padding-left:12px;">它能搜什么？</h2>
<table width="100%" cellpadding="10" cellspacing="0" border="0" style="background:{{数据卡底色}};margin:12px 0;">
  <tr style="text-align:center;">
    <td style="font-size:14px;color:#333;padding:8px;"><strong style="color:{{主题色}};">🐦 X/Twitter</strong><br><span style="font-size:12px;color:#666;">实时讨论</span></td>
    <td style="font-size:14px;color:#333;padding:8px;"><strong style="color:{{主题色}};">📱 Reddit</strong><br><span style="font-size:12px;color:#666;">深度讨论</span></td>
    <td style="font-size:14px;color:#333;padding:8px;"><strong style="color:{{主题色}};">📰 HackerNews</strong><br><span style="font-size:12px;color:#666;">技术圈热议</span></td>
  </tr>
</table>
<h2 style="font-size:19px;color:#1a1a1a;margin:20px 0 12px;border-left:4px solid {{主题色}};padding-left:12px;">发现了什么？拆开看这 N 个维度</h2>
<blockquote style="border-left:3px solid {{强调色}};background:{{功能卡底色}};margin:12px 0;padding:8px 14px;"><p style="font-size:14px;color:{{主题色}};font-weight:600;margin:0 0 4px;">🔍 维度 1：活生生的真实观点</p></blockquote>
<p style="font-size:15px;color:#333;line-height:1.7;margin:0 0 12px;">发现描述……</p>
<blockquote style="border-left:3px solid {{强调色}};background:{{功能卡底色}};margin:12px 0;padding:8px 14px;"><p style="font-size:14px;color:{{主题色}};font-weight:600;margin:0 0 4px;">🔍 维度 2：跨平台情绪追踪</p></blockquote>
<p style="font-size:15px;color:#333;line-height:1.7;margin:0 0 12px;">发现描述……</p>
<hr style="border:0;border-top:1px dashed {{主题色}};margin:24px 0;">
<h2 style="font-size:19px;color:#1a1a1a;margin:20px 0 12px;border-left:4px solid {{主题色}};padding-left:12px;">搜索背后的秘密</h2>
<p style="font-size:15px;color:#333;line-height:1.7;margin:0 0 12px;">技术亮点说明……</p>
<pre style="background:#1e1b4b;color:#e2e8f0;padding:12px;font-size:14px;line-height:1.6;"><code>npx last30days "AI coding tools"</code></pre>
<hr style="border:0;border-top:1px dashed {{主题色}};margin:24px 0;">
<table width="100%" cellpadding="14" cellspacing="0" border="0" style="background:{{数据卡底色}};text-align:center;">
  <tr><td>
    <p style="font-size:16px;font-weight:600;color:{{主题色}};margin:0 0 12px;">{{CTA 问题}}</p>
    <p style="font-size:14px;color:#666;margin:0 0 6px;">A. X/Twitter 搜技术趋势</p>
    <p style="font-size:14px;color:#666;margin:0 0 6px;">B. Reddit 看真实用户讨论</p>
    <p style="font-size:14px;color:#666;margin:0 0 12px;">C. 都想试试 🔥</p>
  </td></tr>
</table>
<p style="font-size:13px;color:#999;text-align:center;margin:16px 0 0;">🧡 欢迎<strong style="color:{{主题色}};">点赞、收藏、转发</strong>～</p>
<p style="font-size:13px;color:#999;text-align:center;margin:8px 0 0;">{{关注引导语}}</p>
```
