from pathlib import Path
import pandas as pd

# keep a local default URL so this module can run standalone
RAW_URL = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"

def extract_to_bronze(bronze_path: Path) -> Path:
    """Download RAW_URL and write to the bronze path, returning the written file path."""
    df = pd.read_csv(RAW_URL)
    out_path = bronze_path / "restaurant_tips_raw.csv"
    df.to_csv(out_path, index=False)
    print(f"[BRONZE]: wrote {out_path} with {len(df)} rows")
    return out_path