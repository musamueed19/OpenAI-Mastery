from pathlib import Path
from extract_bronze_layer import extract_to_bronze
from transform_silver_layer import transform_to_silver

RAW_URL = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"

BRONZE = Path("data/bronze")
SILVER = Path("data/silver")
GOLD = Path("data/gold")

for p in [BRONZE, SILVER, GOLD]:
    print(f"Creating directory: {p}")
    p.mkdir(parents=True, exist_ok=True)


if __name__ == "__main__":
    # extract raw CSV into the bronze layer
    p = extract_to_bronze(BRONZE)
    # transform bronze -> silver
    transform_to_silver(bronze_path=p, SILVER=SILVER)