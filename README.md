# 🏡 ChiEstate Analytics

### Chicago Real Estate Insights, Beautifully Visualized 💗

**ChiEstate Analytics** is an interactive real estate analytics dashboard built with Python and Streamlit. It transforms publicly available Cook County property sales data into accessible, interactive insights about Chicago's housing market.

The project combines data collection, cleaning, property matching, geographic analysis, and interactive visualization into one end-to-end data analytics application.

## ✨ Features

### 📊 Market Insights
- Explore recorded Cook County residential property sales.
- Analyze median sale prices and property-type distributions.
- Visualize sale price distributions.
- Explore and download property-level data.

### 📍 Chicago Neighborhood Explorer
- Compare median recorded sale prices across Chicago community areas.
- Explore sales geographically using an interactive map.
- Filter between single-family and multi-family properties.
- Apply minimum transaction-count thresholds to improve comparisons.
- Download Chicago sales data.

### 🏦 Mortgage Studio
- Estimate monthly principal and interest payments.
- Adjust home price, down payment, interest rate, and loan term.
- Explore mortgage cost breakdowns interactively.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Data processing and application logic |
| Pandas | Data cleaning, transformation, and analysis |
| Streamlit | Interactive web dashboard |
| Plotly | Charts and geographic visualizations |
| Cook County Open Data | Public real estate data |

## 📂 Project Structure

```text
chicago-real-estate-dash/
├── app.py
├── fetch_data.py
├── clean_data.py
├── combine_data.py
├── match_chicago_locations.py
├── analyze_chicago.py
├── data/
│   ├── chicago_sales.csv
│   └── chicago_community_summary.csv
└── README.md
```

*Additional scripts support data exploration, property matching, and preparation.*

## 🔍 Data Sources and Methodology

The dashboard uses public Cook County datasets, including:

- [Cook County Assessor — Parcel Sales](https://datacatalog.cookcountyil.gov/resource/wvhk-k5uv.json)
- [Cook County Assessor — Residential Property Characteristics](https://datacatalog.cookcountyil.gov/resource/x54s-btds.json)
- [Cook County Assessor — Parcel Universe](https://datacatalog.cookcountyil.gov/resource/pabr-t5kh.json)

The data pipeline retrieves recorded sales, cleans and validates transactions, matches available residential property characteristics, and enriches records with geographic information.

Chicago-specific analysis filters properties to the City of Chicago and groups transactions by official community area.

### Important Data Limitations

The current dataset is a limited sample of recent recorded transactions, not a comprehensive representation of Chicago's housing market. Some transactions lack matching property characteristics and are excluded from residential analyses. Community-area medians based on small sample sizes should be interpreted cautiously.

## 🚀 Run Locally

Clone the repository:

```bash
git clone https://github.com/fizabajwa25/chiestate-analytics.git
cd chiestate-analytics
```

Install dependencies:

```bash
pip install streamlit pandas plotly requests
```

Launch the dashboard:

```bash
streamlit run app.py
```

The dashboard requires the prepared CSV files in the `data/` directory.

## 🎯 Project Goals

This project demonstrates practical experience in:

- Collecting and integrating data from public APIs.
- Cleaning and joining real-world datasets.
- Performing exploratory and geographic data analysis.
- Building interactive dashboards.
- Communicating findings through accessible visualizations.
- Developing an end-to-end Python analytics project.

## 👩‍💻 Author

**Fiza Bajwa**

Built as a personal data analytics portfolio project.

---

*Made with Python, curiosity, and a little pink.* 💗
