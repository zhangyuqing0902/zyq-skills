[中文](./README.md) · **English**

# ZYQ Skills

A personal monorepo for reusable AI agent skills

**License:** [MIT](./LICENSE) · **Skills:** 1 · **Standard:** [Agent Skills](https://agentskills.io)

**Platforms:** Codex · Claude Code · OpenCode · OpenClaw

This repository collects my reusable AI agent skills. Each skill lives in its own top-level folder and follows the Agent Skills `SKILL.md` structure, so skills can be installed, updated, and shared independently.

- **Skills** - structured instructions that agents can load automatically
- **Monorepo layout** - one repository, many independent skill folders
- **Offline-first** - local workflows are preferred whenever practical

---

## Directory

### Skills

| Name | One-liner | Entry |
|---|---|---|
| [**doc2html**](#doc2html) | Convert documents into standalone offline interactive HTML reports | [SKILL.md](./doc2html/SKILL.md) |

---

## Installation

In Codex, Claude Code, OpenCode, OpenClaw, or another agent that supports Skills, say:

```text
Install this skill: https://github.com/zhangyuqing0902/zyq-skills/tree/main/<skill-name>
```

After publishing this repository to GitHub, install `doc2html` with:

```text
Install this skill: https://github.com/zhangyuqing0902/zyq-skills/tree/main/doc2html
```

For manual installation, copy the skill folder into your agent's skills directory:

```bash
cp -R doc2html ~/.codex/skills/
```

---

## Skills

<a id="-skills"></a>

<table>
<tr><td>

<a id="doc2html"></a>

### doc2html

Doc2HTML converts document inputs into a standalone offline interactive HTML webpage or report. It is designed for Feishu/Lark document links, Word/DOCX, PDF, Markdown, HTML, rich text, and pasted document content.

**What it does**

- Identifies the source type and chooses the right local or Feishu/Lark extraction path
- Reads the actual content structure, including sections, tables, images, attachments, concepts, and terminology
- Generates three visual style directions before building the final HTML
- Produces a single-file, offline-first, responsive, print-friendly HTML page
- Preserves source traceability through a new-tab link or local source download
- Runs static validation to catch CDN, remote font, telemetry, or runtime network dependencies

**Good for**

- Turning Feishu/Lark documents into offline web reports
- Converting Word, PDF, or Markdown into static pages
- Packaging source material into an HTML report with navigation, a top button, and source traceability

**Example prompts**

```text
Use $doc2html to turn this document into an offline interactive HTML report.
Convert this Feishu document into an offline HTML webpage.
Turn this PDF into a printable interactive web report.
```

-> [SKILL.md](./doc2html/SKILL.md)

</td></tr>
</table>

---

## Repository Layout

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

To add another skill, create a new top-level folder:

```text
new-skill/
├── SKILL.md
├── references/
├── scripts/
└── assets/
```

Only `SKILL.md` is required. Add `references/`, `scripts/`, and `assets/` only when the skill needs them.

---

[MIT License](./LICENSE)
