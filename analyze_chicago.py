
import pandas as pd
from pathlib import Path

# Load sales with geographic information
df = pd.read_csv(
    "data/sales_with_locations.csv",
    dtype={"pin": "string"}
)

print("Total sales:", len(df))


# Keep Chicago properties with verified community areas
chicago = df[
    (
        df["cook_municipality_name"]
        .astype("string")
        .str.strip()
        .str.casefold()
        .eq("city of chicago")
    )
    &
    (
        df["chicago_community_area_name"].notna()
    )
].copy()


# Keep matched residential properties
chicago = chicago[
    chicago["char_use"].isin(
        ["Single-Family", "Multi-Family"]
    )
].copy()

# Clean numeric values
chicago["sale_price"] = pd.to_numeric(
    chicago["sale_price"],
    errors="coerce"
)

chicago["lat"] = pd.to_numeric(
    chicago["lat"],
    errors="coerce"
)

chicago["lon"] = pd.to_numeric(
    chicago["lon"],
    errors="coerce"
)

chicago = chicago[
    chicago["sale_price"] > 0
].copy()

# Save Chicago-only sales
Path("data").mkdir(exist_ok=True)

chicago.to_csv(
    "data/chicago_sales.csv",
    index=False
)

# Calculate community area statistics
summary = (
    chicago.groupby("chicago_community_area_name")
    .agg(
        sales_count=("sale_price", "size"),
        median_sale_price=("sale_price", "median"),
        average_sale_price=("sale_price", "mean")
    )
    .reset_index()
    .sort_values(
        "median_sale_price",
        ascending=False
    )
)

summary.to_csv(
    "data/chicago_community_summary.csv",
    index=False
)

print("\n--- CHICAGO RESULTS ---")
print("Chicago residential sales:", len(chicago))
print(
    "Community areas represented:",
    chicago["chicago_community_area_name"].nunique()
)

print("\nTop community areas by median sale price:")
print(summary.head(10).to_string(index=False))

print("\nSaved:")
print("data/chicago_sales.csv")
print("data/chicago_community_summary.csv")
