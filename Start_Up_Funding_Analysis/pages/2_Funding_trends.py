import streamlit as st
import pandas as pd
import plotly.express as px

from utils.data_loader import load_data
from utils.preprocessing import preprocess_data

# Page Configuration
st.set_page_config(
    page_title="Funding Trends",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Funding Trends Analysis")

try:
    # Load and preprocess data
    df = load_data()
    df = preprocess_data(df)

    if df.empty:
        st.warning("No data available.")
        st.stop()

    # Remove invalid dates
    df = df.dropna(subset=["Funding_Date"])

    # Month abbreviation for chart
    df["Month_Short"] = df["Funding_Date"].dt.strftime("%b")

    # ==========================
    # Funding Records Per Year
    # ==========================
    st.header("Funding Records Over Time")

    yearly_deals = (
        df.groupby("Year")
        .size()
        .reset_index(name="Number of Deals")
    )

    fig1 = px.line(
        yearly_deals,
        x="Year",
        y="Number of Deals",
        markers=True,
        title="Number of Funding Deals Per Year"
    )

    st.plotly_chart(fig1, use_container_width=True)

    st.divider()

    # ==========================
    # Total Funding Per Year
    # ==========================
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

    # ==========================
    # Monthly Funding Activity
    # ==========================
    st.header("Monthly Funding Activity")

    monthly_deals = (
        df.groupby("Month_Short")
        .size()
        .reset_index(name="Deals")
    )

    month_order = [
        "Jan", "Feb", "Mar", "Apr",
        "May", "Jun", "Jul", "Aug",
        "Sep", "Oct", "Nov", "Dec"
    ]

    monthly_deals["Month_Short"] = pd.Categorical(
        monthly_deals["Month_Short"],
        categories=month_order,
        ordered=True
    )

    monthly_deals = monthly_deals.sort_values("Month_Short")

    fig3 = px.bar(
        monthly_deals,
        x="Month_Short",
        y="Deals",
        title="Monthly Funding Deals"
    )

    st.plotly_chart(fig3, use_container_width=True)

    st.divider()

    # ==========================
    # Funding Summary Table
    # ==========================
    st.header("Funding Summary")

    st.dataframe(
        yearly_funding.sort_values(
            by="Amount_USD",
            ascending=False
        ),
        use_container_width=True
    )

except Exception as e:
    st.error(f"Error: {e}")
