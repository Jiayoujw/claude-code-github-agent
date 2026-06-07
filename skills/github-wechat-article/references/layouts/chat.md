##### ⑦ LAYOUT_CHAT — 聊天式布局（配对 COMPANION）

```
核心原则：像跟朋友微信聊天安利一个小工具。轻松、有趣、个人化。

【段落顺序】
h1 标题
├─ p 开篇钩子（个人小故事——"我有一个困扰了很久的问题……"）
├─ p 封面图（故事结束后，自然出现——"直到我发现了它"）
├─ blockquote "我的第一印象"（用个人口吻的引用块，代替正式功能卡片）
├─ table 数据卡片（简化为「第一印象反应卡」——3 列 emoji 反应）
├─ h2 "它是个什么东西？简单说"
├─ p 一句话介绍
├─ h2 "亮点一览：最实用的 N 个功能"
├─ p 功能 1：<strong style="color:{{主题色}};">✨ 亮点名：</strong> 简短说明（不用卡片，直接用段落）
├─ p 功能 2：同上
├─ p 功能 3：同上
├─ h2 "装好后是什么体验？"
├─ p 个人使用感受（"自从装上之后，我每天的流程变成了这样……"）
├─ pre 安装命令（简单的一行命令）
├─ hr
└─ CTA：趣味安利投票

【数据卡格式】「第一印象反应卡」：3 列 emoji（如 😍 / ⭐ / 🎮）+ 简短标签，不像正式数据
【功能展示】聊天气泡式：直接用 p 段落 + <strong> 高亮功能名，不用 table 卡片
【「适合谁用」格式】融入"装好后是什么体验"和"第一印象"，不单独列
【封面位置】个人故事之后
【间距密/疏】轻快多变：段落间距 12-18px 不等，行高 1.75，像聊天记录的节奏
【分割线】极简：<hr style="border:0;border-top:1px solid #d1d5db;margin:24px 0;">
【h2 装饰】border-left:3px solid {{主题色}} + padding-left:10px（轻量装饰）

【完整 HTML 模板】
<h1 style="font-size:24px;color:#1a1a1a;text-align:center;margin:0 0 20px;line-height:1.5;">标题</h1>
<p style="font-size:15px;color:#333;line-height:1.75;margin:0 0 14px;">我有一个困扰了很久的问题……（个人小故事开头）</p>
<p style="font-size:15px;color:#333;line-height:1.75;margin:0 0 14px;">直到我发现了 [项目名]……</p>
<p style="text-align:center;margin:16px 0;"><img src="data:image/png;base64,..." alt="" style="max-width:100%;"></p>
<blockquote style="border-left:3px solid {{主题色}};background:{{数据卡底色}};margin:16px 0;padding:10px 14px;">
  <p style="font-size:14px;color:{{主题色}};font-weight:600;margin:0 0 6px;">我的第一印象 👇</p>
  <p style="font-size:14px;color:#333;line-height:1.7;margin:0;">"装好打开的那一瞬间，我就知道这玩意儿会常驻我的电脑——"（个人化评价）</p>
</blockquote>
<table width="100%" cellpadding="8" cellspacing="0" border="0" style="background:{{数据卡底色}};margin:14px 0;text-align:center;">
  <tr>
    <td style="padding:8px;"><p style="font-size:28px;margin:0;">😍</p><p style="font-size:13px;color:#666;margin:4px 0 0;">1.6k Star</p></td>
    <td style="padding:8px;"><p style="font-size:28px;margin:0;">⭐</p><p style="font-size:13px;color:#666;margin:4px 0 0;">MIT 开源</p></td>
    <td style="padding:8px;"><p style="font-size:28px;margin:0;">🪟</p><p style="font-size:13px;color:#666;margin:4px 0 0;">WinUI 3</p></td>
  </tr>
</table>
<h2 style="font-size:19px;color:#1a1a1a;margin:22px 0 14px;border-left:3px solid {{主题色}};padding-left:10px;">它是个什么东西？简单说</h2>
<p style="font-size:15px;color:#333;line-height:1.75;margin:0 0 14px;">一句话轻松介绍……</p>
<h2 style="font-size:19px;color:#1a1a1a;margin:22px 0 14px;border-left:3px solid {{主题色}};padding-left:10px;">亮点一览：最实用的 N 个功能</h2>
<p style="font-size:15px;color:#333;line-height:1.75;margin:0 0 14px;"><strong style="color:{{主题色}};">✨ 功能名：</strong>简短说明。用了之后你会发现……</p>
<p style="font-size:15px;color:#333;line-height:1.75;margin:0 0 14px;"><strong style="color:{{主题色}};">✨ 功能名：</strong>简短说明。特别适合……</p>
<p style="font-size:15px;color:#333;line-height:1.75;margin:0 0 14px;"><strong style="color:{{主题色}};">✨ 功能名：</strong>简短说明。最让我惊喜的是……</p>
<h2 style="font-size:19px;color:#1a1a1a;margin:22px 0 14px;border-left:3px solid {{主题色}};padding-left:10px;">装好后是什么体验？</h2>
<p style="font-size:15px;color:#333;line-height:1.75;margin:0 0 14px;">个人使用感受，像聊天一样说……</p>
<pre style="background:#1e1b4b;color:#e2e8f0;padding:12px;font-size:14px;line-height:1.6;"><code>winget install OpenClaw</code></pre>
<hr style="border:0;border-top:1px solid #d1d5db;margin:24px 0;">
<table width="100%" cellpadding="14" cellspacing="0" border="0" style="background:{{数据卡底色}};text-align:center;">
  <tr><td>
    <p style="font-size:16px;font-weight:600;color:{{主题色}};margin:0 0 12px;">{{CTA 问题}}</p>
    <p style="font-size:14px;color:#666;margin:0 0 6px;">A. 已安装！确实好用 🎉</p>
    <p style="font-size:14px;color:#666;margin:0 0 6px;">B. 马上去装，忍不了了 🏃</p>
    <p style="font-size:14px;color:#666;margin:0 0 12px;">C. 我有更好的推荐！评论区见 👇</p>
  </td></tr>
</table>
<p style="font-size:13px;color:#999;text-align:center;margin:16px 0 0;">🧡 欢迎<strong style="color:{{主题色}};">点赞、收藏、转发</strong>给同样爱折腾的朋友～</p>
<p style="font-size:13px;color:#999;text-align:center;margin:8px 0 0;">{{关注引导语}}</p>
