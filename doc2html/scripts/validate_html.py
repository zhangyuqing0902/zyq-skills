#!/usr/bin/env python3
"""Validate Doc2HTML offline HTML output."""

from __future__ import annotations

import argparse
import re
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse


class Checker(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.ids: set[str] = set()
        self.external_runtime_assets: list[str] = []
        self.source_links: list[str] = []
        self.has_top_button = False
        self.has_print_css = False
        self.has_viewport = False
        self._in_style = False
        self._style_chunks: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        data = dict(attrs)
        if "id" in data and data["id"]:
            self.ids.add(data["id"])
        if tag == "meta" and data.get("name") == "viewport":
            self.has_viewport = True
        if tag == "style":
            self._in_style = True
        if tag == "a":
            href = data.get("href") or ""
            if href == "#top":
                self.has_top_button = True
            if href.startswith(("http://", "https://", "data:")):
                self.source_links.append(href)
        if tag in {"script", "img", "iframe", "source", "video", "audio"}:
            src = data.get("src") or ""
            if _is_external(src):
                self.external_runtime_assets.append(src)
        if tag == "link":
            href = data.get("href") or ""
            rel = (data.get("rel") or "").lower()
            if _is_external(href) and ("stylesheet" in rel or "preload" in rel):
                self.external_runtime_assets.append(href)

    def handle_endtag(self, tag: str) -> None:
        if tag == "style":
            self._in_style = False

    def handle_data(self, data: str) -> None:
        if self._in_style:
            self._style_chunks.append(data)

    def close(self) -> None:
        super().close()
        css = "\n".join(self._style_chunks)
        self.has_print_css = "@media print" in css


def _is_external(value: str) -> bool:
    if not value:
        return False
    parsed = urlparse(value)
    return parsed.scheme in {"http", "https", "//"}


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate an offline Doc2HTML file.")
    parser.add_argument("html_file")
    args = parser.parse_args()

    text = Path(args.html_file).read_text(encoding="utf-8")
    checker = Checker()
    checker.feed(text)
    checker.close()

    failures: list[str] = []
    if "top" not in checker.ids:
        failures.append("missing id=\"top\" anchor")
    if not checker.has_top_button:
        failures.append("missing top button link href=\"#top\"")
    if not checker.has_viewport:
        failures.append("missing viewport meta")
    if not checker.has_print_css:
        failures.append("missing @media print CSS")
    if checker.external_runtime_assets:
        failures.append("external runtime assets found: " + ", ".join(checker.external_runtime_assets))
    if not checker.source_links:
        failures.append("missing source traceability link or embedded download")
    if re.search(r"https?://(fonts|cdn|unpkg|jsdelivr|cdnjs)\.", text):
        failures.append("CDN/font URL found")

    if failures:
        for failure in failures:
            print(f"FAIL: {failure}")
        return 1

    print("OK: offline HTML checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
