
import pandas as pd
import os
import json

RAW_DIR = "dev/raw_xlsx"
OUT_DIR = "data"

file_map = {
    "BDO Cooking Recipes.xlsx": "cooking.json",
    "BDO Alchemy Recipes.xlsx": "alchemy.json",
    "BDO Processing Recipes.xlsx": "processing.json",
    "BDO Imperial Box Recipes.xlsx": "imperial_boxes.json",
    "BDO Ingredient List.xlsx": "ingredients.json"
}

def clean_columns(df):
    df.columns = [str(col).strip() for col in df.columns]
    return df

def convert_excel_to_json(file_name, output_name):
    input_path = os.path.join(RAW_DIR, file_name)
    output_path = os.path.join(OUT_DIR, output_name)
    
    try:
        df = pd.read_excel(input_path)
        df = clean_columns(df)
        records = df.fillna("").to_dict(orient="records")

        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(records, f, indent=2, ensure_ascii=False)

        print(f"[SUCCESS] Converted {file_name} → {output_name} ({len(records)} records)")

    except Exception as e:
        print(f"[ERROR] Failed to convert {file_name}: {e}")

def run_conversion_pipeline():
    for excel_file, json_file in file_map.items():
        convert_excel_to_json(excel_file, json_file)

if __name__ == "__main__":
    run_conversion_pipeline()
