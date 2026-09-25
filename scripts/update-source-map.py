"""Refresh the line-level source map for the site's unbundled, readable CSS."""

import json
from pathlib import Path


root = Path(__file__).resolve().parent.parent
css = (root / "style.css").read_text(encoding="utf-8")
source = css.split("/*# sourceMappingURL=", 1)[0].rstrip() + "\n"
source_map = {
    "version": 3,
    "file": "style.css",
    "sources": ["style.css"],
    "sourcesContent": [source],
    "names": [],
    "mappings": ";".join(["AAAA"] + ["AACA"] * (len(source.splitlines()) - 1)),
}
(root / "style.css.map").write_text(
    json.dumps(source_map, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
)
(root / "style.css").write_text(
    source + "\n/*# sourceMappingURL=style.css.map */\n", encoding="utf-8"
)
