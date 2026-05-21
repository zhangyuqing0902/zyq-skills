# Doc2HTML Workflow

## 1. Intake

Identify source type and user goals:

- Source: Feishu/Lark URL, DOCX, PDF, Markdown, HTML, rich text, pasted content, or mixed attachments.
- Desired style: user-specified style, reference image, or no explicit preference.
- Output mode: single HTML, or packaged HTML plus source files when embedding is impractical.
- Audience and use case: report, proposal, tutorial, dashboard, presentation-like webpage, knowledge page, review artifact.

Ask only when a missing answer blocks safe execution. Otherwise proceed conservatively.

## 2. Source Readiness

For Feishu/Lark links, check ability before promising output:

1. Confirm relevant Feishu skills / `lark-cli` are available.
2. Attempt read with user identity where local policy requires it.
3. If authorization fails, guide minimal auth and stop until the user completes it.
4. Offer fallback: export/download the Feishu document as DOCX/PDF/Markdown/HTML and provide the local file.

For local files, confirm the file path is readable. For pasted content, preserve headings/tables/code blocks when possible.

## 3. Deep Reading And Dynamic Structure

Do not force a universal schema. Instead, build a document-specific content model:

- Title, subtitle, objective, audience.
- Natural sections and hierarchy.
- Tables and their semantic role.
- Figures/images/diagrams and captions.
- Processes, timelines, dependencies, decisions.
- Metrics, formulas, thresholds.
- Definitions, abbreviations, named methods.
- Prompts, code blocks, examples, appendices.
- Source links and downloadable originals.

Create a brief coverage checklist before finalizing:

- Sections read.
- Tables read.
- Media/attachments handled.
- Embedded documents/spreadsheets handled or explicitly not available.
- Ambiguities or missing data.

## 4. Visual Direction First

Before final HTML, generate or propose three style directions:

- A/B/C labels.
- Distinct but content-appropriate layouts.
- Short notes on typography, palette, density, and interaction.
- Wait for the user to choose or adjust.

In Codex, use image2 for visual direction images when available. In non-Codex environments, ask for a style/reference image or infer a restrained style and say so.

## 5. HTML Build

Build a standalone HTML:

- Inline CSS and minimal inline JS only when needed.
- No CDN, remote fonts, analytics, telemetry, or backend dependency.
- Responsive desktop/mobile layout.
- Top/置顶 button.
- Source link/download.
- Print CSS.
- Subtle hover/animation effects for orientation.
- Terms explained where they matter.

## 6. Validate And Report

Run `scripts/validate_html.py <html>` and any available rendering checks. Final response should include:

- Output file path.
- Source handling summary.
- Validation result.
- Any limitations, such as blocked browser rendering or source files too large to embed.
