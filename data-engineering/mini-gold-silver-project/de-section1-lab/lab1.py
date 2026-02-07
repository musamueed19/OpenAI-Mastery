from pathlib import Path
from extract_bronze_layer import extract_to_bronze
from transform_silver_layer import transform_to_silver
import os

# Ensure the venv uses a valid CA bundle. If certifi is installed this will
# point SSL operations (urllib / pandas) at certifi's bundle and avoid
# macOS/python.org certificate verification errors.
try:
    import certifi
    os.environ.setdefault("SSL_CERT_FILE", certifi.where())
except Exception:
    # if certifi isn't available we'll fall back to the system settings and
    # a failing SSL will raise an explicit error during the network call.
    pass

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