import pandas as pd
import streamlit as st


@st.cache_data
def load_data():
    """
    Load startup funding dataset.
    """
    try:
        df = pd.read_csv("data/startup_funding.csv")
        return df

    except FileNotFoundError:
        st.error(
            "Dataset not found. Please place 'startup_funding.csv' inside the data folder."
        )
        return pd.DataFrame()

    except Exception as e:
        st.error(f"Error loading dataset: {e}")
        return pd.DataFrame()
