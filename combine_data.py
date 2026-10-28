
import pandas as pd
from pathlib import Path

# Load cleaned property sales
sales = pd.read_csv(
    "data/cleaned_sales.csv",
    dtype={"pin": "string"}
)

# Load matched property characteristics
properties = pd.read_csv(
    "data/matched_properties.csv",
    dtype={"pin": "string"}
)

# Convert assessment year to numeric
properties["year"] = pd.to_numeric(
    properties["year"], errors="coerce"
)

# Keep the newest property record for each PIN
properties = (
    properties
    .sort_values("year", ascending=False)
    .drop_duplicates(subset="pin")
)

# Select the property characteristics we need
properties = properties[
    [
        "pin",
        "char_use",
        "char_beds",
        "char_bldg_sf",
        "char_yrblt"
    ]
]

# Join sales with property characteristics
combined = sales.merge(
    properties,
    on="pin",
    how="left",
    validate="many_to_one"
)

# Save the combined data
Path("data").mkdir(exist_ok=True)

combined.to_csv(
    "data/combined_sales.csv",
    index=False
)

print("Total sales:", len(sales))
print("Combined records:", len(combined))
print(
    "Sales with property details:",
    combined["char_use"].notna().sum()
)

print("\nPreview:")
print(combined.head(10).to_string(index=False))

print("\nSaved to data/combined_sales.csv")
