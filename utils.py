import json
def normalize_text(text):
    return text.lower().strip()

def load_outline(path):
    try:
        with open(path, "r") as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading outline: {e}")
        return []

def save_ranked_sections(sections, path):
    try:
        with open(path, "w") as f:
            json.dump(sections, f, indent=2)
    except Exception as e:
        print(f"Error saving ranked sections: {e}")