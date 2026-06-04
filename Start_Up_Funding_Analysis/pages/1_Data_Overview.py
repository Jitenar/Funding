import streamlit as st
import pandas as pd

# Page Configuration
st.set_page_config(page_title="Data Overview", page_icon="📂", layout="wide")

st.title("📂 Data Overview")

# Load Dataset
@st.cache_data
def load_data():
    return pd.read_csv("data/startup_funding.csv")

try:
    df = load_data()

    # Dataset Shape
    st.header("Dataset Shape")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Rows", df.shape[0])

    with col2:
        st.metric("Columns", df.shape[1])

    st.divider()

    # Dataset Preview
    st.header("Dataset Preview")
    st.dataframe(df.head(10), use_container_width=True)

    st.divider()

    # Column Information
    st.header("Column Information")

    column_info = pd.DataFrame({
        "Column": df.columns,
        "Data Type": df.dtypes.astype(str)
    })

    st.dataframe(column_info, use_container_width=True)

    st.divider()

    # Missing Values
    st.header("Missing Values")

    missing_values = pd.DataFrame({
        "Column": df.columns,
        "Missing Values": df.isnull().sum(),
        "Percentage (%)": round((df.isnull().sum() / len(df)) * 100, 2)
    })

    st.dataframe(missing_values, use_container_width=True)

    st.divider()

    # Summary Statistics
    st.header("Summary Statistics")

    st.dataframe(
        df.describe(include="all").transpose(),
        use_container_width=True
    )

except FileNotFoundError:
    st.error("❌ Dataset not found. Please place 'startup_funding.csv' inside the data folder.")

except Exception as e:
    st.error(f"An error occurred: {e}")
