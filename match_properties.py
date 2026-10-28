
import requests
import pandas as pd
from pathlib import Path

sales = pd.read_csv(
    "data/cleaned_sales.csv",
    dtype={"pin": "string"}
)

# Start with 20 unique properties to test
pins = sales["pin"].dropna().unique()[:20]

url = "https://datacatalog.cookcountyil.gov/resource/x54s-btds.json"

matched = []
unmatched = []

for pin in pins:
    params = {
        "$where": f"pin='{pin}'",
        "$order": "year DESC",
        "$limit": 1
    }

    try:
        response = requests.get(url, params=params, timeout=30)
        response.raise_for_status()
        records = response.json()

        if records:
            matched.append(records[0])
        else:
            unmatched.append(pin)

    except requests.RequestException as error:
        print(f"Request failed for {pin}: {error}")
        unmatched.append(pin)

properties = pd.DataFrame(matched)

print("\nProperties searched:", len(pins))
print("Properties matched:", len(matched))
print("Properties without a match:", len(unmatched))

if matched:
    print("\nProperty types:")
    print(properties["char_use"].value_counts(dropna=False))

    print("\nMatched properties:")
    columns = [
        "pin", "year", "char_use",
        "char_beds", "char_bldg_sf"
    ]

    print(properties[columns].to_string(index=False))

    Path("data").mkdir(exist_ok=True)
    properties.to_csv(
        "data/matched_properties.csv",
        index=False
    )

    print("\nSaved to data/matched_properties.csv")
