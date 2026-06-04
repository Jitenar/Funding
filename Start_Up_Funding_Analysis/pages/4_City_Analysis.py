import streamlit as st
import pandas as pd
import plotly.express as px

# Page Configuration
st.set_page_config(
    page_title="City Analysis",
    page_icon="🌍",
    layout="wide"
)

st.title("🌍 City Analysis")

# Load Data
@st.cache_data
def load_data():
    return pd.read_csv("data/startup_funding.csv")

try:
    df = load_data()

    # Remove missing city values
    df = df.dropna(subset=["City"])

    st.header("Top Startup Cities")

    city_count = (
        df["City"]
        .value_counts()
        .head(10)
        .reset_index()
    )

    city_count.columns = ["City", "Startup Count"]

    fig1 = px.bar(
        city_count,
        x="City",
        y="Startup Count",
        title="Top 10 Cities by Number of Startups"
    )

    st.plotly_chart(fig1, use_container_width=True)

    st.divider()

    # Funding Analysis
    if "Amount_USD" in df.columns:

        st.header("Top Cities by Funding Amount")

        city_funding = (
            df.groupby("City")["Amount_USD"]
            .sum()
            .sort_values(ascending=False)
            .head(10)
            .reset_index()
        )

        fig2 = px.bar(
            city_funding,
            x="City",
            y="Amount_USD",
            title="Top 10 Cities by Total Funding"
        )

        st.plotly_chart(fig2, use_container_width=True)

        st.divider()

        st.header("Funding Distribution Across Cities")

        fig3 = px.pie(
            city_funding,
            names="City",
            values="Amount_USD",
            hole=0.4
        )

        st.plotly_chart(fig3, use_container_width=True)

    st.divider()

    st.header("City Summary")

    summary = (
        df.groupby("City")
        .agg(
            Startup_Count=("City", "count"),
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
