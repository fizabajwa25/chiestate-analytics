
import pandas as pd

df = pd.read_csv(
    "data/cleaned_sales.csv",
    dtype={
        "pin": "string",
        "class": "string",
        "nbhd": "string",
        "township_code": "string"
    }
)

print("Total cleaned properties:", len(df))

print("\nProperty classes:")
print(df["class"].value_counts().head(20))

print("\nTownship codes:")
print(df["township_code"].value_counts().head(20))

print("\nSale date range:")
print("Earliest:", df["sale_date"].min())
print("Latest:", df["sale_date"].max())

print("\nSale price summary:")
print(df["sale_price"].describe())

print("\nParcel identifiers:")
print(df[["pin", "township_code", "nbhd", "class"]].head(10).to_string(index=False))

print("\nMissing identifiers:")
print(df[["pin", "township_code", "nbhd", "class"]].isna().sum())

print("\nUnique parcel identifiers:", df["pin"].nunique())
print("Unique assessor neighborhoods:", df["nbhd"].nunique())
