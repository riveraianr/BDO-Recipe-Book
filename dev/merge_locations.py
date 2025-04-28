
import pandas as pd
import json
import os

# Dynamically locate the project root
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INGREDIENT_JSON_PATH = os.path.join(BASE_DIR, "data", "ingredients.json")
LOCATION_XLSX_PATH = os.path.join(BASE_DIR, "dev", "raw_xlsx", "BDO Ingredient Locations.xlsx")

def normalize(name):
    return str(name).strip().lower() if name else ""

def load_location_data():
    df = pd.read_excel(LOCATION_XLSX_PATH)
    df.columns = [c.strip() for c in df.columns]
    return {
        normalize(row["Name"]): {
            "Source": row["Source"],
            "Location Details": row["Location Details"]
        }
        for _, row in df.iterrows()
        if pd.notna(row["Name"])
    }

def merge_ingredient_locations():
    if not os.path.exists(INGREDIENT_JSON_PATH):
        print(f"[ERROR] Missing file: {INGREDIENT_JSON_PATH}")
        return

    with open(INGREDIENT_JSON_PATH, "r", encoding="utf-8") as f:
        ingredients = json.load(f)

    locations = load_location_data()
    updated = 0
    unmatched = []
    missing_name = []

    for entry in ingredients:
        name_raw = entry.get("Ingredient Name")
        if not name_raw:
            missing_name.append(entry)
            continue

        name = normalize(name_raw)
        if name in locations:
            entry["Source"] = locations[name]["Source"]
            entry["Location Details"] = locations[name]["Location Details"]
            updated += 1
        else:
            unmatched.append(name_raw)

    with open(INGREDIENT_JSON_PATH, "w", encoding="utf-8") as f:
        json.dump(ingredients, f, indent=2, ensure_ascii=False)

    print(f"[SUCCESS] Enhanced {updated} ingredients with location data.")
    print(f"[INFO] {len(unmatched)} unmatched ingredient names:")
    for missing in unmatched[:10]:
        print(f"  - {missing}")
    if len(unmatched) > 10:
        print("  ... (truncated)")

    print(f"[INFO] {len(missing_name)} entries missing an 'Ingredient Name' field.")
    if missing_name:
        print("  Example missing entry:", missing_name[0])

if __name__ == "__main__":
    merge_ingredient_locations()
