
import json
import os

DATA_DIR = "data"

def load_json(filename):
    path = os.path.join(DATA_DIR, filename)
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"[ERROR] File not found: {path}")
        return []
    except json.JSONDecodeError:
        print(f"[ERROR] Invalid JSON in file: {path}")
        return []

def load_cooking_data():
    return load_json("cooking.json")

def load_alchemy_data():
    return load_json("alchemy.json")

def load_processing_data():
    return load_json("processing.json")

def load_imperial_box_data():
    return load_json("imperial_boxes.json")

def load_ingredient_data():
    return load_json("ingredients.json")

if __name__ == "__main__":
    print("Testing Cooking Data:")
    cooking = load_cooking_data()
    print(f"Loaded {len(cooking)} cooking recipes")

    print("\nTesting Alchemy Data:")
    alchemy = load_alchemy_data()
    print(f"Loaded {len(alchemy)} alchemy recipes")

    print("\nTesting Ingredient Data:")
    ingredients = load_ingredient_data()
    print(f"Loaded {len(ingredients)} ingredients")
