"""English project list: same slugs, order and structure as projects.PROJECTS."""
from achats_en import ACHATS
from copilote_erp_en import COPILOTE_ERP_EN
from visiontrack_en import VISIONTRACK_EN
from projects import PROJECTS as _FR
from projects import _vitrine
from projects_en_a import PART_A
from projects_en_b import PART_B, STRENGTHS_EN

_by_slug = {p["slug"]: p for p in PART_A + PART_B + [ACHATS, COPILOTE_ERP_EN, VISIONTRACK_EN]}
PROJECTS = [_by_slug[p["slug"]] for p in _FR]
for _p in PROJECTS:
    _p["strengths"] = STRENGTHS_EN.get(_p["slug"]) or _p.get("strengths")
for _p in PROJECTS:
    _p.update(_vitrine(_p["slug"], "EN"))
