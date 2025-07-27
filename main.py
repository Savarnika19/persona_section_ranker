import json
import os
from app.ranker import rank_sections_by_persona
from app.utils import load_outline, save_ranked_sections

INPUT_PATH = "input/outline.json"
OUTPUT_PATH = "output/ranked_sections.json"
PROFILE_PATH = "app/persona_profiles.json"

# Load data
outline = load_outline(INPUT_PATH)

if not outline:
    print("No valid outline provided.")
    exit()

with open(PROFILE_PATH, "r") as pfile:
    profiles = json.load(pfile)

persona = os.environ.get("PERSONA", "student")
profile_keywords = profiles.get(persona, [])

if not profile_keywords:
    print(f"Unknown persona '{persona}'. Using empty keyword list.")

ranked_sections = rank_sections_by_persona(outline, profile_keywords)
save_ranked_sections(ranked_sections, OUTPUT_PATH)

print(f"Ranking complete for persona: {persona}")
