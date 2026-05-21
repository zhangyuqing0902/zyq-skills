---
name: doc2html
description: "Convert document inputs into standalone offline interactive HTML webpages. Use when the user asks to turn a Feishu/Lark document link, Word/DOCX, PDF, Markdown, HTML, rich text, or pasted document content into a polished visual static webpage/report with responsive layout, source traceability, print support, top button, subtle interactions, and design-style exploration before final generation."
---

# Doc2HTML

Doc2HTML turns source documents into single-file, offline-first, responsive, interactive HTML reports. The user-facing Chinese name is **文档转离线交互式网页**.

## Non-Negotiable Workflow

1. **Identify source type.**
   - Feishu/Lark link: use the available `lark-*` skills and `lark-cli` when present.
   - Word/PDF/local rich text: extract locally with appropriate document/PDF tooling.
   - Pasted rich text/Markdown/HTML: parse from the prompt or local artifact.

2. **For Feishu/Lark links, run readiness checks before extraction.**
   - If `lark-doc` / relevant `lark-*` skills or `lark-cli` are unavailable, tell the user and guide installation. Do not pretend Feishu can be read.
   - If authorization is missing, expired, or permission is denied, tell the user to complete Feishu authorization and provide the minimal relevant command or flow from `lark-shared`.
   - Always offer a fallback: ask the user to export/download the Feishu content as DOCX/PDF/Markdown/HTML and provide the local file, then continue from the local file.
   - Read `references/extraction.md` for exact Feishu handling.

3. **Read deeply before designing.**
   - Do not use fixed extraction fields.
   - Derive the structure from the actual content: sections, tables, images, attachments, formulas, prompts, metrics, workflows, concepts, risks, examples, and any domain-specific entities.
   - Produce or maintain a coverage checklist so missing sections/tables/media are visible before finalizing.

4. **Generate three visual style directions before final HTML.**
   - In Codex, use image2/image generation to create three main-visual style options when available.
   - Ask the user to choose or adjust a style before building the webpage.
   - In non-Codex agents, if image2 is unavailable, either require the user to specify a design style or upload a reference image; if neither is provided, infer a restrained style from the content and proceed only after stating that fallback.
   - Read `references/visual-styles.md`.

5. **Build the offline HTML.**
   - Prefer one standalone `.html` file with inline CSS/JS and no CDN, remote font, remote image, external backend, telemetry, or analytics.
   - Add restrained local CSS animations or transitions when they improve visual orientation.
   - Include a visible top/置顶 button and source traceability.
   - If the source is a link, open it in a new browser tab (`target="_blank"` with `rel="noopener noreferrer"`).
   - If the source is Word/PDF/rich text, embed the source file as a local download link by default when file size is reasonable; otherwise output an HTML plus source-file package and explain it.
   - Make desktop and mobile layouts first-class. Read `references/html-quality.md`.

6. **Validate.**
   - Run `scripts/validate_html.py <html>` or equivalent checks.
   - Verify no external runtime dependencies exist, required anchors are present, and the source link/download exists.
   - If browser validation is blocked by the environment, state that and report static checks.

## Required Output Features

- Single-file offline HTML whenever practical.
- Responsive desktop/mobile layout.
- Top/置顶 anchor button.
- Original source traceability: new-tab link for URLs; download link for local Word/PDF/rich text sources.
- Three design directions before final generation.
- Content-specific structure, not fixed schemas.
- Term explanation for domain abbreviations and jargon when useful.
- Section/table/media completeness checklist.
- Print-friendly CSS.
- Optional subtle animations/hover highlights that remain professional and restrained.

## Resources

- `references/workflow.md`: end-to-end operating procedure and user confirmation points.
- `references/extraction.md`: source-specific extraction guidance, including Feishu authorization/install fallbacks.
- `references/visual-styles.md`: design direction rules and image2/non-Codex behavior.
- `references/html-quality.md`: required HTML quality bar and validation checklist.
- `scripts/build_html.py`: create a minimal compliant starter HTML.
- `scripts/embed_source.py`: generate an HTML download link for local source files.
- `scripts/validate_html.py`: validate single-file HTML requirements.
- `assets/templates/single-file-report.html`: starter template for offline reports.
