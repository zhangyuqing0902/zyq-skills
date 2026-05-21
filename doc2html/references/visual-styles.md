# Visual Style Guidance

## Core Principle

Design must fit the current document and any user-specified design requirement. Keep it restrained, clean, and content-led. Avoid over-design, generic AI aesthetics, glowing neural networks, excessive gradients, decorative orbs, and style choices that obscure reading.

## Three Direction Requirement

Before producing the final HTML, provide three visual directions:

- Label them A, B, C.
- Make them meaningfully different.
- Tie each direction to the document type and audience.
- Include a concise rationale for why it fits.

In Codex, generate three main-visual images using image2 when available. This skill is optimal in Codex because the multi-style visual direction step can use Codex's image2 capability.

If used in Claude Code or another agent without image2:

1. Prefer that the user specifies a design style or uploads a reference image.
2. If the user does neither, infer a style from the document content and proceed with a restrained self-designed direction.
3. Explicitly state that image2-based visual previews are unavailable in the current agent.

## Suggested Style Families

Choose based on content, not personal preference:

- Research/report: editorial, quiet grids, strong hierarchy, measured accent color.
- Data/metrics: dashboard-like information architecture, tables and metric cards, restrained charts.
- Proposal/strategy: executive brief, section bands, decision blocks, timeline.
- Tutorial/guide: readable handbook, callouts, steps, examples.
- Product/design: visual-first but still clear, screenshots/mockups when relevant.
- Legal/policy: conservative, high readability, careful source and section numbering.

## Animation

Use subtle local CSS animation only when it improves comprehension:

- Hover scale and border highlight for blocks.
- Gentle reveal or section emphasis.
- Sticky or floating top button.
- Simple progress or timeline transitions.

Avoid motion that distracts from reading. Respect `prefers-reduced-motion`.
