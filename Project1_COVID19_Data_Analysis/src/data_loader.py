"""
Data loading, missing value handling, and feature engineering for COVID-19 Dataset.
"""

import os
import pandas as pd
import numpy as np
from typing import Tuple, Dict, Any


def load_and_preprocess_covid_data(dataset_path: str = None) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """
    Loads COVID-19 dataset from Excel or CSV, performs data validation,
    imputes missing values, and computes derived epidemiological metrics.
    """
    if dataset_path is None:
        base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
        excel_path = os.path.join(base_dir, "datasets", "covid_19_data.xlsx")
        csv_path = os.path.join(base_dir, "datasets", "covid_19_data.csv")
        dataset_path = excel_path if os.path.exists(excel_path) else csv_path

    # Read data
    if dataset_path.endswith(".xlsx"):
        df = pd.read_excel(dataset_path, sheet_name="Raw_Recorded_Data")
    else:
        df = pd.read_csv(dataset_path)

    df["Date"] = pd.to_datetime(df["Date"])

    # Missing value audit
    null_counts_before = df.isnull().sum().to_dict()

    # Impute missing values
    # For missing New_Recovered, estimate as 95% of New_Cases minus New_Deaths
    if df["New_Recovered"].isnull().any():
        estimated_rec = (df["New_Cases"] * 0.95 - df["New_Deaths"]).clip(lower=0)
        df["New_Recovered"] = df["New_Recovered"].fillna(estimated_rec)

    # For missing New_Vaccinated, fill with 0 (no report or pre-vaccine era)
    if df["New_Vaccinated"].isnull().any():
        df["New_Vaccinated"] = df["New_Vaccinated"].fillna(0)

    null_counts_after = df.isnull().sum().to_dict()

    # Feature Engineering
    df["Active_Cases"] = df["Total_Cases"] - df["Total_Recovered"] - df["Total_Deaths"]
    df["Case_Fatality_Rate"] = (df["Total_Deaths"] / df["Total_Cases"] * 100).round(2)
    df["Recovery_Rate"] = (df["Total_Recovered"] / df["Total_Cases"] * 100).round(2)
    df["Vaccination_Rate"] = (df["Total_Vaccinated"] / df["Population"] * 100).round(2)

    metadata = {
        "total_rows": len(df),
        "countries_count": df["Country"].nunique(),
        "date_range": [str(df["Date"].min().date()), str(df["Date"].max().date())],
        "null_counts_before": null_counts_before,
        "null_counts_after": null_counts_after
    }

    return df, metadata


if __name__ == "__main__":
    df, meta = load_and_preprocess_covid_data()
    print("COVID-19 Preprocessing Complete:")
    print(f"Total Rows: {meta['total_rows']}, Countries: {meta['countries_count']}")
    print(f"Date Range: {meta['date_range'][0]} to {meta['date_range'][1]}")
    print("Null Counts Before Cleaning:", meta["null_counts_before"])
    print("Null Counts After Cleaning:", meta["null_counts_after"])
