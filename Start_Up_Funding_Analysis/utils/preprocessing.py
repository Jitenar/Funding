import pandas as pd
import numpy as np


def clean_data(df):
    """
    Basic data cleaning.
    """

    # Remove duplicate rows
    df = df.drop_duplicates()

    # Remove leading/trailing spaces from column names
    df.columns = df.columns.str.strip()

    return df


def handle_missing_values(df):
    """
    Handle missing values.
    """

    # Fill missing categorical values
    categorical_cols = [
        "Startup_Name",
        "Industry_Vertical",
        "City",
        "Investors_Name"
    ]

    for col in categorical_cols:
        if col in df.columns:
            df[col] = df[col].fillna("Unknown")

    return df


def convert_dates(df):
    """
    Convert funding date column.
    """

    if "Funding_Date" in df.columns:
        df["Funding_Date"] = pd.to_datetime(
            df["Funding_Date"],
            errors="coerce"
        )

        df["Year"] = df["Funding_Date"].dt.year
        df["Month"] = df["Funding_Date"].dt.month_name()

    return df


def clean_funding_amount(df):
    """
    Clean Amount_USD column.
    """

    if "Amount_USD" in df.columns:

        df["Amount_USD"] = (
            df["Amount_USD"]
            .astype(str)
            .str.replace(",", "", regex=False)
            .str.replace("$", "", regex=False)
        )

        df["Amount_USD"] = pd.to_numeric(
            df["Amount_USD"],
            errors="coerce"
        )

        df["Amount_USD"] = df["Amount_USD"].fillna(0)

    return df


def preprocess_data(df):
    """
    Complete preprocessing pipeline.
    """

    df = clean_data(df)
    df = handle_missing_values(df)
    df = convert_dates(df)
    df = clean_funding_amount(df)

    return df
