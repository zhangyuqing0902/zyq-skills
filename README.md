**中文** · [English](./README.en.md)

# ZYQ Skills

我自己沉淀和维护的 AI Skills 聚合仓库

**License:** [MIT](./LICENSE) · **Skills:** 1 · **Standard:** [Agent Skills](https://agentskills.io)

**支持平台:** Codex · Claude Code · OpenCode · OpenClaw

这里是我的 Skills 集合。每个 Skill 都是仓库根目录下的一个独立文件夹，遵循 Agent Skills 的 `SKILL.md` 结构，方便单独安装、更新和分发。

- **Skills** - Agent 可自动加载的结构化指令集
- **单仓库聚合** - 一个仓库管理多个 Skill，每个 Skill 仍保持独立目录
- **离线优先** - 能本地完成的工作默认不依赖外部服务

---

## 目录

### Skills

| 名字 | 一句话 | 入口 |
|---|---|---|
| [**doc2html（文档转离线交互式网页）**](#doc2html) | 把飞书文档、Word、PDF、Markdown、HTML 或富文本转成单文件离线交互式 HTML 报告 | [SKILL.md](./doc2html/SKILL.md) |

---

## 安装方式

在 Codex、Claude Code、OpenCode、OpenClaw 等支持 Skill 的 Agent 里，直接说：

```text
帮我安装这个 skill：<你的 GitHub 仓库地址>/tree/main/<skill-name>
```

例如发布到 GitHub 后安装 `doc2html`：

```text
帮我安装这个 skill：<你的 GitHub 仓库地址>/tree/main/doc2html
```

手动安装时，把对应 Skill 文件夹复制到你的 Agent Skills 目录即可：

```bash
cp -R doc2html ~/.codex/skills/
```

---

## Skills

<a id="-skills"></a>

<table>
<tr><td>

<a id="doc2html"></a>

### doc2html（文档转离线交互式网页）

把文档输入转成一个可离线打开的交互式 HTML 页面或报告。适合把飞书/Lark 文档链接、Word/DOCX、PDF、Markdown、HTML、富文本或粘贴内容整理成视觉完成度更高的静态网页。

**它会做什么**

- 先识别来源类型，并按来源选择本地解析或飞书/Lark 提取流程
- 读取真实内容结构，保留章节、表格、图片、附件、概念和术语
- 生成最终 HTML 前，先给出三种视觉风格方向
- 输出单文件、离线优先、响应式、可打印的 HTML
- 保留原始来源追溯：链接新窗口打开，本地源文件可下载
- 做静态校验，确认无 CDN、远程字体、遥测或运行时网络依赖

**适合**

- 把飞书文档整理成离线网页版汇报
- 把 Word / PDF / Markdown 变成可浏览、可打印的静态页面
- 把资料包转换成带目录、置顶按钮、来源追溯的 HTML 报告

**触发示例**

```text
Use $doc2html to turn this document into an offline interactive HTML report.
把这个飞书文档转成离线 HTML 网页。
把这个 PDF 做成一份可打印的交互式网页报告。
```

-> [SKILL.md](./doc2html/SKILL.md)

</td></tr>
</table>

---

## 仓库结构

```text
zyq-skills/
├── README.md
├── README.en.md
├── LICENSE
├── .gitignore
└── doc2html/
    ├── SKILL.md
    ├── agents/
    ├── assets/
    ├── references/
    └── scripts/
```

新增 Skill 时，在仓库根目录创建一个新的同级文件夹即可：

```text
new-skill/
├── SKILL.md
├── references/
├── scripts/
└── assets/
```

只有 `SKILL.md` 是必需的；`references/`、`scripts/`、`assets/` 按需要添加。

---

[MIT License](./LICENSE)
