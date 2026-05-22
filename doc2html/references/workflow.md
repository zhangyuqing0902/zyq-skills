# Doc2HTML Workflow

## 1. Intake

Identify source type and user goals:

- Source: Feishu/Lark URL, DOCX, PDF, Markdown, HTML, rich text, pasted content, or mixed attachments.
- Desired style: user-specified style, reference image, or no explicit preference.
- Output mode: single HTML, or packaged HTML plus source files when embedding is impractical.
- Audience and use case: report, proposal, tutorial, dashboard, presentation-like webpage, knowledge page, review artifact.

Ask only when a missing answer blocks safe execution. Style confirmation is always blocking: never proceed to final HTML generation until the user confirms one visual direction.

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

Before final HTML, generate three style directions:

- A/B/C labels.
- Distinct but content-appropriate layouts.
- Short notes on typography, palette, density, and interaction.
- Actual main-visual images for each direction when running in Codex.
- Wait for the user to choose or adjust.

In Codex, use image2 for visual direction images. Text-only style descriptions are not sufficient. Do not pick a direction on the user's behalf, even if one direction seems obviously suitable. If image generation is unavailable or fails, stop and ask the user whether to retry image generation, provide a reference image, or choose from text-only directions as an explicit fallback.

In non-Codex environments, ask for a style/reference image or infer a restrained style only after stating that image2-based visual previews are unavailable.

## 5. HTML Build

Build a standalone HTML:

- Inline CSS and minimal inline JS only when needed.
- No CDN, remote fonts, analytics, telemetry, or backend dependency.
- Responsive desktop/mobile layout.
- Navigation selection:
  - If the document has 5 or fewer primary sections, default to a fixed sticky top navigation menu.
  - If the document has more than 5 primary sections, default to a fixed left navigation menu.
  - User instructions override this default when explicit.
- Navigation behavior:
  - Any navigation menu must remain fixed while scrolling.
  - As the page scrolls, the corresponding menu tab must become active and remain visible in the menu.
  - Left navigation must collapse/expand. In expanded state, reserve layout space or shrink content so the menu never covers the body content.
  - Top horizontal navigation must support overflow with a subtle rounded scroll hint arrow that does not cover text.
- Hero:
  - Place the document title centered in the hero.
  - Use a polished, restrained title style.
  - Keep the desktop title on one line when practical; on narrow screens allow wrapping to avoid overflow.
  - Ensure a left navigation layout never covers or visually compresses the title.
- Icon-only upward arrow top button.
- Source link/download at the bottom of the page for URL sources.
- Print CSS.
- Hover/animation effects for important modules and tables: highlight, restrained scale/elevation, and clear focus states.
- Add a top-of-content visual summary: one content-specific summary image, diagram, or designed block that helps readers discuss the document as a whole.
- Add other content-appropriate visual aids: process diagrams, flow blocks, highlighted callouts, and emphasized key text where useful.
- Avoid low-value generated counts such as h1/h2 totals in the hero or summary unless the user asks.
- Avoid low-value operational metadata such as data statistics time, owner/person-in-charge, or administrative fields unless the user asks or those fields are essential source content.
- Terms explained where they matter.

## 6. Validate And Report

Run `scripts/validate_html.py <html>` and any available rendering checks. Final response should include:

- Output file path.
- Source handling summary.
- Validation result.
- Any limitations, such as blocked browser rendering or source files too large to embed.
