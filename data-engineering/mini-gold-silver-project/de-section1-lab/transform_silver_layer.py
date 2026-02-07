from pathlib import Path
import numpy as np
import pandas as pd


def transform_to_silver(bronze_path: Path, SILVER: Path) -> Path:
    df = pd.read_csv(bronze_path)

    # standardize columns
    # replace spaces with underscores
    df.columns = [c.strip().lower().replace(" ", "_") for c in df.columns]

    # derived columns
    df["tip_pct"] = (df["tip"] / df["total_bill"]).round(4)

    # simple synthetic timestamp for demo (hourly sequence)
    # use lowercase 'h' for hourly frequency to be compatible across pandas versions
    df["visit_datetime"] = pd.date_range("2024-01-01", periods=len(df), freq="h")

    # basic type tweaks
    cat_cols = ["sex", "smoker", "day", "time"]
    for c in cat_cols:
        if c in df.columns:
            df[c] = df[c].astype("category")

    SILVER.mkdir(parents=True, exist_ok=True)
    out_path = SILVER / "restaurant_tips_clean.parquet"
    df.to_parquet(out_path, index=False)  # needs pyarrow
    print(f"[SILVER]: wrote {out_path} with {len(df)} rows")
    return out_path