"""Redirections /buyvera/ -> https://buyvera.fr (depuis le 10/10/2026).

Le site commercial Buyvera est publié sur son propre domaine, buyvera.fr ; la copie qui était servie
sous /buyvera/ est remplacée par une page de redirection par adresse (même chemin sur buyvera.fr,
« noindex » + canonical vers buyvera.fr) pour ne pas laisser deux sites identiques indexés.
/pondera/ (ancien nom) redirige aussi directement vers buyvera.fr.

Usage : python3 build/buyvera.py
"""
import shutil
from pathlib import Path

SITE = Path(__file__).resolve().parent.parent
CIBLE = "https://buyvera.fr"
PAGES = [
    "", "plateforme/integration", "plateforme/remises-et-prix", "plateforme/pilotage", "plateforme/assistant-local",
    "groupes", "architecture", "securite", "demo", "ressources/faq", "ressources/glossaire",
    "ressources/feuille-de-route", "a-propos", "mentions-legales", "confidentialite", "cookies",
    "en", "en/platform/integration", "en/platform/discounts-and-prices", "en/platform/management",
    "en/platform/local-assistant", "en/groups", "en/architecture", "en/security", "en/demo", "en/resources/faq",
    "en/resources/glossary", "en/resources/roadmap", "en/about", "en/legal-notice", "en/privacy", "en/cookies",
]


def page(url: str, lang: str) -> str:
    msg = (f'Le site Buyvera est désormais sur <a href="{url}">buyvera.fr</a>.' if lang == "fr"
           else f'The Buyvera website has moved to <a href="{url}">buyvera.fr</a>.')
    return (f'<!DOCTYPE html>\n<html lang="{lang}"><head><meta charset="utf-8">\n<title>Buyvera</title>\n'
            f'<meta name="robots" content="noindex">\n<link rel="canonical" href="{url}">\n'
            f'<meta http-equiv="refresh" content="0; url={url}">\n</head><body><p>{msg}</p></body></html>\n')


def main() -> None:
    dossier = SITE / "buyvera"
    if dossier.exists():
        shutil.rmtree(dossier)
    for chemin in PAGES:
        url = f"{CIBLE}/{chemin}/" if chemin else f"{CIBLE}/"
        lang = "en" if chemin == "en" or chemin.startswith("en/") else "fr"
        f = dossier / chemin / "index.html"
        f.parent.mkdir(parents=True, exist_ok=True)
        f.write_text(page(url, lang), encoding="utf-8")
    (dossier / "404.html").write_text(page(f"{CIBLE}/", "fr"), encoding="utf-8")
    (SITE / "pondera" / "index.html").write_text(page(f"{CIBLE}/", "fr"), encoding="utf-8")
    print(f"{len(PAGES)} redirections écrites sous buyvera/, plus 404 et pondera/")


if __name__ == "__main__":
    main()
