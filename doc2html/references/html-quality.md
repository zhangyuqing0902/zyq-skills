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
- Fixed navigation chosen by document scale:
  - 5 or fewer primary sections: fixed sticky top navigation menu.
  - More than 5 primary sections: fixed left navigation menu.
  - Explicit user requests override the default.
- Navigation behavior:
  - Current section tab highlights while scrolling.
  - Active tab stays visible within the menu.
  - Left navigation supports collapse/expand; expanded panels reserve layout space or shrink content and never cover body content.
  - Top horizontal navigation overflow uses a subtle rounded scroll hint arrow that does not cover text.
- Hero title is centered, visually polished, and single-line on desktop when practical. It must not be covered or squeezed by a left navigation panel.
- Top button anchored to the top of the page, shown as an icon-only upward arrow rather than text.
- Source traceability:
  - URL source appears at the bottom of the page and opens in a new tab with `target="_blank"` and `rel="noopener noreferrer"`.
  - Local source file can be downloaded from the page, preferably embedded with a `data:` URL when file size is reasonable.
- Print CSS that hides floating controls and preserves readable sections.
- Clear heading hierarchy and table styling.
- Visual block hover/highlight interaction unless user requests static output.
- Tables and important modules must have hover highlight plus restrained scale/elevation or equivalent interaction feedback.
- Add one top-of-content visual summary image, diagram, or designed block that summarizes the document for whole-team discussion.
- Add other content-appropriate visual aids such as process diagrams, flow blocks, highlighted callouts, and emphasized key phrases when they improve reading.
- Do not place generated metadata counts such as "number of h1/h2 sections" in the hero or summary unless the user asks for those counts.
- Do not show low-value operational metadata such as data statistics time, owner/person-in-charge, or administrative fields unless the user asks or the source requires them.
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
4. Source traceability exists at the bottom for URL sources.
5. Mobile CSS exists.
6. Print CSS exists.
7. User-chosen visual style is reflected.
8. Navigation matches section count or explicit user instruction: top nav for 5 or fewer primary sections; collapsible left nav for more than 5.
9. Navigation stays fixed, synchronizes active tab on scroll, and keeps active tab visible.
10. Left navigation, when used, can collapse/expand and does not cover content when expanded.
11. Top navigation, when used and overflowing, has a polished rounded scroll hint arrow that does not cover text.
12. Hero title is centered, designed, and not covered or compressed by navigation.
13. Important modules and tables include hover/highlight interactions.
14. A top-of-content visual summary exists, plus other useful diagrams, high-emphasis blocks, or highlighted key text when supported.
15. Content avoids low-value counts and administrative metadata unless requested or essential.
16. Content coverage checklist is complete or limitations are reported.

Use `scripts/validate_html.py <html>` when available.
