##### ④ LAYOUT_LETTER — 书信式布局（配对 MENTOR）

```
核心原则：像收到一封前辈的来信，娓娓道来一个真实的故事。结构天然、不刻意。

【段落顺序】
h1 标题
├─ p 开篇钩子（作者故事第一段——"X 年前，他是……"）
├─ p 故事第二段——转折
├─ p 故事第三段——结局（拿下 Offer / 做出项目）
├─ p 封面图（故事讲完后才出现——"这就是他留下的宝藏"）
├─ h2 "它的来历？一个真实的故事"
├─ p 补充作者背景 + 项目由来
├─ table 数据卡片（简约，仅 2 行：Star + License）
├─ h2 "里面有什么？帮你省半年的精华"
├─ blockquote "📖 第一部分：[名称]" → p 内容描述
├─ blockquote "📖 第二部分：[名称]" → p 内容描述
├─ blockquote "📖 第三部分：[名称]" → p 内容描述
├─ hr 分割线
├─ h2 "适合谁？不适合谁？"
├─ p 叙事体适���场景（"如果你也像当年的他一样……" 不用表格）
├─ h2 "怎么开始？"
├─ p 最简单的入手方式（链接/安装）
├─ hr
└─ CTA：阶段式投票

【数据卡格式】极简 2 行表：仅 Star + License，无其他干扰信息
【功能展示】章回式 blockquote：每部分用带书名号的 blockquote 标题 + p 展开
【「适合谁用」格式】叙事体段落："如果你也……"，不用表格清单
【封面位置】故事讲完后（"这就是他留下的宝藏"）
【间距密/疏】温暖舒适：h2 margin 26px/16px，段间距 16px，行高 1.85
【分割线】柔和虚线：<hr style="border:0;border-top:1px dashed #d8b4fe;margin:28px 0;">
【h2 装饰】border-left:3px solid {{主题色}} + padding-left:14px（左侧细线，比别的布局细）

【完整 HTML 模板】
<h1 style="font-size:24px;color:#1a1a1a;text-align:center;margin:0 0 24px;line-height:1.5;">标题</h1>
<p style="font-size:15px;color:#333;line-height:1.85;margin:0 0 16px;">故事第一段……</p>
<p style="font-size:15px;color:#333;line-height:1.85;margin:0 0 16px;">故事第二段……</p>
<p style="font-size:15px;color:#333;line-height:1.85;margin:0 0 16px;">故事第三段——引出项目……</p>
<p style="text-align:center;margin:20px 0;"><img src="data:image/png;base64,..." alt="" style="max-width:100%;"></p>
<h2 style="font-size:19px;color:#1a1a1a;margin:26px 0 16px;border-left:3px solid {{主题色}};padding-left:14px;">它的来历？一个真实的故事</h2>
<p style="font-size:15px;color:#333;line-height:1.85;margin:0 0 16px;">补充作者背景和项目由来……</p>
<table width="100%" cellpadding="10" cellspacing="0" border="0" style="background:{{数据卡底色}};margin:16px 0;">
  <tr><td style="font-size:14px;color:#666;padding:6px 10px;">⭐ Stars</td><td style="font-size:14px;color:{{主题色}};font-weight:600;padding:6px 10px;">350k</td></tr>
  <tr><td style="font-size:14px;color:#666;padding:6px 10px;">📝 协议</td><td style="font-size:14px;color:#059669;padding:6px 10px;">CC-BY-SA-4.0</td></tr>
</table>
<h2 style="font-size:19px;color:#1a1a1a;margin:26px 0 16px;border-left:3px solid {{主题色}};padding-left:14px;">里面有什么？帮你省半年的精华</h2>
<blockquote style="border-left:3px solid {{强调色}};background:{{功能卡底色}};margin:14px 0;padding:8px 14px;"><p style="font-size:14px;color:{{主题色}};font-weight:600;margin:0;">📖 第一部分：[名称]</p></blockquote>
<p style="font-size:15px;color:#333;line-height:1.85;margin:0 0 14px;">内容描述……</p>
<blockquote style="border-left:3px solid {{强调色}};background:{{功能卡底色}};margin:14px 0;padding:8px 14px;"><p style="font-size:14px;color:{{主题色}};font-weight:600;margin:0;">📖 第二部分：[名称]</p></blockquote>
<p style="font-size:15px;color:#333;line-height:1.85;margin:0 0 14px;">内容描述……</p>
<hr style="border:0;border-top:1px dashed #d8b4fe;margin:28px 0;">
<h2 style="font-size:19px;color:#1a1a1a;margin:26px 0 16px;border-left:3px solid {{主题色}};padding-left:14px;">适合谁？不适合谁？</h2>
<p style="font-size:15px;color:#333;line-height:1.85;margin:0 0 16px;">如果你也像 [作者/人群] 一样，[具体描述]，那这份 [资料/工具] 可能就是为你准备的……（叙事体，不用列表）</p>
<h2 style="font-size:19px;color:#1a1a1a;margin:26px 0 16px;border-left:3px solid {{主题色}};padding-left:14px;">怎么开始？</h2>
<p style="font-size:15px;color:#333;line-height:1.85;margin:0 0 16px;">最简单的入手方式……</p>
<hr style="border:0;border-top:1px dashed #d8b4fe;margin:28px 0;">
<table width="100%" cellpadding="14" cellspacing="0" border="0" style="background:{{数据卡底色}};text-align:center;">
  <tr><td>
    <p style="font-size:16px;font-weight:600;color:{{主题色}};margin:0 0 12px;">{{CTA 问题}}</p>
    <p style="font-size:14px;color:#666;margin:0 0 6px;">A. 正在自学中，求过来人经验 🙋</p>
    <p style="font-size:14px;color:#666;margin:0 0 6px;">B. 准备面试，需要系统复习 📝</p>
    <p style="font-size:14px;color:#666;margin:0 0 12px;">C. 已经上岸了，回来看看 👋</p>
  </td></tr>
</table>
<p style="font-size:13px;color:#999;text-align:center;margin:16px 0 0;">🧡 欢迎<strong style="color:{{主题色}};">点赞、收藏、转发</strong>给同样在路上的朋友～</p>
<p style="font-size:13px;color:#999;text-align:center;margin:8px 0 0;">{{关注引导语}}</p>
```
