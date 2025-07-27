import json
from app.utils import normalize_text

def score_section(title, keywords):
    title = normalize_text(title)
    return sum(1 for kw in keywords if kw in title)

def rank_sections_by_persona(outline, persona_profile):
    scored = []
    for section in outline:
        title = section.get("title", "")
        score = score_section(title, persona_profile)
        scored.append((score, section))

    scored.sort(key=lambda x: x[0], reverse=True)
    return [s[1] for s in scored]