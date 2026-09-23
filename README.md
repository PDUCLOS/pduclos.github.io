# Portfolio — Patrice Duclos, Data Analyst Senior · Data Scientist · MLOps

Portfolio personnel : 20 ans d'expertise en distribution industrielle et une reconversion data certifiée
(Jedha RNCP niveau 6, niveau 7 Lead Data Science / AI Architect en cours).

## Site live

[https://pduclos.github.io](https://pduclos.github.io)

## Contenu

| Page | Public | Contenu |
|---|---|---|
| `/` | Tous | Accueil, parcours, projets phares, compétences, contact |
| `/profil-rh.html` | Recruteurs, managers | Proposition de valeur, impact chiffré, objections fréquentes |
| `/profil-tech.html` | Équipes data / tech | Compétences reliées aux preuves dans le code, décisions d'ingénierie |
| `/stack.html` | Tech | Outils et langages par étape du cycle MLOps, niveau et projets associés |
| `/projets/` | Tous | Index des projets + matrice de maturité MLOps |
| `/projets/<slug>.html` | Tous | Une page par projet : problème, argumentaire RH / tech, pipeline draw.io, stack, maturité MLOps, métriques, code, limites |

Les schémas sont dans `diagrams/` au format `.drawio` (source éditable) et `.svg` (affichage).

## Génération

Les pages projets, les pages d'audience, les diagrammes et le menu sont générés par `build/` :

| Fichier | Rôle |
|---|---|
| `build/projects.py` | Contenu de chaque projet (texte, pipeline, stack, métriques) |
| `build/drawio.py` | Génère les `.drawio` et les exporte en SVG via draw.io desktop |
| `build/pages.py` | Gabarit d'une page projet |
| `build/render.py` | En-tête, navigation, pied de page communs |
| `build/build.py` | Point d'entrée ; réexporte aussi les schémas d'origine des dépôts en masquant les données sensibles |

```bash
python3 build/build.py                 # tout régénérer (nécessite draw.io desktop et les dépôts clonés dans ../repos)
python3 build/build.py --no-diagrams   # pages seulement
```

Les règles de masquage sont lues depuis `build/redact.local` (non versionné).
`index.html` est édité à la main, sauf le menu et les tuiles projets, remplacés entre les marqueurs `NAV` et `TILES`.

## Stack technique

HTML5, CSS3 (`assets/style.css`), JavaScript vanilla (`assets/site.js`), Google Fonts. Aucun framework.
Générateur en Python standard + draw.io CLI.
