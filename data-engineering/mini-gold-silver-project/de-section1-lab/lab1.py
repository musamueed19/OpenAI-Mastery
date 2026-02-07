from pathlib import Path
import pandas as pd

RAW_URL = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"

BRONZE = Path("data/bronze")
SILVER = Path("data/silver")
GOLD = Path("data/gold")

for p in [BRONZE, SILVER, GOLD]:
    print(f"Creating directory: {p}")
    p.mkdir(parents=True, exist_ok=True)
  
def extract_to_bronze():  
    df = pd.read_csv(RAW_URL)
    print(df.head())
    
extract_to_bronze()