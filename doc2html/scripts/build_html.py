#!/usr/bin/env python3
"""Create a minimal Doc2HTML-compliant starter HTML from the bundled template."""

from __future__ import annotations

import argparse
import html
from pathlib import Path
from urllib.parse import urlparse


def render_source(source: str) -> str:
    parsed = urlparse(source)
    if parsed.scheme in {"http", "https"}:
        escaped = html.escape(source, quote=True)
        return f'<a href="{escaped}" target="_blank" rel="noopener noreferrer">{escaped}</a>'
    return html.escape(source)


def main() -> int:
    parser = argparse.ArgumentParser(description="Build a starter offline HTML report.")
    parser.add_argument("--title", required=True, help="HTML title and H1")
    parser.add_argument("--subtitle", default="", help="Hero subtitle")
    parser.add_argument("--source", default="未提供", help="Source label/link text")
    parser.add_argument("--content-file", help="Optional HTML fragment to inject")
    parser.add_argument("--output", required=True, help="Output HTML path")
    parser.add_argument(
        "--template",
        default=str(Path(__file__).resolve().parents[1] / "assets/templates/single-file-report.html"),
        help="Template path",
    )
    args = parser.parse_args()

    template = Path(args.template).read_text(encoding="utf-8")
    content = ""
    if args.content_file:
        content = Path(args.content_file).read_text(encoding="utf-8")
    else:
        content = "<section><h2>内容待整理</h2><div class=\"card\"><p>请将结构化后的文档内容替换到这里。</p></div></section>"

    rendered = (
        template.replace("{{TITLE}}", html.escape(args.title))
        .replace("{{SUBTITLE}}", html.escape(args.subtitle))
        .replace("{{SOURCE}}", render_source(args.source))
        .replace("{{CONTENT}}", content)
    )

    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(rendered, encoding="utf-8")
    print(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
