#!/usr/bin/env python3
"""Generate an HTML download anchor that embeds a local source file as a data URL."""

from __future__ import annotations

import argparse
import base64
import html
import mimetypes
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(description="Embed a source file as a downloadable HTML link.")
    parser.add_argument("file", help="Local source file")
    parser.add_argument("--label", default=None, help="Link label")
    parser.add_argument(
        "--max-mb",
        type=float,
        default=15.0,
        help="Warn when the file is larger than this size; still embeds unless --strict is used",
    )
    parser.add_argument("--strict", action="store_true", help="Fail instead of warning when file is large")
    args = parser.parse_args()

    path = Path(args.file)
    if not path.is_file():
        raise SystemExit(f"not a file: {path}")

    size_mb = path.stat().st_size / (1024 * 1024)
    if size_mb > args.max_mb:
        message = f"warning: {path.name} is {size_mb:.1f} MB; consider packaging as a companion file"
        if args.strict:
            raise SystemExit(message)
        print(f"<!-- {html.escape(message)} -->")

    mime = mimetypes.guess_type(path.name)[0] or "application/octet-stream"
    data = base64.b64encode(path.read_bytes()).decode("ascii")
    label = args.label or f"下载原文：{path.name}"
    safe_name = html.escape(path.name, quote=True)
    safe_label = html.escape(label)
    print(f'<a href="data:{mime};base64,{data}" download="{safe_name}">{safe_label}</a>')
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
