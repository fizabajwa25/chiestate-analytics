
import requests
import pandas as pd
from pathlib import Path

# Your existing cleaned sales dataset
sales = pd.read_csv(
    "data/combined_sales.csv",
    dtype={"pin": "string"}
)

# Keep PINs as 14-character strings
sales["pin"] = sales["pin"].str.zfill(14)

pins = sales["pin"].dropna().unique().tolist()

# Official Cook County Parcel Universe dataset
url = "https://datacatalog.cookcountyil.gov/resource/pabr-t5kh.json"

all_records = []
batch_size = 25

print(f"Looking up locations for {len(pins)} properties...")

for start in range(0, len(pins), batch_size):
    batch = pins[start:start + batch_size]
    quoted = ",".join(f"'{pin}'" for pin in batch)

    params = {
        "$where": f"pin IN ({quoted})",
        "$limit": 5000
    }

    response = requests.get(
        url,
        params=params,
        timeout=60
    )
    response.raise_for_status()

    all_records.extend(response.json())

    print(
        f"Checked {min(start + batch_size, len(pins))}"
        f" of {len(pins)} PINs"
    )

locations = pd.DataFrame(all_records)

if locations.empty:
    raise ValueError("No parcel locations were returned.")

# Identify the geographic fields provided by the API
print("\nAvailable location-related columns:")
keywords = [
    "community", "municipality",
    "city", "lat", "lon", "ward"
]

for column in locations.columns:
    if any(word in column.lower() for word in keywords):
        print(" -", column)

# One location record per PIN
locations["pin"] = locations["pin"].astype("string").str.zfill(14)
locations = locations.drop_duplicates(subset="pin")

# Combine the sales and geographic information
combined = sales.merge(
    locations,
    on="pin",
    how="left",
    suffixes=("", "_location"),
    validate="many_to_one"
)

Path("data").mkdir(exist_ok=True)

combined.to_csv(
    "data/sales_with_locations.csv",
    index=False
)

print("\n--- RESULTS ---")
print("Original sales:", len(sales))
print("Combined sales:", len(combined))
print("PINs with location matches:", sales["pin"].isin(locations["pin"]).sum())

print("\nSaved to data/sales_with_locations.csv")
