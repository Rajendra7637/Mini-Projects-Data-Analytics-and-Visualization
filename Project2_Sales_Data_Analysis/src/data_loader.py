"""
Data loading, missing value handling, and feature engineering for Retail & Commercial Sales Dataset.
"""

import os
import pandas as pd
import numpy as np
from typing import Tuple, Dict, Any


def load_and_preprocess_sales_data(dataset_path: str = None) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """
    Loads Sales dataset from Excel or CSV, validates data types,
    handles missing values, and engineers business analysis attributes.
    """
    if dataset_path is None:
        base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
        excel_path = os.path.join(base_dir, "datasets", "sales_data.xlsx")
        csv_path = os.path.join(base_dir, "datasets", "sales_data.csv")
        dataset_path = excel_path if os.path.exists(excel_path) else csv_path

    # Read data
    if dataset_path.endswith(".xlsx"):
        df = pd.read_excel(dataset_path, sheet_name="Raw_Orders_Data")
    else:
        df = pd.read_csv(dataset_path)

    df["Order_Date"] = pd.to_datetime(df["Order_Date"])
    df["Ship_Date"] = pd.to_datetime(df["Ship_Date"])

    # Audit missing values
    null_counts_before = df.isnull().sum().to_dict()

    # Impute missing values
    if df["Discount"].isnull().any():
        df["Discount"] = df["Discount"].fillna(0.0)

    if df["Ship_Mode"].isnull().any():
        df["Ship_Mode"] = df["Ship_Mode"].fillna("Standard Class")

    null_counts_after = df.isnull().sum().to_dict()

    # Feature engineering
    df["Profit_Margin"] = (df["Profit"] / df["Sales"] * 100).round(2)
    df["Order_Year"] = df["Order_Date"].dt.year
    df["Order_Month"] = df["Order_Date"].dt.month
    df["Year_Month"] = df["Order_Date"].dt.to_period("M").astype(str)
    df["Shipping_Days"] = (df["Ship_Date"] - df["Order_Date"]).dt.days

    metadata = {
        "total_transactions": len(df),
        "unique_customers": df["Customer_ID"].nunique(),
        "date_range": [str(df["Order_Date"].min().date()), str(df["Order_Date"].max().date())],
        "null_counts_before": null_counts_before,
        "null_counts_after": null_counts_after
    }

    return df, metadata


if __name__ == "__main__":
    df, meta = load_and_preprocess_sales_data()
    print("Sales Data Preprocessing Complete:")
    print(f"Transactions: {meta['total_transactions']}, Unique Customers: {meta['unique_customers']}")
    print(f"Date Range: {meta['date_range'][0]} to {meta['date_range'][1]}")
    print("Null Counts Before Cleaning:", meta["null_counts_before"])
    print("Null Counts After Cleaning:", meta["null_counts_after"])
