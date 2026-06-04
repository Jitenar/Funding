import streamlit as st
import pandas as pd

# Page Configuration
st.set_page_config(
    page_title="Insights",
    page_icon="💡",
    layout="wide"
)

st.title("💡 Key Insights & Findings")

# Load Dataset
@st.cache_data
def load_data():
    return pd.read_csv("data/startup_funding.csv")

try:
    df = load_data()

    st.header("📊 Dashboard Summary")

    total_startups = len(df)

    total_funding = (
        df["Amount_USD"].sum()
        if "Amount_USD" in df.columns
        else 0
    )

    total_cities = (
        df["City"].nunique()
        if "City" in df.columns
        else 0
    )

    total_industries = (
        df["Industry_Vertical"].nunique()
        if "Industry_Vertical" in df.columns
        else 0
    )

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Startups", f"{total_startups:,}")
    col2.metric("Funding (USD)", f"${total_funding:,.0f}")
    col3.metric("Cities", total_cities)
    col4.metric("Industries", total_industries)

    st.divider()

    # Top Startup
    if "Amount_USD" in df.columns and "Startup_Name" in df.columns:

        st.header("🏆 Top Funded Startup")

        top_startup = df.loc[
            df["Amount_USD"].idxmax()
        ]

        st.success(
            f"""
            Startup: {top_startup['Startup_Name']}
            
            Funding: ${top_startup['Amount_USD']:,.0f}
            """
        )

    st.divider()

    # Top Industry
    if "Industry_Vertical" in df.columns:

        st.header("🏭 Leading Industry")

        top_industry = (
            df["Industry_Vertical"]
            .value_counts()
            .idxmax()
        )

        industry_count = (
            df["Industry_Vertical"]
            .value_counts()
            .max()
        )

        st.info(
            f"{top_industry} leads with {industry_count} startup records."
        )

    st.divider()

    # Top City
    if "City" in df.columns:

        st.header("🌍 Leading Startup Hub")

        top_city = (
            df["City"]
            .value_counts()
            .idxmax()
        )

        city_count = (
            df["City"]
            .value_counts()
            .max()
        )

        st.info(
            f"{top_city} is the leading startup hub with {city_count} startups."
        )

    st.divider()

    # Top Investor
    if "Investors_Name" in df.columns:

        st.header("💰 Most Active Investor")

        top_investor = (
            df["Investors_Name"]
            .value_counts()
            .idxmax()
        )

        investor_count = (
            df["Investors_Name"]
            .value_counts()
            .max()
        )

        st.info(
            f"{top_investor} participated in {investor_count} funding rounds."
        )

    st.divider()

    st.header("📌 Key Business Insights")

    st.markdown("""
    - Industries such as FinTech, E-commerce, EdTech, and HealthTech often attract significant funding.
    - Startup ecosystems are usually concentrated in major cities.
    - A small group of investors often participates in a large share of funding rounds.
    - Funding activity can reveal emerging sectors and market opportunities.
    - Understanding funding patterns helps entrepreneurs and investors make informed decisions.
    """)

    st.divider()

    st.header("🚀 Recommendations")

    st.markdown("""
    1. Focus on high-growth industries showing consistent investment activity.
    2. Build strong investor networks in leading startup hubs.
    3. Track emerging sectors for future opportunities.
    4. Analyze investor behavior to identify funding trends.
    5. Use data-driven insights for strategic business decisions.
    """)

except FileNotFoundError:
    st.error(
        "❌ Dataset not found. Please place startup_funding.csv inside the data folder."
    )

except Exception as e:
    st.error(f"Error: {e}")
