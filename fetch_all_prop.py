
import requests
import pandas as pd
from pathlib import Path

sales = pd.read_csv(
    "data/cleaned_sales.csv",
    dtype={"pin": "string"}
)

pins = sales["pin"].dropna().unique().tolist()

url = "https://datacatalog.cookcountyil.gov/resource/x54s-btds.json"

all_records = []
batch_size = 25

for start in range(0, len(pins), batch_size):
    batch = pins[start:start + batch_size]

    # Query multiple property PINs in one request
    quoted_pins = ",".join(f"'{pin}'" for pin in batch)

    params = {
        "$where": f"pin IN ({quoted_pins})",
        "$order": "year DESC",
        "$limit": 5000
    }

    response = requests.get(url, params=params, timeout=60)
    response.raise_for_status()

    records = response.json()
    all_records.extend(records)

    print(
        f"Processed {min(start + batch_size, len(pins))}"
        f" / {len(pins)} PINs"
    )

properties = pd.DataFrame(all_records)

if properties.empty:
    raise ValueError("No property characteristics found.")

# Keep the latest record per PIN
properties["year"] = pd.to_numeric(
    properties["year"], errors="coerce"
)

properties = (
    properties
    .sort_values("year", ascending=False)
    .drop_duplicates(subset="pin")
)

columns = [
    "pin",
    "year",
    "char_use",
    "char_beds",
    "char_bldg_sf",
    "char_yrblt"
]

properties = properties[
    [col for col in columns if col in properties.columns]
]

Path("data").mkdir(exist_ok=True)

properties.to_csv(
    "data/matched_properties.csv",
    index=False
)

print("\nUnique sales PINs:", len(pins))
print("Properties matched:", len(properties))
print("Properties unmatched:", len(pins) - len(properties))
print("\nSaved to data/matched_properties.csv")
