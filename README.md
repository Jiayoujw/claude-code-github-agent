# Claude Code GitHub Agent

> 在 Claude Code 中直接搜、看、比、存 GitHub 项目的智能技能套件

## 🚀 快速安装

```bash
# 复制命令到你的项目
cp -r commands/ 你的项目/.claude/commands/
```

或在 Claude Code 中直接使用：把 `commands/` 下的文件放到你项目的 `.claude/commands/` 目录，重启 Claude Code 即可。

**前提条件**：
- 已安装 [GitHub CLI](https://cli.github.com/) 并通过 `gh auth login` 认证
- 使用 Claude Code（支持 DeepSeek 等任意模型）

## 📦 8 个命令

| 优先级 | 命令 | 功能 | 示例 |
|:--:|------|------|------|
| **P0** | `/github-trending` | 发现本周热门 | `/github-trending AI 编程` |
| **P0** | `/github-recommend` | 基于 Star 历史个性化推荐 | `/github-recommend` |
| **P1** | `/github-analyze` | 深度解读：架构/代码/社区/上手 | `分析 owner/repo` |
| **P1** | `/github-compare` | 横向对比选型 | `对比 ECC 和 superpowers` |
| **P1** | `/github-me` | 个人中心：收件箱+关注+状态 | `/github-me` |
| **P1** | `/github-weekly` | 定时推送+项目监控 | `设置 GitHub 每周推送` |
| **P2** | `/github-check` | 安全扫描：License/漏洞/活跃度 | `检查 owner/repo` |
| **P2** | `/github-contribute` | Fork/Issue/PR 完整流程 | `Fork owner/repo` |

## 🔗 协作流程

```
/github-trending ──→ 发现项目
       │
  ┌────┼────┐
  ↓    ↓    ↓
analyze compare recommend
  │    │    │
  └────┼────┘
       ↓
  Star / Clone / 关注
       │
  ┌────┼────┐
  ↓         ↓
github-me  github-weekly
(管理)     (监控推送)
```

## 🛠️ 技术栈

- **Claude Code** - AI 编程代理
- **DeepSeek V4** - 底层模型（或其他兼容模型）
- **GitHub CLI (`gh`)** - 已认证，直接操作 GitHub
- **WebSearch + WebFetch** - 搜索和抓取项目信息

## 📂 文件结构

```
.claude/commands/
├── github-trending.md      # P0 发现热门
├── github-recommend.md     # P0 个性化推荐
├── github-analyze.md       # P1 深度解读
├── github-compare.md       # P1 对比选型
├── github-me.md            # P1 个人中心
├── github-weekly.md        # P1 定时推送
├── github-check.md         # P2 安全扫描
└── github-contribute.md    # P2 贡献工作流
```

## 🔄 更新日志

### v2.0 (2026-06-01)
- ✅ 新增 P0: 个性化推荐（基于 Star 画像）
- ✅ 新增 P1: 个人中心（收件箱+关注列表）
- ✅ 新增 P2: 安全扫描
- ✅ 新增 P2: Fork/Issue/PR 工作流

### v1.0 (2026-05-31)
- ✅ 发现 Trending
- ✅ 深度解读
- ✅ 对比选型
- ✅ 定时推送
- ✅ Star/Clone 操作

## 📝 License

MIT - 随意使用、修改、分享
