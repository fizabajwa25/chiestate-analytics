
import pandas as pd
from pathlib import Path

# Load downloaded property sales
df = pd.read_csv(
    "data/cook_county_sales_sample.csv",
    dtype={"pin": "string", "class": "string", "nbhd": "string"}
)

print("Original records:", len(df))

# Convert columns into usable formats
df["sale_price"] = pd.to_numeric(
    df["sale_price"], errors="coerce"
)

df["sale_date"] = pd.to_datetime(
    df["sale_date"], errors="coerce"
)

# Convert sale flags into booleans
for column in [
    "is_multisale",
    "sale_filter_less_than_10k",
    "sale_filter_deed_type",
    "sale_filter_same_sale_within_365"
]:
    df[column] = (
        df[column].astype("string").str.lower() == "true"
    )

# Remove missing and nonpositive sale prices
df = df.dropna(subset=["sale_price", "sale_date"])
df = df[df["sale_price"] > 0]

# Exclude flagged transactions
df = df[
    ~df["is_multisale"]
    & ~df["sale_filter_less_than_10k"]
    & ~df["sale_filter_deed_type"]
    & ~df["sale_filter_same_sale_within_365"]
]

# Keep useful columns
df = df[
    [
        "pin",
        "sale_date",
        "sale_price",
        "class",
        "township_code",
        "nbhd"
    ]
]

Path("data").mkdir(exist_ok=True)
df.to_csv("data/cleaned_sales.csv", index=False)

print("Cleaned records:", len(df))
print("Median sale price:", f"${df['sale_price'].median():,.0f}")
print("\nPreview:")
print(df.head())
