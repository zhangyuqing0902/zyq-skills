---
name: doc2html
description: "Convert document inputs into standalone offline interactive HTML webpages. Use when the user asks to turn a Feishu/Lark document link, Word/DOCX, PDF, Markdown, HTML, rich text, or pasted document content into a polished visual static webpage/report with responsive layout, adaptive fixed navigation, top-of-content visual summary, source traceability, print support, top button, subtle interactions, and design-style exploration before final generation."
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
   - The three options must include actual main-visual images, not text-only descriptions.
   - Ask the user to choose or adjust a style before building the webpage.
   - Do not choose for the user, infer final visual direction, or build the HTML until the user explicitly confirms one direction.
   - In non-Codex agents, if image2 is unavailable, either require the user to specify a design style or upload a reference image; if neither is provided, infer a restrained style from the content and proceed only after stating that fallback.
   - Read `references/visual-styles.md`.

5. **Build the offline HTML.**
   - Prefer one standalone `.html` file with inline CSS/JS and no CDN, remote font, remote image, external backend, telemetry, or analytics.
   - Add restrained local CSS animations or transitions when they improve visual orientation.
   - Choose navigation by content scale unless the user explicitly specifies otherwise:
     - If the article has 5 or fewer primary sections, use a fixed sticky top navigation menu.
     - If it has more than 5 primary sections, use a fixed left navigation menu.
   - Any navigation menu must stay fixed while scrolling, highlight the current section tab as the page scrolls, and keep the active tab visible inside the menu.
   - Left navigation must support collapse/expand. When expanded, the right content area must automatically shrink or reserve space; the panel must not cover the content.
   - Top horizontal navigation must include a subtle scroll hint arrow when overflowing; the arrow must not cover menu text and should be rounded, restrained, and visually polished.
   - Hero title must be centered, visually designed, and kept on one line on desktop when practical. It must never be hidden or visually compressed by a left navigation panel.
   - Add clear hover interactions for important modules and tables: highlight, border emphasis, and restrained scale/elevation.
   - Add a content-specific summary visualization near the top of the page: a single visual summary image/diagram/block that helps readers discuss the document as a whole.
   - Include additional visual aids such as process diagrams, flow blocks, highlighted callouts, and emphasized key text when the content supports it.
   - Do not display low-value generated counts such as "number of h1/h2 sections" in the page hero or summary unless the user asks.
   - Do not show low-value operational metadata such as data statistics time, owner/person-in-charge, or other administrative fields unless the user asks or the source content requires it.
   - Include a visible top button as an icon-only upward arrow, not text like "置顶".
   - Put source traceability for URL sources at the bottom of the page, not in the hero/top area.
   - If the source is a link, the bottom source link must open in a new browser tab (`target="_blank"` with `rel="noopener noreferrer"`).
   - If the source is Word/PDF/rich text, embed the source file as a local download link by default when file size is reasonable; otherwise output an HTML plus source-file package and explain it.
   - Make desktop and mobile layouts first-class. Read `references/html-quality.md`.

6. **Validate.**
   - Run `scripts/validate_html.py <html>` or equivalent checks.
   - Verify no external runtime dependencies exist, required anchors are present, and the source link/download exists.
   - If browser validation is blocked by the environment, state that and report static checks.

## Required Output Features

- Single-file offline HTML whenever practical.
- Responsive desktop/mobile layout.
- Fixed navigation chosen by primary section count: top navigation for 5 or fewer primary sections; collapsible left navigation for more than 5, unless the user explicitly requests otherwise.
- Navigation scroll synchronization: current section tab is highlighted while scrolling and the active tab is kept visible.
- Desktop hero title centered, designed, and single-line when practical; it must not be covered or squeezed by a left navigation panel.
- Icon-only upward arrow top anchor button.
- Original source traceability: new-tab link for URLs; download link for local Word/PDF/rich text sources.
- Original source traceability for URLs belongs at the bottom of the page.
- Three design directions with actual main-visual images before final generation, followed by explicit user confirmation.
- Content-specific structure, not fixed schemas.
- Term explanation for domain abbreviations and jargon when useful.
- Section/table/media completeness checklist.
- Print-friendly CSS.
- Required subtle animations/hover highlights for important modules and tables unless the user requests static output.
- Top-of-content visual summary: a content-specific summary image/diagram/block for whole-document discussion, plus any additional flow diagrams, high-emphasis blocks, and highlighted key phrases that improve comprehension.

## Resources

- `references/workflow.md`: end-to-end operating procedure and user confirmation points.
- `references/extraction.md`: source-specific extraction guidance, including Feishu authorization/install fallbacks.
- `references/visual-styles.md`: design direction rules and image2/non-Codex behavior.
- `references/html-quality.md`: required HTML quality bar and validation checklist.
- `scripts/build_html.py`: create a minimal compliant starter HTML.
- `scripts/embed_source.py`: generate an HTML download link for local source files.
- `scripts/validate_html.py`: validate single-file HTML requirements.
- `assets/templates/single-file-report.html`: starter template for offline reports.
