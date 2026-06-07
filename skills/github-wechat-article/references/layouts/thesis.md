#### 各布局详细规范

##### ① LAYOUT_THESIS — 论文式布局（配对 SCHOLAR）

```
核心原则：像读一篇严谨的论文，先建立信任再展示方案。

【段落顺序】
h1 标题
├─ p 开篇钩子（2 段，制造认知冲突）
├─ p 封面图（在引子完成、读者产生好奇后出现——约第 3 段位置）
├─ h2 "为什么它值得你关注？"
├─ p 项目介绍（直接以段落叙述，融入数据；不使用独立数据卡片）
│   示例："open-notebook 在 GitHub 上获得了 2.6 万 Star，137 位贡献者
│   参与了开发。它的核心承诺很简单：复刻 NotebookLM 的全部体验，但
│   让你拥有数据的绝对控制权。"
├─ h2 "核心技术深度拆解"
├─ p 功能 1（论点-论据式，不用编号卡片）
│   格式：<strong style="color:{{主题色}};">隐私架构。</strong> 论据叙述……
├─ blockquote 引用社区评价（替代数据卡片）
├─ p 功能 2（同上论点-论据式）
├─ p 功能 3（同上）
├─ h2 "谁在用？效果如何？"
├─ p 适用场景叙述（不用 table 清单，用流畅段落）
│   格式："目前主要用户群体包括：研究人员用它做文献综述，律师用它
│   分析合同条款，……"
├─ h2 "一分钟上手"
├─ p 安装说明 + 体验链接（如有在线 Demo 优先推荐）
├─ hr 分割线
└─ CTA：开放式提问段落（无 ABC 选项）

【数据卡格式】无独立数据卡片，Star/许可证等数据融入项目介绍段落中
【功能展示】论点-论据式：<strong>关键词。</strong> 论据展开。每个论点后用小号灰色文字标出处
【「适合谁用」格式】段落叙述，不用表格
【封面位置】第 3 段位置（引子完成、问题充分铺垫后）
【间距密/疏】疏朗：h2 上下 margin 30px/18px，段间距 18px，行高 1.9
【分割线】细实线：<hr style="border:0;border-top:1px solid #d1d5db;margin:32px 0;">
【h2 装饰】仅文字，不加 border-left（保持学术克制感）
【安装代码块】无代码块，改用段落文字说明（保持学术风，不用 terminal 风格）

【完整 HTML 模板】
<h1 style="font-size:24px;color:#1a1a1a;text-align:center;margin:0 0 24px;line-height:1.5;">标题</h1>
<p style="font-size:16px;color:#333;line-height:1.9;margin:0 0 18px;">开篇钩子第一段……</p>
<p style="font-size:16px;color:#333;line-height:1.9;margin:0 0 18px;">开篇钩子第二段……</p>
<p style="text-align:center;margin:20px 0;"><img src="data:image/png;base64,..." alt="" style="max-width:100%;"></p>
<h2 style="font-size:18px;color:#1a1a1a;margin:30px 0 18px;">为什么它值得你关注？</h2>
<p style="font-size:15px;color:#333;line-height:1.9;margin:0 0 18px;">项目介绍段落，融入 Star 数和许可证等关键数据……</p>
<h2 style="font-size:18px;color:#1a1a1a;margin:30px 0 18px;">核心技术深度拆解</h2>
<p style="font-size:15px;color:#333;line-height:1.9;margin:0 0 18px;"><strong style="color:{{主题色}};">隐私架构。</strong> 论据展开说明……</p>
<blockquote style="border-left:3px solid {{主题色}};background:{{数据卡底色}};margin:20px 0;padding:12px 16px;"><p style="font-size:14px;color:#555;margin:0;">「引用社区真实评价或第三方评测数据」</p></blockquote>
<p style="font-size:15px;color:#333;line-height:1.9;margin:0 0 18px;"><strong style="color:{{主题色}};">多模型支持。</strong> 论据展开说明……</p>
<p style="font-size:15px;color:#333;line-height:1.9;margin:0 0 18px;"><strong style="color:{{主题色}};">研究增强。</strong> 论据展开说明……</p>
<h2 style="font-size:18px;color:#1a1a1a;margin:30px 0 18px;">谁在用？效果如何？</h2>
<p style="font-size:15px;color:#333;line-height:1.9;margin:0 0 18px;">目前主要用户群体包括：……</p>
<h2 style="font-size:18px;color:#1a1a1a;margin:30px 0 18px;">一分钟上手</h2>
<p style="font-size:15px;color:#333;line-height:1.9;margin:0 0 18px;">最快的试用方式是……（推荐在线体验或安装步骤）</p>
<hr style="border:0;border-top:1px solid #d1d5db;margin:32px 0;">
<p style="font-size:15px;color:#333;line-height:1.8;margin:0 0 12px;text-align:center;">{{开放式提问 CTA}}</p>
<p style="font-size:13px;color:#999;text-align:center;margin:16px 0 0;">🧡 欢迎<strong style="color:{{主题色}};">点赞、收藏、转发</strong>给需要的朋友～</p>
<p style="font-size:13px;color:#999;text-align:center;margin:8px 0 0;">{{关注引导语}}</p>
```
