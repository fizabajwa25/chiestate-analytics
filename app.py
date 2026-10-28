
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from pathlib import Path

# ============================================================
# CHIESTATE ANALYTICS — GIRLY POP REAL ESTATE DASHBOARD
# ============================================================

st.set_page_config(
    page_title="ChiEstate | Chicago Real Estate",
    page_icon="💗",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ---------------------------
# COLOR PALETTE
# ---------------------------
PINK = "#D84C91"
HOT_PINK = "#B93579"
BLUSH = "#FBE3EF"
LAVENDER = "#B8A0E8"
PURPLE = "#8E70C4"
CREAM = "#FFF9FC"
INK = "#432B42"
MUTED = "#927C90"
GRID = "#F1E6EE"
WHITE = "#FFFFFF"

# ---------------------------
# CUSTOM CSS
# ---------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Outfit:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
}

.stApp {
    background: #FFF9FC;
    color: #432B42;
}

.block-container {
    max-width: 1240px;
    padding-top: 1.2rem;
    padding-bottom: 4rem;
}

h1, h2, h3 {
    font-family: 'Outfit', sans-serif !important;
    color: #432B42 !important;
    letter-spacing: -0.035em;
}

h1 {
    font-size: 2.65rem !important;
    font-weight: 800 !important;
}

h2 {
    font-size: 1.6rem !important;
    font-weight: 750 !important;
}

p, label {
    color: #6E586C;
}

[data-testid="stHeader"] {
    background: #FFF9FC;
}

[data-testid="stMetric"] {
    background: #FFFFFF;
    border: 1px solid #F3E3ED;
    border-radius: 18px;
    padding: 20px;
    box-shadow: 0 5px 22px rgba(142, 65, 111, 0.045);
}

[data-testid="stMetricLabel"] {
    color: #927C90;
    font-size: 0.86rem;
    font-weight: 600;
}

[data-testid="stMetricValue"] {
    color: #432B42;
    font-family: 'Outfit', sans-serif;
    font-weight: 800;
}

[data-testid="stMetricDelta"] {
    font-size: 0.8rem;
}

[data-testid="stVerticalBlockBorderWrapper"] {
    border-radius: 18px;
}

div[data-baseweb="select"] > div,
div[data-baseweb="input"] > div {
    border-radius: 12px;
    border-color: #EEDAE6;
}

.stButton > button[kind="primary"] {
    background: #D84C91;
    border: 1px solid #D84C91;
    color: white;
    border-radius: 12px;
    font-weight: 700;
}

.stButton > button[kind="primary"]:hover {
    background: #B93579;
    border-color: #B93579;
}

.stButton > button[kind="secondary"] {
    border-radius: 12px;
    border: 1px solid #EAD7E4;
    background: #FFFFFF;
    color: #432B42;
}

.stDownloadButton > button {
    background: #D84C91;
    color: white;
    border: 0;
    border-radius: 12px;
}

.stTabs [data-baseweb="tab-list"] {
    gap: 8px;
}

.stTabs [data-baseweb="tab"] {
    border-radius: 12px;
    padding: 12px 18px;
}

.stTabs [aria-selected="true"] {
    color: #B93579 !important;
}

[data-testid="stDataFrame"] {
    border-radius: 14px;
    overflow: hidden;
}

.brand-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 22px;
    gap: 15px;
}

.brand-name {
    font-family: 'Outfit', sans-serif;
    font-weight: 800;
    font-size: 1.85rem;
    letter-spacing: -0.07em;
    color: #432B42;
}

.brand-dot {
    color: #D84C91;
}

.brand-tagline {
    font-size: 0.7rem;
    font-weight: 700;
    color: #A28A9E;
    letter-spacing: 0.14em;
}

.brand-pill {
    background: #FBE3EF;
    color: #B93579;
    padding: 9px 14px;
    border-radius: 999px;
    font-size: 0.8rem;
    font-weight: 700;
    white-space: nowrap;
}

.hero {
    background: linear-gradient(115deg, #FBE3EF 0%, #F9EAF9 56%, #EDE6FF 100%);
    border: 1px solid #F4DCEB;
    border-radius: 26px;
    padding: 38px 42px;
    margin: 12px 0 28px;
}

.hero-kicker {
    color: #B93579;
    font-size: 0.76rem;
    font-weight: 800;
    letter-spacing: 0.14em;
}

.hero-title {
    color: #432B42;
    font-family: 'Outfit', sans-serif;
    font-size: clamp(2rem, 4vw, 3.2rem);
    font-weight: 800;
    letter-spacing: -0.06em;
    line-height: 1.12;
    margin: 12px 0;
}

.hero-description {
    color: #7D637B;
    font-size: 1.02rem;
    line-height: 1.7;
    max-width: 620px;
}

.section-kicker {
    color: #B93579;
    font-size: 0.75rem;
    font-weight: 800;
    letter-spacing: 0.12em;
    margin-bottom: 6px;
}

.section-description {
    color: #927C90;
    margin-top: -8px;
    margin-bottom: 20px;
}

.soft-card {
    background: #FFFFFF;
    border: 1px solid #F1E2ED;
    border-radius: 18px;
    padding: 22px;
    margin: 8px 0;
}

.soft-card-title {
    color: #432B42;
    font-family: 'Outfit', sans-serif;
    font-size: 1.2rem;
    font-weight: 700;
}

.soft-card-text {
    color: #927C90;
    font-size: 0.9rem;
    line-height: 1.6;
    margin-top: 8px;
}

.notice {
    background: #FFF0F7;
    border: 1px solid #F4D4E5;
    border-radius: 14px;
    padding: 14px 18px;
    color: #885A76;
    font-size: 0.88rem;
    line-height: 1.6;
    margin: 12px 0 22px;
}

.footer {
    color: #A18A9E;
    font-size: 0.83rem;
    text-align: center;
    margin-top: 32px;
    padding-top: 20px;
    border-top: 1px solid #F0E2EC;
}

/* Fix logo clipping */
.brand-row {
    min-height: 76px;
    padding-top: 12px;
    overflow: visible;
}

.brand-name {
    line-height: 1.5;
    padding: 2px 0;
    overflow: visible;
}

/* Fix metric card text */
[data-testid="stMetric"] {
    min-width: 0;
    padding: 18px 14px;
}

[data-testid="stMetricValue"] {
    font-size: clamp(1.2rem, 2vw, 1.8rem);
    line-height: 1.4;
    white-space: normal;
}

[data-testid="stMetricLabel"] {
    line-height: 1.4;
}

</style>
""", unsafe_allow_html=True)


# ---------------------------
# HELPER FUNCTIONS
# ---------------------------
def money(value):
    if pd.isna(value):
        return "N/A"
    return f"${value:,.0f}"



def plot_style(fig, height=390, currency_axis=True):
    fig.update_layout(
        height=height,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",

        font=dict(
            family="DM Sans",
            color="#432B42",
            size=14
        ),

        title_font=dict(
            family="Outfit",
            size=19,
            color="#432B42"
        ),

        margin=dict(l=55, r=35, t=65, b=70),

        xaxis=dict(
            showgrid=False,
            zeroline=False,
            automargin=True,
            tickfont=dict(color="#6D4968", size=13),
            title_font=dict(color="#432B42", size=14)
        ),

        yaxis=dict(
            showgrid=True,
            gridcolor="#EBDCE6",
            zeroline=False,
            automargin=True,
            tickfont=dict(color="#6D4968", size=13),
            title_font=dict(color="#432B42", size=14),
            tickprefix="$" if currency_axis else "",
            tickformat="~s" if currency_axis else None
        )
    )

    return fig



def mortgage_payment(price, down_pct, annual_rate, years):
    principal = price * (1 - down_pct / 100)
    months = years * 12
    monthly_rate = annual_rate / 100 / 12

    if principal <= 0:
        return 0.0
    if monthly_rate == 0:
        return principal / months

    factor = (1 + monthly_rate) ** months
    return principal * monthly_rate * factor / (factor - 1)


# ---------------------------
# LOAD REAL DATA
# ---------------------------
DATA_FILE = Path("data/combined_sales.csv")

if DATA_FILE.exists():
    sales = pd.read_csv(
        DATA_FILE,
        dtype={"pin": "string", "class": "string"}
    )

    sales["sale_price"] = pd.to_numeric(
        sales["sale_price"], errors="coerce"
    )
    sales["char_bldg_sf"] = pd.to_numeric(
        sales["char_bldg_sf"], errors="coerce"
    )
    sales["char_beds"] = pd.to_numeric(
        sales["char_beds"], errors="coerce"
    )
    sales["sale_date"] = pd.to_datetime(
        sales["sale_date"], errors="coerce"
    )
else:
    sales = pd.DataFrame()


# ---------------------------
# HEADER
# ---------------------------
st.markdown("""
<div class="brand-row">
    <div>
        <div class="brand-name">chiestate<span class="brand-dot">.</span> ♡</div>
        <div class="brand-tagline">CHICAGO REAL ESTATE, REIMAGINED</div>
    </div>
    <div class="brand-pill">✦ Your real estate era</div>
</div>
""", unsafe_allow_html=True)

# Navigation
page = st.segmented_control(
    "Navigation",
    [
        "🏡 Market Insights",
        "💗 Neighborhoods",
        "✨ Mortgage Studio"
    ],
    default="🏡 Market Insights",
    label_visibility="collapsed"
)

# ============================================================
# PAGE 1 — MARKET INSIGHTS
# ============================================================
if page == "🏡 Market Insights":

    st.markdown("""
    <div class="hero">
        <div class="hero-kicker">✦ THE MARKET, BUT MAKE IT CUTE</div>
        <div class="hero-title">Find your place<br>in the city. ♡</div>
        <div class="hero-description">
            Explore real property sales, compare home types,
            and make your next move with a little more confidence.
        </div>
    </div>
    """, unsafe_allow_html=True)

    if sales.empty:
        st.error(
            "Real sales data is missing. "
            "Run combine_data.py to create data/combined_sales.csv."
        )
        st.stop()

    residential = sales[
        sales["char_use"].isin(
            ["Single-Family", "Multi-Family"]
        )
    ].copy()

    st.markdown(
        '<div class="section-kicker">YOUR MARKET SNAPSHOT</div>',
        unsafe_allow_html=True
    )
    st.subheader("The numbers at a glance")

    selected_types = st.multiselect(
        "Explore property types",
        options=["Single-Family", "Multi-Family"],
        default=["Single-Family", "Multi-Family"],
        help="Only properties with matched residential characteristics are included."
    )

    filtered = residential[
        residential["char_use"].isin(selected_types)
    ].copy()

    if filtered.empty:
        st.info("Choose at least one property type to explore the data.")
        st.stop()

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "Properties Sold",
        f"{len(filtered):,}"
    )
    c2.metric(
        "Median Sale Price",
        money(filtered["sale_price"].median())
    )
    c3.metric(
        "Avg. Building Size (sq ft)",
        f"{filtered['char_bldg_sf'].mean():,.0f}"
    )
    c4.metric(
        "Property Types",
        filtered["char_use"].nunique()
    )

    st.markdown("""
    <div class="notice">
        <strong>About this data:</strong> These are real recorded sales
        from a recent Cook County-wide sample, not a complete Chicago
        market report. Property characteristics are available for a
        subset of transactions.
    </div>
    """, unsafe_allow_html=True)

    st.markdown(
        '<div class="section-kicker">PRICE EXPLORER</div>',
        unsafe_allow_html=True
    )
    st.subheader("What are homes selling for?")

    summary = (
        filtered.groupby("char_use")
        .agg(
            median_price=("sale_price", "median"),
            sales_count=("sale_price", "size"),
            avg_sqft=("char_bldg_sf", "mean")
        )
        .reset_index()
    )

    left, right = st.columns([1.5, 1], gap="large")

    with left:
        fig = px.bar(
            summary,
            x="char_use",
            y="median_price",
            color="char_use",
            color_discrete_map={
                "Single-Family": PINK,
                "Multi-Family": LAVENDER
            },
            text="median_price",
            title="Median sale price by home type",
            labels={
                "char_use": "Property type",
                "median_price": "Median sale price"
            }
        )

        fig.update_traces(
            texttemplate="$%{text:,.0f}",
            textposition="outside",
            marker_cornerradius=9
        )

                
        fig = plot_style(fig)

        fig.update_traces(
            texttemplate="$%{text:,.0f}",
            textposition="outside",
            textfont=dict(size=13, color="#432B42"),
            cliponaxis=False
        )

        fig.update_layout(
            yaxis=dict(
                range=[0, summary["median_price"].max() * 1.25],
                tickprefix="$",
                tickformat="~s",
                gridcolor="#F1E6EE"
            ),
            margin=dict(l=30, r=35, t=75, b=65)
        )

        st.plotly_chart(fig, width="stretch")


    with right:
        donut = px.pie(
            summary,
            names="char_use",
            values="sales_count",
            hole=0.7,
            color="char_use",
            color_discrete_map={
                "Single-Family": PINK,
                "Multi-Family": LAVENDER
            },
            title="Sales by property type"
        )

        
        donut.update_layout(
            height=430,
            paper_bgcolor="rgba(0,0,0,0)",
            font=dict(
                family="DM Sans",
                color="#432B42",
                size=12
            ),
            title_font=dict(
                family="Outfit",
                size=18,
                color="#432B42"
            ),
            margin=dict(l=15, r=15, t=70, b=85),
            legend=dict(
                orientation="h",
                y=-0.12,
                x=0.5,
                xanchor="center",
                font=dict(size=11, color="#432B42")
            )
        )


        st.plotly_chart(donut, width="stretch")

    st.markdown(
        '<div class="section-kicker">DEEPER INSIGHTS</div>',
        unsafe_allow_html=True
    )
    st.subheader("Explore the details")

    chart_tab, data_tab = st.tabs(
        ["💗 Price distribution", "📋 Property records"]
    )

    with chart_tab:
        histogram = px.histogram(
            filtered,
            x="sale_price",
            color="char_use",
            nbins=30,
            barmode="overlay",
            color_discrete_map={
                "Single-Family": PINK,
                "Multi-Family": LAVENDER
            },
            title="Distribution of recorded sale prices",
            labels={
                "sale_price": "Sale price",
                "count": "Sales",
                "char_use": "Property type"
            }
        )

        histogram.update_traces(opacity=0.8)
        
        histogram.update_layout(
            height=430,

            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",

            font=dict(
                family="DM Sans",
                color="#432B42",
                size=14
            ),

            title_font=dict(
                family="Outfit",
                size=19,
                color="#432B42"
            ),

            margin=dict(
                l=65,
                r=30,
                t=70,
                b=100
            ),

            showlegend=True,

            xaxis=dict(
                title="Sale Price",
                tickprefix="$",
                tickformat="~s",
                tickfont=dict(
                    color="#6D4968",
                    size=13
                ),
                title_font=dict(
                    color="#432B42",
                    size=14
                ),
                gridcolor="#EBDCE6",
                automargin=True
            ),

            yaxis=dict(
                title="Number of Sales",
                tickfont=dict(
                    color="#6D4968",
                    size=13
                ),
                title_font=dict(
                    color="#432B42",
                    size=14
                ),
                gridcolor="#EBDCE6",
                automargin=True
            ),

            legend=dict(
                orientation="h",
                y=-0.28,
                x=0,
                font=dict(
                    color="#432B42",
                    size=13
                ),
                title=dict(
                    text="Property Type",
                    font=dict(color="#432B42", size=13)
                )
            )
        )


        st.plotly_chart(histogram, width="stretch")

    with data_tab:
        columns = [
            "sale_date",
            "sale_price",
            "char_use",
            "char_beds",
            "char_bldg_sf",
            "char_yrblt"
        ]

        display = filtered[columns].copy()
        display.columns = [
            "Sale Date",
            "Sale Price",
            "Property Type",
            "Bedrooms",
            "Building Sq Ft",
            "Year Built"
        ]

        st.dataframe(
            display,
            width="stretch",
            hide_index=True,
            column_config={
                "Sale Price": st.column_config.NumberColumn(
                    format="$%.0f"
                ),
                "Building Sq Ft": st.column_config.NumberColumn(
                    format="%.0f"
                ),
                "Sale Date": st.column_config.DateColumn(
                    format="MMM DD, YYYY"
                )
            }
        )

        st.download_button(
            "♡ Download property data",
            data=display.to_csv(index=False),
            file_name="chiestate_property_sales.csv",
            mime="text/csv",
            type="primary"
        )

    min_date = filtered["sale_date"].min()
    max_date = filtered["sale_date"].max()

    if pd.notna(min_date) and pd.notna(max_date):
        st.caption(
            f"Source: Cook County Assessor | "
            f"Sales dated {min_date:%B %d, %Y} "
            f"through {max_date:%B %d, %Y}."
        )


# ============================================================
# PAGE 2 — NEIGHBORHOOD EXPLORER
# ============================================================

elif page == "💗 Neighborhoods":

    st.markdown("""
    <div class="hero">
        <div class="hero-kicker">✦ EXPLORE CHICAGO</div>
        <div class="hero-title">Find your neighborhood<br>crush. ♡</div>
        <div class="hero-description">
            Explore real recorded residential sales across
            Chicago's community areas.
        </div>
    </div>
    """, unsafe_allow_html=True)

    chicago_file = Path("data/chicago_sales.csv")

    if not chicago_file.exists():
        st.error("Run analyze_chicago.py first.")
        st.stop()

    chicago = pd.read_csv(chicago_file)

    chicago["sale_price"] = pd.to_numeric(
        chicago["sale_price"], errors="coerce"
    )
    chicago["lat"] = pd.to_numeric(
        chicago["lat"], errors="coerce"
    )
    chicago["lon"] = pd.to_numeric(
        chicago["lon"], errors="coerce"
    )

    chicago = chicago.dropna(
        subset=["sale_price", "chicago_community_area_name"]
    )

    st.markdown(
        '<div class="section-kicker">NEIGHBORHOOD EXPLORER</div>',
        unsafe_allow_html=True
    )
    st.subheader("Explore Chicago's community areas")

    property_types = st.multiselect(
        "Property type",
        ["Single-Family", "Multi-Family"],
        default=["Single-Family", "Multi-Family"]
    )

    min_sales = st.slider(
        "Minimum recorded sales per community area",
        min_value=1,
        max_value=10,
        value=3,
        help="Higher minimums exclude areas with very few sales."
    )

    filtered = chicago[
        chicago["char_use"].isin(property_types)
    ].copy()

    if filtered.empty:
        st.info("Select at least one property type.")
        st.stop()

    summary = (
        filtered.groupby("chicago_community_area_name")
        .agg(
            sales_count=("sale_price", "size"),
            median_price=("sale_price", "median"),
            average_price=("sale_price", "mean")
        )
        .reset_index()
    )

    eligible = summary[
        summary["sales_count"] >= min_sales
    ].copy()

    c1, c2, c3 = st.columns(3)

    c1.metric("Chicago Sales", f"{len(filtered):,}")
    c2.metric(
        "Median Recorded Sale",
        money(filtered["sale_price"].median())
    )
    c3.metric(
        "Community Areas",
        filtered["chicago_community_area_name"].nunique()
    )

    st.markdown("""
    <div class="notice">
        <strong>About these results:</strong>
        Prices reflect a small, recent sample of recorded
        Chicago residential sales, not typical home values
        or comprehensive neighborhood market estimates.
        Community-area rankings can be especially unstable
        when sales counts are low.
    </div>
    """, unsafe_allow_html=True)

    st.subheader("Compare community area prices")

    if eligible.empty:
        st.warning(
            "No community areas meet this minimum sales count. "
            "Try lowering the slider."
        )
    else:
        top_areas = (
            eligible.sort_values(
                "median_price", ascending=False
            )
            .head(15)
            .sort_values("median_price")
        )

        fig = px.bar(
            top_areas,
            x="median_price",
            y="chicago_community_area_name",
            orientation="h",
            color_discrete_sequence=[PINK],
            hover_data=["sales_count"],
            title="Median recorded sale price by community area",
            labels={
                "median_price": "Median sale price",
                "chicago_community_area_name": "Community area",
                "sales_count": "Recorded sales"
            }
        )

        fig.update_layout(
            height=550,
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            font=dict(
                family="DM Sans",
                color="#432B42",
                size=13
            ),
            title_font=dict(
                family="Outfit",
                color="#432B42",
                size=18
            ),
            margin=dict(l=30, r=35, t=65, b=45),
            xaxis=dict(
                tickprefix="$",
                tickformat="~s",
                gridcolor="#EBDCE6"
            ),
            yaxis=dict(
                title=None,
                tickfont=dict(color="#432B42", size=13),
                automargin=True
            )
        )

        st.plotly_chart(fig, width="stretch")

    st.subheader("Map of recorded Chicago sales")

    mapped = filtered.dropna(subset=["lat", "lon"])

    if not mapped.empty:
        map_fig = px.scatter_map(
            mapped,
            lat="lat",
            lon="lon",
            color="char_use",
            color_discrete_map={
                "Single-Family": PINK,
                "Multi-Family": LAVENDER
            },
            hover_name="chicago_community_area_name",
            hover_data={
                "sale_price": ":$,.0f",
                "char_use": True,
                "lat": False,
                "lon": False
            },
            zoom=9.5,
            height=520,
            title="Where properties sold"
        )

        map_fig.update_traces(marker=dict(size=10))
        map_fig.update_layout(
            map_style="carto-positron",
            font=dict(color="#432B42"),
            margin=dict(l=0, r=0, t=50, b=0),
            legend_title_text="Property Type"
        )

        st.plotly_chart(map_fig, width="stretch")

    st.subheader("Community area comparison")

    table = summary.sort_values(
        "sales_count", ascending=False
    ).copy()

    table.columns = [
        "Community Area",
        "Recorded Sales",
        "Median Sale Price",
        "Average Sale Price"
    ]

    st.dataframe(
        table,
        width="stretch",
        hide_index=True,
        column_config={
            "Median Sale Price": st.column_config.NumberColumn(
                format="$%.0f"
            ),
            "Average Sale Price": st.column_config.NumberColumn(
                format="$%.0f"
            )
        }
    )

    st.download_button(
        "♡ Download Chicago sales data",
        data=filtered.to_csv(index=False),
        file_name="chiestate_chicago_sales.csv",
        mime="text/csv",
        type="primary"
    )


# ============================================================
# PAGE 3 — MORTGAGE STUDIO
# ============================================================
elif page == "✨ Mortgage Studio":

    st.markdown("""
    <div class="hero">
        <div class="hero-kicker">✦ DREAM HOME MATH</div>
        <div class="hero-title">Big dreams.<br>Smart money moves. ✨</div>
        <div class="hero-description">
            Your dream home deserves a realistic budget.
            Explore monthly payments before making your move.
        </div>
    </div>
    """, unsafe_allow_html=True)

    left, right = st.columns([1.1, 1], gap="large")

    with left:
        st.markdown(
            '<div class="section-kicker">CUSTOMIZE YOUR LOAN</div>',
            unsafe_allow_html=True
        )
        st.subheader("Let's crunch the numbers")

        price = st.number_input(
            "Home price ($)",
            min_value=0,
            value=350000,
            step=10000
        )

        down = st.slider(
            "Down payment (%)",
            min_value=0,
            max_value=100,
            value=20
        )

        interest = st.number_input(
            "Annual interest rate (%)",
            min_value=0.0,
            value=6.5,
            step=0.1
        )

        years = st.selectbox(
            "Loan term",
            [15, 20, 30],
            index=2,
            format_func=lambda x: f"{x} years"
        )

    with right:
        payment = mortgage_payment(
            price, down, interest, years
        )

        down_amount = price * down / 100
        loan_amount = price - down_amount

        st.markdown(
            '<div class="section-kicker">YOUR MONTHLY ESTIMATE</div>',
            unsafe_allow_html=True
        )
        st.subheader("The payment breakdown")

        st.metric(
            "Monthly Principal & Interest",
            f"${payment:,.2f}"
        )

        a, b = st.columns(2)

        a.metric(
            "Down Payment",
            money(down_amount)
        )
        b.metric(
            "Loan Amount",
            money(loan_amount)
        )

        st.markdown("""
        <div class="notice">
            ♡ This estimate includes principal and interest only.
            Property taxes, homeowners insurance, HOA fees, PMI,
            and maintenance are not included.
        </div>
        """, unsafe_allow_html=True)

    st.write("")
    st.markdown(
        '<div class="section-kicker">SEE THE BIG PICTURE</div>',
        unsafe_allow_html=True
    )
    st.subheader("Your purchase at a glance")

    if price > 0:
        breakdown = pd.DataFrame({
            "Category": [
                "Down Payment",
                "Loan Amount"
            ],
            "Amount": [
                down_amount,
                loan_amount
            ]
        })

        donut = px.pie(
            breakdown,
            names="Category",
            values="Amount",
            hole=0.72,
            color="Category",
            color_discrete_map={
                "Down Payment": PINK,
                "Loan Amount": LAVENDER
            }
        )

        donut.update_layout(
            height=360,
            paper_bgcolor="rgba(0,0,0,0)",
            font=dict(
                family="DM Sans",
                color=INK
            ),
            margin=dict(l=10, r=10, t=15, b=10),
            legend=dict(
                orientation="h",
                y=-0.1,
                x=0.5,
                xanchor="center"
            )
        )

        st.plotly_chart(donut, width="stretch")

    st.caption(
        "For educational planning only. "
        "This is not a quote or loan approval."
    )


# ---------------------------
# FOOTER
# ---------------------------
st.markdown("""
<div class="footer">
    Made with ♡ in Chicago<br>
    ChiEstate Analytics · Python · Pandas · Plotly · Streamlit<br>
    Recorded sales source: Cook County Assessor
</div>
""", unsafe_allow_html=True)

