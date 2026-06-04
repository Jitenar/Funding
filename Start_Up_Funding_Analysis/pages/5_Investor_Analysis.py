import streamlit as st
import pandas as pd
import plotly.express as px

# Page Configuration
st.set_page_config(
    page_title="Investor Analysis",
    page_icon="💰",
    layout="wide"
)

st.title("💰 Investor Analysis")

# Load Dataset
@st.cache_data
def load_data():
    return pd.read_csv("data/startup_funding.csv")

try:
    df = load_data()

    # Remove missing investor names
    df = df.dropna(subset=["Investors_Name"])

    st.header("Top Active Investors")

    investor_count = (
        df["Investors_Name"]
        .value_counts()
        .head(10)
        .reset_index()
    )

    investor_count.columns = [
        "Investor",
        "Investment Count"
    ]

    fig1 = px.bar(
        investor_count,
        x="Investment Count",
        y="Investor",
        orientation="h",
        title="Top 10 Most Active Investors"
    )

    st.plotly_chart(fig1, use_container_width=True)

    st.divider()

    # Funding Contribution
    if "Amount_USD" in df.columns:

        st.header("Top Investors by Funding Amount")

        investor_funding = (
            df.groupby("Investors_Name")["Amount_USD"]
            .sum()
            .sort_values(ascending=False)
            .head(10)
            .reset_index()
        )

        fig2 = px.bar(
            investor_funding,
            x="Investors_Name",
            y="Amount_USD",
            title="Top 10 Investors by Total Funding"
        )

        st.plotly_chart(fig2, use_container_width=True)

        st.divider()

        st.header("Funding Distribution Among Investors")

        fig3 = px.pie(
            investor_funding,
            names="Investors_Name",
            values="Amount_USD",
            hole=0.4
        )

        st.plotly_chart(fig3, use_container_width=True)

    st.divider()

    st.header("Investor Summary")

    summary = (
        df.groupby("Investors_Name")
        .agg(
            Investment_Count=("Investors_Name", "count"),
            Total_Funding=("Amount_USD", "sum")
        )
        .reset_index()
        .sort_values(
            "Total_Funding",
            ascending=False
        )
    )

    st.dataframe(
        summary,
        use_container_width=True
    )

except FileNotFoundError:
    st.error(
        "❌ Dataset not found. Please place startup_funding.csv inside the data folder."
    )

except Exception as e:
    st.error(f"Error: {e}")
