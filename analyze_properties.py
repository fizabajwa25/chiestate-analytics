
import pandas as pd

df = pd.read_csv(
    "data/combined_sales.csv",
    dtype={"pin": "string"}
)

# Keep records with a known property type
residential = df[
    df["char_use"].isin(["Single-Family", "Multi-Family"])
].copy()

print("Total combined sales:", len(df))
print("Residential sales with property details:", len(residential))

print("\nProperty types:")
print(residential["char_use"].value_counts())

print("\nMedian sale price by property type:")
print(
    residential.groupby("char_use")["sale_price"]
    .median()
    .map(lambda value: f"${value:,.0f}")
)

print("\nAverage building size by property type:")
print(
    residential.groupby("char_use")["char_bldg_sf"]
    .mean()
    .round(0)
)

print("\nNumber of sales by property class:")
print(residential["class"].value_counts().head(10))
