# HTML Quality Bar

## Offline Requirements

The output should be a single standalone HTML file whenever practical:

- Inline CSS.
- Inline JavaScript only if needed.
- No CDN.
- No remote fonts.
- No analytics or telemetry.
- No backend service.
- No runtime fetch calls for content.

Remote source links are allowed only for traceability, not for required rendering.

## Required Page Features

- Responsive desktop and mobile layouts.
- Top/置顶 button anchored to the top of the page.
- Source traceability:
  - URL source opens in a new tab with `target="_blank"` and `rel="noopener noreferrer"`.
  - Local source file can be downloaded from the page, preferably embedded with a `data:` URL when file size is reasonable.
- Print CSS that hides floating controls and preserves readable sections.
- Clear heading hierarchy and table styling.
- Visual block hover/highlight interaction unless user requests static output.
- Term explanations for important abbreviations and jargon.
- Completeness checklist or summary of covered sections/tables/media.

## Source Embedding Policy

For Word/PDF/rich text local sources:

- Default to embedding the original source as a downloadable link in the HTML.
- If the file is too large for practical embedding, copy it into a `source/` folder or package with the HTML and explain that the HTML references a local companion file.

## Validation Checklist

Before final response:

1. HTML parses successfully.
2. No external runtime dependencies exist.
3. Required top button exists.
4. Source traceability exists.
5. Mobile CSS exists.
6. Print CSS exists.
7. User-chosen visual style is reflected.
8. Content coverage checklist is complete or limitations are reported.

Use `scripts/validate_html.py <html>` when available.
