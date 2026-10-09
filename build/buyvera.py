"""Rebuild the Buyvera commercial site (Astro, project repo) as a sub-folder of the portfolio: /buyvera/.

The project repository is never modified: a temporary copy is patched (base path, prefixed routes,
draft banner removed, generic sector wording) then built, and dist/ replaces site/buyvera/.

Usage: python3 build/buyvera.py <path/to/site-commercial>   (or set BUYVERA_SRC)
"""
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

import os

_src = sys.argv[1] if len(sys.argv) > 1 else os.environ.get("BUYVERA_SRC")
if not _src:
    sys.exit("Indiquer le dossier site-commercial du projet : python3 build/buyvera.py <chemin> (ou BUYVERA_SRC)")
SRC = Path(_src)
SITE = Path(__file__).resolve().parent.parent
BASE = "/buyvera"


def sub(path, old, new, regex=False):
    s = path.read_text(encoding="utf-8")
    s2 = re.sub(old, new, s) if regex else s.replace(old, new)
    assert s2 != s, f"motif introuvable dans {path}: {old[:60]}"
    path.write_text(s2, encoding="utf-8")


with tempfile.TemporaryDirectory() as tmp:
    w = Path(tmp) / "site"
    shutil.copytree(SRC, w, ignore=shutil.ignore_patterns("node_modules", "dist", ".astro", "docs", "* 2.*", "* 3.*"))
    (w / "node_modules").symlink_to(SRC / "node_modules")

    sub(w / "astro.config.mjs", r"site: process\.env\.SITE_URL \|\| '[^']*',",
        f"site: 'https://pduclos.github.io',\n  base: '{BASE}',", regex=True)
    routes = w / "src/i18n/routes.ts"
    routes.write_text(re.sub(r"(fr|en): '(/[^']*)'",
                             lambda m: f"{m.group(1)}: '{BASE}{'' if m.group(2) == '/' else m.group(2)}'",
                             routes.read_text(encoding="utf-8")), encoding="utf-8")
    sub(w / "src/config.ts", "file: '/photos/", f"file: '{BASE}/photos/")
    sub(w / "src/components/Photo.astro", "path.join(process.cwd(), 'public', p.file)",
        f"path.join(process.cwd(), 'public', p.file.replace(/^\\{BASE}/, ''))")
    sub(w / "src/layouts/Base.astro", 'href="/favicon.svg"', f'href="{BASE}/favicon.svg"')
    sub(w / "src/layouts/Base.astro", 'href="/sitemap.xml"', f'href="{BASE}/sitemap.xml"')
    sub(w / "src/pages/404.astro", 'href="/favicon.svg"', f'href="{BASE}/favicon.svg"')
    sub(w / "src/views/APropos.astro", r'(?s)\s*<aside class="validate".*?</aside>', "", regex=True)
    sub(w / "src/i18n/fr/faq.ts", "adhésifs, films, chimie", "industriel")
    sub(w / "src/i18n/en/faq.ts", "adhesives, films, chemicals", "industrial")

    subprocess.run(["npx", "astro", "build"], cwd=w, check=True, capture_output=True)
    dist = w / "dist"
    bad = []
    for f in dist.rglob("*"):
        if f.is_file() and f.suffix in (".html", ".css", ".js", ".xml"):
            for m in re.finditer(r'''(?:href|src|action)=["'](/(?!buyvera)[^"']*)|url\((/(?!buyvera)[^)]*)\)''',
                                 f.read_text(errors="ignore")):
                bad.append((f.name, m.group(0)[:60]))
    assert not bad, bad[:10]
    out = SITE / "buyvera"
    shutil.rmtree(out, ignore_errors=True)
    shutil.copytree(dist, out)
    print("site Buyvera ->", out, sum(1 for _ in out.rglob("*.html")), "pages")
