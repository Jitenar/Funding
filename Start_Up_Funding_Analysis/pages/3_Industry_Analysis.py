import streamlit as st
import pandas as pd
import plotly.express as px

# Page Configuration
st.set_page_config(
    page_title="Industry Analysis",
    page_icon="🏭",
    layout="wide"
)

st.title("🏭 Industry Analysis")

# Load Data
@st.cache_data
def load_data():
    return pd.read_csv("data/startup_funding.csv")

try:
    df = load_data()

    # Remove missing industries
    df = df.dropna(subset=["Industry_Vertical"])

    st.header("Top Industries by Number of Startups")

    industry_count = (
        df["Industry_Vertical"]
        .value_counts()
        .head(10)
        .reset_index()
    )

    industry_count.columns = [
        "Industry",
        "Startup Count"
    ]

    fig1 = px.bar(
        industry_count,
        x="Startup Count",
        y="Industry",
        orientation="h",
        title="Top 10 Industries by Startup Count"
    )

    st.plotly_chart(fig1, use_container_width=True)

    st.divider()

    # Funding Distribution
    if "Amount_USD" in df.columns:

        st.header("Top Industries by Funding Amount")

        industry_funding = (
            df.groupby("Industry_Vertical")["Amount_USD"]
            .sum()
            .sort_values(ascending=False)
            .head(10)
            .reset_index()
        )

        fig2 = px.bar(
            industry_funding,
            x="Industry_Vertical",
            y="Amount_USD",
            title="Top 10 Industries by Total Funding"
        )

        st.plotly_chart(fig2, use_container_width=True)

        st.divider()

        st.header("Funding Distribution Across Industries")

        fig3 = px.pie(
            industry_funding,
            names="Industry_Vertical",
            values="Amount_USD",
            hole=0.4
        )

        st.plotly_chart(fig3, use_container_width=True)

    st.divider()

    st.header("Industry Summary")

    summary = (
        df.groupby("Industry_Vertical")
        .agg(
            Startup_Count=("Industry_Vertical", "count"),
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
        "Dataset not found. Please place startup_funding.csv inside the data folder."
    )

except Exception as e:
    st.error(f"Error: {e}")
