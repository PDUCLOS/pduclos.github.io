"""Shared page chrome (head, nav, footer) for the multi-page portfolio."""
import html
import re

from i18n import T, alt_path, home

SITE = "https://pduclos.github.io"
REPO_RAW = "https://raw.githubusercontent.com/PDUCLOS/pduclos.github.io/main"

e = lambda s: html.escape(str(s), quote=True)


def head(title, description, path, lang="fr"):
    description = re.sub(r"<[^>]+>", "", description)
    other = alt_path(path, lang)
    alts = ""
    if other:
        fr, en = (path, other) if lang == "fr" else (other, path)
        alts = (f'\n    <link rel="alternate" hreflang="fr" href="{SITE}{fr}">'
                f'\n    <link rel="alternate" hreflang="en" href="{SITE}{en}">'
                f'\n    <link rel="alternate" hreflang="x-default" href="{SITE}{fr}">')
    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{e(title)}</title>
    <meta name="description" content="{e(description)}">
    <meta name="robots" content="index, follow, noai, noimageai">
    <meta name="tdm-reservation" content="1">
    <meta name="tdm-policy" content="https://pduclos.github.io/LICENSE.txt">
    <meta name="copyright" content="© 2026 Patrice Duclos — tous droits réservés">
    <meta property="og:title" content="{e(title)}">
    <meta property="og:description" content="{e(description)}">
    <meta property="og:type" content="website">
    <meta property="og:url" content="{SITE}{path}">
    <link rel="canonical" href="{SITE}{path}">{alts}
    <meta property="og:locale" content="{"en_US" if lang == "en" else "fr_FR"}">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=DM+Serif+Display&family=Outfit:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="/assets/style.css?v=7">
</head>
<body>
"""


def nav(projects, current="", lang="fr"):
    """projects: list of dicts with slug, short, kicker. current: path of the active page."""
    t = T[lang]
    proj_root = "/en/projects/" if lang == "en" else "/projets/"
    h = home(lang)
    items = []
    for p in projects:
        href = f"{proj_root}{p['slug']}.html"
        cur = ' aria-current="page"' if current == href else ""
        items.append(f'<li><a href="{href}"{cur}>{e(p["short"])}<small>{e(p["kicker"])}</small></a></li>')
    def link(href, label, cls=""):
        cur = ' aria-current="page"' if current == href else ""
        c = f' class="{cls}"' if cls else ""
        return f'<li><a href="{href}"{c}{cur}>{label}</a></li>'
    other = alt_path(current, lang) or (home("en") if lang == "fr" else home("fr"))
    other_lang = "en" if lang == "fr" else "fr"
    switch = (f'<li><a href="{other}" class="lang-switch" hreflang="{other_lang}" lang="{other_lang}" '
              f'title="{t["switch_label"]}" aria-label="{t["switch_label"]}">{t["switch_text"]}</a></li>')
    buy = "https://buyvera.fr/en/" if lang == "en" else "https://buyvera.fr/"
    in_proj = current.startswith((proj_root, '/presentations/'))
    sk = "/en/skills.html" if lang == "en" else "/competences.html"
    st = "/en/stack.html" if lang == "en" else "/stack.html"
    rh = "/en/recruiters.html" if lang == "en" else "/profil-rh.html"
    te = "/en/tech-profile.html" if lang == "en" else "/profil-tech.html"
    return f"""    <nav>
        <a href="{h}" class="nav-logo">P<span>.</span>D</a>
        <button class="nav-toggle" aria-label="Menu">
            <span></span><span></span><span></span>
        </button>
        <ul class="nav-links">
            {link(h + '#about', t['nav_about'])}
            <li class="has-dropdown">
                <a href="{proj_root}" class="dropdown-toggle"{' aria-current="page"' if in_proj else ''}>{t['projects']}</a>
                <ul class="dropdown">
                    <li><a href="{proj_root}">{t['all_projects']}<small>{t['all_projects_sub']}</small></a></li>
                    <li class="dropdown-sep" aria-hidden="true"></li>
                    {''.join(items)}
                    <li class="dropdown-sep" aria-hidden="true"></li>
                    <li><a href="{buy}">{t['buyvera']}<small>{t['buyvera_sub']}</small></a></li>
                    <li><a href="/presentations/plateforme-tarifs.html">{t['deck_sales']}<small>{t['deck_sales_sub']}</small></a></li>
                    <li><a href="/presentations/hausses-tarifaires.html">{t['deck_tech']}<small>{t['deck_tech_sub']}</small></a></li>
                </ul>
            </li>
            {link(sk, t['nav_skills'])}
            {link(st, t['nav_stack'])}
            {link(rh, t['nav_rh'])}
            {link(te, t['nav_tech'])}
            {link(h + '#contact', t['nav_contact'], 'nav-cta')}
            {switch}
        </ul>
    </nav>
"""


def footer(lang="fr"):
    return f"""
    <footer>
        © 2026 Patrice Duclos — {T[lang]['footer']} · <a href="/LICENSE.txt" style="color:var(--text-muted)">{T[lang]['rights']}</a> ·
        <a href="https://github.com/PDUCLOS" style="color:var(--accent);text-decoration:none">GitHub</a> ·
        <a href="https://www.linkedin.com/in/patrice-duclos-04819b96" style="color:var(--accent);text-decoration:none">LinkedIn</a>
    </footer>
    <script src="/assets/site.js?v=7"></script>
</body>
</html>
"""


FOOTER = """
    <footer>
        © 2026 Patrice Duclos — Analytics Engineer — Lyon · <a href="/LICENSE.txt" style="color:var(--text-muted)">Tous droits réservés</a> ·
        <a href="https://github.com/PDUCLOS" style="color:var(--accent);text-decoration:none">GitHub</a> ·
        <a href="https://www.linkedin.com/in/patrice-duclos-04819b96" style="color:var(--accent);text-decoration:none">LinkedIn</a>
    </footer>
    <script src="/assets/site.js?v=7"></script>
</body>
</html>
"""


def badges(items):
    return "".join(f'<span class="tech-badge">{e(t)}</span>' for t in items)


def arrow():
    return '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M12 5l7 7-7 7"/></svg>'
