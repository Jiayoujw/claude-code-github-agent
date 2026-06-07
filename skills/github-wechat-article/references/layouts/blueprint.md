##### ⑥ LAYOUT_BLUEPRINT — 蓝图式布局（配对 ARCHITECT）

```
核心原则：像读一份建筑设计图，结构清晰、层级分明、每一个模块都有明确位置。

【段落顺序】
h1 标题
├─ p 开篇钩子（问题场景——"你有没有遇到过这种场景……"）
├─ p 问题收束——"这件事之前没有统一方案，直到 [项目名]"
├─ p 封面图（问题时陈述后——"这就是它的架构全貌"）
├─ h2 "它解决的问题是什么？"
├─ p 问题描述
├─ table 规格说明书（3 行：Stars / 协议 / 支持的协议/标准）+ 一句话描述
├─ h2 "架构拆解：关键设计"
├─ table "🔷 基础层：[名称]" + p 说明
├─ table "🔷 中间层：[名称]" + p 说明
├─ table "🔷 接口层：[名称]" + p 说明
├─ h2 "谁在用它？生态如何？"
├─ table 决策矩阵（3 列：角色 / 需求 / 匹配度）
├─ p 生态说明（被哪些大厂采用、社区活跃度）
├─ h2 "怎么接入？"
├─ pre 安装/接入命令
├─ hr
└─ CTA：技术栈偏好投票

【数据卡格式】规格说明书：左对齐 label + 右对齐 value 的 3 行 table，像 API 文档
【功能展示】分层架构：每层用带菱形标记的 table 做标题 + p 展开，模拟系统架构图
【「适合谁用」格式】决策矩阵：3 列 table（角色/需求/匹配度），每个角色一行
【封面位置】问题陈述之后
【间距密/疏】精准一致：h2 margin 24px/12px，段间距 14px，行高 1.75，所有元素对齐一致
【分割线】仅在 CTA 前：<hr style="border:0;border-top:1px solid #cbd5e1;">
【h2 装饰】border-left:4px solid {{主题色}} + padding-left:14px

【完整 HTML 模板】
<h1 style="font-size:24px;color:#1a1a1a;text-align:center;margin:0 0 24px;line-height:1.5;">标题</h1>
<p style="font-size:15px;color:#333;line-height:1.75;margin:0 0 14px;">问题场景钩子……</p>
<p style="font-size:15px;color:#333;line-height:1.75;margin:0 0 14px;">问题收束——"之前没有统一方案，直到 [项目名]"……</p>
<p style="text-align:center;margin:18px 0;"><img src="data:image/png;base64,..." alt="" style="max-width:100%;"></p>
<h2 style="font-size:19px;color:#1a1a1a;margin:24px 0 14px;border-left:4px solid {{主题色}};padding-left:14px;">它解决的问题是什么？</h2>
<p style="font-size:15px;color:#333;line-height:1.75;margin:0 0 14px;">问题详细说明……</p>
<table width="100%" cellpadding="10" cellspacing="0" border="0" style="background:{{数据卡底色}};margin:14px 0;">
  <tr><td style="font-size:14px;color:#666;padding:6px 12px;">⭐ Stars</td><td style="font-size:14px;color:{{主题色}};font-weight:600;padding:6px 12px;text-align:right;">32k</td></tr>
  <tr><td style="font-size:14px;color:#666;padding:6px 12px;">📝 协议</td><td style="font-size:14px;color:#059669;padding:6px 12px;text-align:right;">MIT</td></tr>
  <tr><td style="font-size:14px;color:#666;padding:6px 12px;">🔗 标准</td><td style="font-size:14px;color:{{强调色}};font-weight:600;padding:6px 12px;text-align:right;">AG-UI 协议</td></tr>
</table>
<p style="font-size:15px;color:#333;line-height:1.75;margin:0 0 14px;">一句话定位项目……</p>
<h2 style="font-size:19px;color:#1a1a1a;margin:24px 0 14px;border-left:4px solid {{主题色}};padding-left:14px;">架构拆解：关键设计</h2>
<table width="100%" cellpadding="10" cellspacing="0" border="0" style="background:{{功能卡底色}};margin:12px 0;">
  <tr><td style="font-size:15px;color:{{主题色}};font-weight:700;padding:6px 12px;">🔷 基础层：消息处理引擎</td></tr>
  <tr><td style="font-size:14px;color:#555;padding:6px 12px;">详细说明……</td></tr>
</table>
<table width="100%" cellpadding="10" cellspacing="0" border="0" style="background:{{功能卡底色}};margin:12px 0;">
  <tr><td style="font-size:15px;color:{{主题色}};font-weight:700;padding:6px 12px;">🔷 中间层：UI 协议适配</td></tr>
  <tr><td style="font-size:14px;color:#555;padding:6px 12px;">详细说明……</td></tr>
</table>
<table width="100%" cellpadding="10" cellspacing="0" border="0" style="background:{{功能卡底色}};margin:12px 0;">
  <tr><td style="font-size:15px;color:{{主题色}};font-weight:700;padding:6px 12px;">🔷 接口层：多平台发布器</td></tr>
  <tr><td style="font-size:14px;color:#555;padding:6px 12px;">详细说明……</td></tr>
</table>
<h2 style="font-size:19px;color:#1a1a1a;margin:24px 0 14px;border-left:4px solid {{主题色}};padding-left:14px;">谁在用它？生态如何？</h2>
<table width="100%" cellpadding="10" cellspacing="0" border="0" style="background:{{数据卡底色}};margin:14px 0;">
  <tr style="border-bottom:1px solid #d1d5db;">
    <td style="font-size:14px;color:#666;font-weight:600;padding:8px 10px;">角色</td>
    <td style="font-size:14px;color:#666;font-weight:600;padding:8px 10px;">需求</td>
    <td style="font-size:14px;color:{{主题色}};font-weight:600;padding:8px 10px;text-align:center;">匹配度</td>
  </tr>
  <tr>
    <td style="font-size:14px;color:#333;padding:8px 10px;">前端开发者</td>
    <td style="font-size:14px;color:#555;padding:8px 10px;">快速接入 AI Agent UI</td>
    <td style="font-size:14px;color:{{主题色}};font-weight:600;padding:8px 10px;text-align:center;">⭐⭐⭐⭐⭐</td>
  </tr>
  <tr>
    <td style="font-size:14px;color:#333;padding:8px 10px;">平台架构师</td>
    <td style="font-size:14px;color:#555;padding:8px 10px;">统一多端 AI 交互标准</td>
    <td style="font-size:14px;color:{{主题色}};font-weight:600;padding:8px 10px;text-align:center;">⭐⭐⭐⭐⭐</td>
  </tr>
</table>
<p style="font-size:15px;color:#333;line-height:1.75;margin:0 0 14px;">Google、Microsoft 等大厂已在采用……</p>
<h2 style="font-size:19px;color:#1a1a1a;margin:24px 0 14px;border-left:4px solid {{主题色}};padding-left:14px;">怎么接入？</h2>
<p style="font-size:15px;color:#333;line-height:1.75;margin:0 0 10px;">接入说明……</p>
<pre style="background:#1e1b4b;color:#e2e8f0;padding:14px;font-size:14px;line-height:1.6;"><code>npm install @copilotkit/react-core</code></pre>
<hr style="border:0;border-top:1px solid #cbd5e1;margin:28px 0;">
<table width="100%" cellpadding="14" cellspacing="0" border="0" style="background:{{数据卡底色}};text-align:center;">
  <tr><td>
    <p style="font-size:16px;font-weight:600;color:{{主题色}};margin:0 0 12px;">{{CTA 问题}}</p>
    <p style="font-size:14px;color:#666;margin:0 0 6px;">A. React 生态（Next.js / Remix）⚛️</p>
    <p style="font-size:14px;color:#666;margin:0 0 6px;">B. 自研框架 + 自定义协议 🛠️</p>
    <p style="font-size:14px;color:#666;margin:0 0 12px;">C. 还在调研中，等生态更成熟 👀</p>
  </td></tr>
</table>
<p style="font-size:13px;color:#999;text-align:center;margin:16px 0 0;">🧡 欢迎<strong style="color:{{主题色}};">点赞、收藏、转发</strong>给同样在搭 AI 应用的伙伴～</p>
<p style="font-size:13px;color:#999;text-align:center;margin:8px 0 0;">{{关注引导语}}</p>
```
