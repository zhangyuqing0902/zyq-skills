# Extraction Guidance

## Feishu / Lark Links

When the source is a Feishu/Lark document link:

1. Check whether `lark-doc`, `lark-drive`, `lark-sheets`, `lark-base`, or other relevant `lark-*` skills are available.
2. Check whether `lark-cli` is available before using CLI commands.
3. Use user identity when required by local policy or when accessing user-owned resources.
4. If authorization or keychain/token state fails, guide the user through the minimal relevant Feishu authorization flow from `lark-shared`.
5. If skills or CLI are missing, tell the user plainly and guide installation. Do not fabricate content from the URL.
6. Always offer a fallback: ask the user to export/download the Feishu document as DOCX/PDF/Markdown/HTML and provide the file.

Feishu documents may contain embedded sheets, bitables, files, media, or whiteboards. When the fetched document exposes embedded resource tokens:

- Sheets: read the corresponding sheet with `lark-sheets`.
- Bitables: read with `lark-base`.
- Images/files: preview or download when needed for understanding or final output.
- If an embedded resource cannot be read, record it in the completeness checklist.

## Word / DOCX

Extract:

- Headings and hierarchy.
- Paragraphs, lists, footnotes/endnotes when relevant.
- Tables.
- Images and captions.
- Embedded files when accessible.

Preserve the original DOCX as a downloadable source link in the generated HTML when file size is reasonable.

## PDF

Use visual PDF tools when layout matters. Extract:

- Page order and section structure.
- Tables and figures.
- Captions, callouts, sidebars.
- Page references when useful.

If text extraction is poor, render pages and use visual interpretation. Preserve the PDF as a downloadable source link by default.

## Rich Text / Markdown / HTML

Preserve semantic structure:

- Headings.
- Lists.
- Tables.
- Links.
- Code blocks.
- Quotes/callouts.
- Images when local or embeddable.

Normalize only enough to create a coherent webpage. Do not flatten everything into generic cards.

## Dynamic Structure Rule

Never assume fixed fields such as `summary`, `metrics`, or `workflow` must exist. Infer fields from the source content. A technical design doc, academic report, contract review, and meeting summary should produce different structures and page sections.
