
import requests
import pandas as pd

# Cook County Assessor property characteristics dataset
url = "https://datacatalog.cookcountyil.gov/resource/x54s-btds.json"

params = {
    "$limit": 5
}

response = requests.get(url, params=params, timeout=30)
response.raise_for_status()

data = response.json()
df = pd.DataFrame(data)

print("Available columns:")
print(df.columns.tolist())

print("\nSample records:")
print(df.head().to_string())
