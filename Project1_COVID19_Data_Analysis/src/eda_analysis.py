"""
Exploratory Data Analysis (EDA) module for COVID-19 Dataset.
Generates statistical summaries, country rankings, correlation analyses, and exports metrics.
"""

import os
import json
import pandas as pd
import numpy as np

from data_loader import load_and_preprocess_covid_data


def perform_covid_eda() -> dict:
    df, meta = load_and_preprocess_covid_data()
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    outputs_dir = os.path.join(base_dir, "outputs")
    os.makedirs(outputs_dir, exist_ok=True)

    print("=" * 60)
    print(">>> Performing Exploratory Data Analysis on COVID-19 Dataset")
    print("=" * 60)

    # 1. Latest Snapshot per Country
    latest_date = df["Date"].max()
    df_latest = df[df["Date"] == latest_date].copy()

    # 2. Global Aggregates
    global_cases = int(df_latest["Total_Cases"].sum())
    global_deaths = int(df_latest["Total_Deaths"].sum())
    global_recovered = int(df_latest["Total_Recovered"].sum())
    global_vaccinated = int(df_latest["Total_Vaccinated"].sum())
    global_cfr = round((global_deaths / global_cases) * 100, 2)
    global_rec_rate = round((global_recovered / global_cases) * 100, 2)

    print("\nGlobal COVID-19 Key Performance Indicators (KPIs):")
    print(f"  Total Confirmed Cases: {global_cases:,}")
    print(f"  Total Deaths:          {global_deaths:,}")
    print(f"  Total Recovered:       {global_recovered:,}")
    print(f"  Total Vaccinations:    {global_vaccinated:,}")
    print(f"  Global Fatality Rate:  {global_cfr}%")
    print(f"  Global Recovery Rate:  {global_rec_rate}%")

    # 3. Country Rankings (Top 10 by Confirmed Cases)
    top_cases = df_latest.sort_values(by="Total_Cases", ascending=False)[
        ["Country", "Total_Cases", "Total_Deaths", "Case_Fatality_Rate", "Vaccination_Rate"]
    ].head(10).to_dict(orient="records")

    print("\nTop Affected Countries by Total Confirmed Cases:")
    for rank, row in enumerate(top_cases[:5], 1):
        print(f"  {rank}. {row['Country']:15} | Cases: {row['Total_Cases']:,} | Deaths: {row['Total_Deaths']:,} | CFR: {row['Case_Fatality_Rate']}%")

    # 4. Correlation Analysis
    num_cols = ["New_Cases", "New_Deaths", "New_Recovered", "New_Vaccinated", "Case_Fatality_Rate"]
    corr_matrix = df[num_cols].corr().round(4).to_dict()

    summary_metrics = {
        "global_kpis": {
            "total_confirmed": global_cases,
            "total_deaths": global_deaths,
            "total_recovered": global_recovered,
            "total_vaccinated": global_vaccinated,
            "case_fatality_rate_percent": global_cfr,
            "recovery_rate_percent": global_rec_rate
        },
        "top_countries_by_cases": top_cases,
        "correlation_matrix": corr_matrix,
        "metadata": meta
    }

    # Save summary metrics to JSON
    json_path = os.path.join(outputs_dir, "covid_summary_metrics.json")
    with open(json_path, "w") as f:
        json.dump(summary_metrics, f, indent=4)
    print(f"\n[Saved] Summary metrics JSON: {json_path}")

    return summary_metrics


if __name__ == "__main__":
    perform_covid_eda()
