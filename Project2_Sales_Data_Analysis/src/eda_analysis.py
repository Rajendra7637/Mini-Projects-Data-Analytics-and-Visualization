"""
Exploratory Data Analysis (EDA) and business insights generator for Sales Dataset.
Analyzes monthly trends, customer segmentation, product performance, and regional profits.
"""

import os
import json
import pandas as pd
import numpy as np

from data_loader import load_and_preprocess_sales_data


def perform_sales_eda() -> dict:
    df, meta = load_and_preprocess_sales_data()
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    outputs_dir = os.path.join(base_dir, "outputs")
    os.makedirs(outputs_dir, exist_ok=True)

    print("=" * 60)
    print(">>> Performing Exploratory Data Analysis on Sales Dataset")
    print("=" * 60)

    # 1. Executive Financial KPIs
    total_sales = float(df["Sales"].sum())
    total_profit = float(df["Profit"].sum())
    total_quantity = int(df["Quantity"].sum())
    total_orders = int(df["Order_ID"].count())
    overall_margin = round((total_profit / total_sales) * 100, 2)
    avg_order_value = round(total_sales / total_orders, 2)

    print("\nExecutive Financial Metrics:")
    print(f"  Total Revenue:       ${total_sales:,.2f}")
    print(f"  Total Profit:        ${total_profit:,.2f}")
    print(f"  Profit Margin:       {overall_margin}%")
    print(f"  Total Transactions:  {total_orders:,}")
    print(f"  Average Order Value: ${avg_order_value:.2f}")

    # 2. Customer Segmentation
    segment_df = df.groupby("Segment").agg({
        "Sales": "sum",
        "Profit": "sum",
        "Order_ID": "count"
    }).rename(columns={"Order_ID": "Orders"}).reset_index()
    segment_df["Margin"] = (segment_df["Profit"] / segment_df["Sales"] * 100).round(2)
    segment_dict = segment_df.to_dict(orient="records")

    # 3. Product Category & Sub-Category Performance
    cat_df = df.groupby("Category").agg({
        "Sales": "sum",
        "Profit": "sum"
    }).reset_index()
    cat_df["Margin"] = (cat_df["Profit"] / cat_df["Sales"] * 100).round(2)

    subcat_df = df.groupby(["Category", "Sub_Category"]).agg({
        "Sales": "sum",
        "Profit": "sum",
        "Quantity": "sum",
        "Discount": "mean"
    }).reset_index()
    subcat_df["Margin"] = (subcat_df["Profit"] / subcat_df["Sales"] * 100).round(2)
    subcat_df["Discount"] = (subcat_df["Discount"] * 100).round(1)
    subcat_dict = subcat_df.sort_values(by="Sales", ascending=False).to_dict(orient="records")

    # 4. Regional Breakdown
    region_df = df.groupby("Region").agg({
        "Sales": "sum",
        "Profit": "sum",
        "Order_ID": "count"
    }).rename(columns={"Order_ID": "Orders"}).reset_index()
    region_df["Margin"] = (region_df["Profit"] / region_df["Sales"] * 100).round(2)
    region_dict = region_df.to_dict(orient="records")

    summary_metrics = {
        "financial_kpis": {
            "total_revenue": total_sales,
            "total_profit": total_profit,
            "profit_margin_percent": overall_margin,
            "total_transactions": total_orders,
            "average_order_value": avg_order_value,
            "total_units_sold": total_quantity
        },
        "customer_segmentation": segment_dict,
        "product_categories": cat_df.to_dict(orient="records"),
        "product_subcategories": subcat_dict,
        "regional_performance": region_dict,
        "metadata": meta
    }

    # Export to JSON
    json_path = os.path.join(outputs_dir, "sales_summary_metrics.json")
    with open(json_path, "w") as f:
        json.dump(summary_metrics, f, indent=4)
    print(f"\n[Saved] Sales summary metrics: {json_path}")

    return summary_metrics


if __name__ == "__main__":
    perform_sales_eda()
