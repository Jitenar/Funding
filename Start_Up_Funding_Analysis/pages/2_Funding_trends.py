import streamlit as st
import pandas as pd
import plotly.express as px

# Page Configuration
st.set_page_config(
    page_title="Funding Trends",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Funding Trends Analysis")

# Load Data
@st.cache_data
def load_data():
    return pd.read_csv("data/startup_funding.csv")

try:
    df = load_data()

    # Convert date column
    df["Funding_Date"] = pd.to_datetime(
        df["Funding_Date"],
        errors="coerce"
    )

    # Remove invalid dates
    df = df.dropna(subset=["Funding_Date"])

    # Create Year and Month columns
    df["Year"] = df["Funding_Date"].dt.year
    df["Month"] = df["Funding_Date"].dt.strftime("%b")

    st.header("Funding Records Over Time")

    yearly_deals = (
        df.groupby("Year")
        .size()
        .reset_index(name="Number of Deals")
    )

    fig = px.line(
        yearly_deals,
        x="Year",
        y="Number of Deals",
        markers=True,
        title="Number of Funding Deals Per Year"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.divider()

    # Funding Amount Trend
    st.header("Total Funding Amount by Year")

    yearly_funding = (
        df.groupby("Year")["Amount_USD"]
        .sum()
        .reset_index()
    )

    fig2 = px.bar(
        yearly_funding,
        x="Year",
        y="Amount_USD",
        title="Total Funding Amount by Year"
    )

    st.plotly_chart(fig2, use_container_width=True)

    st.divider()

    # Monthly Analysis
    st.header("Monthly Funding Activity")

    monthly_deals = (
        df.groupby("Month")
        .size()
        .reset_index(name="Deals")
    )

    month_order = [
        "Jan", "Feb", "Mar", "Apr",
        "May", "Jun", "Jul", "Aug",
        "Sep", "Oct", "Nov", "Dec"
    ]

    monthly_deals["Month"] = pd.Categorical(
        monthly_deals["Month"],
        categories=month_order,
        ordered=True
    )

    monthly_deals = monthly_deals.sort_values("Month")

    fig3 = px.bar(
        monthly_deals,
        x="Month",
        y="Deals",
        title="Monthly Funding Deals"
    )

    st.plotly_chart(fig3, use_container_width=True)

    st.divider()

    # Funding Trend Table
    st.header("Funding Summary")

    st.dataframe(
        yearly_funding.sort_values(
            "Amount_USD",
            ascending=False
        ),
        use_container_width=True
    )

except FileNotFoundError:
    st.error(
        "Dataset not found. Please place startup_funding.csv inside the data folder."
    )

except Exception as e:
    st.error(f"Error: {e}")
