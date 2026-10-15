"""English project list: same slugs, order and structure as projects.PROJECTS."""
from achats_en import ACHATS
from projects import PROJECTS as _FR
from projects_en_a import PART_A
from projects_en_b import PART_B, STRENGTHS_EN

_by_slug = {p["slug"]: p for p in PART_A + PART_B + [ACHATS]}
PROJECTS = [_by_slug[p["slug"]] for p in _FR]
for _p in PROJECTS:
    _p["strengths"] = STRENGTHS_EN.get(_p["slug"])
