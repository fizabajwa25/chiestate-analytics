
import requests
import pandas as pd
from pathlib import Path

# Official Cook County Assessor Parcel Sales dataset
URL = "https://datacatalog.cookcountyil.gov/resource/wvhk-k5uv.json"

# Download a manageable sample of recent sales.
# This is Cook County-wide data, not yet Chicago-only.
params = {
    "$limit": 1000,
    "$order": "sale_date DESC"
}

response = requests.get(URL, params=params, timeout=30)
response.raise_for_status()

records = response.json()
df = pd.DataFrame(records)

if df.empty:
    raise ValueError("The API returned no records.")

print("Rows downloaded:", len(df))
print("\nAvailable columns:")
print(df.columns.tolist())

print("\nFirst five records:")
print(df.head().to_string())

Path("data").mkdir(exist_ok=True)
df.to_csv("data/cook_county_sales_sample.csv", index=False)

print("\nSaved to data/cook_county_sales_sample.csv")
