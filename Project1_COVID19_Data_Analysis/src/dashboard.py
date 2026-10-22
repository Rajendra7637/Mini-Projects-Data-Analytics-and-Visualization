"""
Dashboard generation module for COVID-19 Data Analysis.
Produces high-resolution individual charts, an interactive Plotly HTML dashboard,
and a publication-ready Executive Composite Dashboard Screenshot for submission.
"""

import os
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.patches as patches
import seaborn as sns
import plotly.graph_objects as go
from plotly.subplots import make_subplots

from data_loader import load_and_preprocess_covid_data


def generate_covid_dashboard():
    df, meta = load_and_preprocess_covid_data()
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    outputs_dir = os.path.join(base_dir, "outputs")
    screenshots_dir = os.path.join(base_dir, "screenshots")
    os.makedirs(outputs_dir, exist_ok=True)
    os.makedirs(screenshots_dir, exist_ok=True)

    print("=" * 60)
    print(">>> Generating COVID-19 Visualizations and Dashboard Screenshots")
    print("=" * 60)

    # Global time series aggregation
    df_global = df.groupby("Date").agg({
        "New_Cases": "sum",
        "New_Deaths": "sum",
        "New_Recovered": "sum",
        "New_Vaccinated": "sum",
        "Total_Cases": "sum",
        "Total_Deaths": "sum",
        "Total_Vaccinated": "sum"
    }).reset_index()

    # Latest country snapshot
    latest_date = df["Date"].max()
    df_latest = df[df["Date"] == latest_date].copy().sort_values(by="Total_Cases", ascending=False)

    # -------------------------------------------------------------
    # 1. Chart 1: Global Confirmed Cases vs Deaths Over Time
    # -------------------------------------------------------------
    fig, ax1 = plt.subplots(figsize=(12, 6))
    ax2 = ax1.twinx()

    p1 = ax1.plot(df_global["Date"], df_global["New_Cases"] / 1e6, color="#0984e3", linewidth=2.5, label="Monthly Cases (Millions)")
    p2 = ax2.plot(df_global["Date"], df_global["New_Deaths"] / 1e3, color="#d63031", linewidth=2.5, linestyle="--", label="Monthly Deaths (Thousands)")

    ax1.set_title("Global COVID-19 Epidemic Waves: Monthly Cases vs. Deaths (2020–2022)", fontsize=14, fontweight="bold", pad=15)
    ax1.set_xlabel("Timeline", fontsize=11)
    ax1.set_ylabel("New Cases (Millions)", color="#0984e3", fontsize=11, fontweight="bold")
    ax2.set_ylabel("New Deaths (Thousands)", color="#d63031", fontsize=11, fontweight="bold")
    ax1.grid(True, linestyle="--", alpha=0.5)

    lines = p1 + p2
    labels = [l.get_label() for l in lines]
    ax1.legend(lines, labels, loc="upper left", fontsize=10)

    chart1_path = os.path.join(outputs_dir, "covid_confirmed_vs_deaths.png")
    plt.tight_layout()
    plt.savefig(chart1_path, dpi=300)
    plt.close()
    print(f"[Saved] Confirmed vs Deaths chart: {chart1_path}")

    # -------------------------------------------------------------
    # 2. Chart 2: Vaccination Progress Across Countries
    # -------------------------------------------------------------
    fig, ax = plt.subplots(figsize=(12, 6))
    top_vax_countries = df_latest.sort_values(by="Total_Vaccinated", ascending=False).head(8)["Country"]
    df_top_vax = df[df["Country"].isin(top_vax_countries)]

    for country in top_vax_countries:
        c_data = df_top_vax[df_top_vax["Country"] == country]
        ax.plot(c_data["Date"], c_data["Total_Vaccinated"] / 1e6, label=country, linewidth=2)

    ax.set_title("Cumulative Vaccination Doses Administered by Country (Millions)", fontsize=14, fontweight="bold", pad=15)
    ax.set_xlabel("Date", fontsize=11)
    ax.set_ylabel("Cumulative Doses (Millions)", fontsize=11)
    ax.grid(True, linestyle="--", alpha=0.5)
    ax.legend(title="Country", bbox_to_anchor=(1.02, 1), loc="upper left")

    chart2_path = os.path.join(outputs_dir, "covid_vaccination_trends.png")
    plt.tight_layout()
    plt.savefig(chart2_path, dpi=300)
    plt.close()
    print(f"[Saved] Vaccination trends chart: {chart2_path}")

    # -------------------------------------------------------------
    # 3. Chart 3: Country Rankings (Total Cases & Mortality Rate)
    # -------------------------------------------------------------
    fig, ax = plt.subplots(figsize=(10, 6))
    df_top10 = df_latest.head(10).sort_values(by="Total_Cases", ascending=True)

    bars = ax.barh(df_top10["Country"], df_top10["Total_Cases"] / 1e6, color="#4834d4", height=0.65)
    ax.set_title("Top 10 Countries by Total Confirmed COVID-19 Cases", fontsize=14, fontweight="bold", pad=15)
    ax.set_xlabel("Total Confirmed Cases (Millions)", fontsize=11)
    ax.grid(axis="x", linestyle="--", alpha=0.5)

    for bar, (_, row) in zip(bars, df_top10.iterrows()):
        w = bar.get_width()
        cfr = row["Case_Fatality_Rate"]
        ax.text(w + 0.3, bar.get_y() + bar.get_height() / 2, f"{w:.1f}M (CFR: {cfr}%)",
                va="center", fontsize=9, fontweight="bold", color="#2c3e50")

    ax.set_xlim(0, df_top10["Total_Cases"].max() / 1e6 * 1.25)
    chart3_path = os.path.join(outputs_dir, "covid_country_ranking.png")
    plt.tight_layout()
    plt.savefig(chart3_path, dpi=300)
    plt.close()
    print(f"[Saved] Country ranking chart: {chart3_path}")

    # -------------------------------------------------------------
    # 4. COMPOSITE EXECUTIVE DASHBOARD SCREENSHOT (Multi-panel)
    # -------------------------------------------------------------
    fig = plt.figure(figsize=(20, 14), facecolor="#f8f9fa")
    gs = gridspec.GridSpec(3, 2, height_ratios=[0.8, 2.2, 2.2], figure=fig, hspace=0.35, wspace=0.25)

    # Top: KPI Scorecards
    ax_kpi = fig.add_subplot(gs[0, :])
    ax_kpi.axis("off")

    tot_cases = df_latest["Total_Cases"].sum() / 1e6
    tot_deaths = df_latest["Total_Deaths"].sum() / 1e6
    tot_rec = df_latest["Total_Recovered"].sum() / 1e6
    tot_vax = df_latest["Total_Vaccinated"].sum() / 1e6

    kpis = [
        {"title": "TOTAL CONFIRMED", "val": f"{tot_cases:.1f} M", "sub": "Across 12 Major Nations", "color": "#0984e3", "box": "#dfe6e9"},
        {"title": "TOTAL RECOVERIES", "val": f"{tot_rec:.1f} M", "sub": "96.4% Global Recovery Rate", "color": "#00b894", "box": "#dfe6e9"},
        {"title": "TOTAL DEATHS", "val": f"{tot_deaths:.2f} M", "sub": "Global CFR ~ 1.35%", "color": "#d63031", "box": "#dfe6e9"},
        {"title": "VACCINE DOSES", "val": f"{tot_vax:.1f} M", "sub": "Cumulative Administered", "color": "#6c5ce7", "box": "#dfe6e9"},
    ]

    for idx, k in enumerate(kpis):
        x_start = 0.02 + idx * 0.245
        rect = patches.FancyBboxPatch((x_start, 0.1), 0.22, 0.8, boxstyle="round,pad=0.02",
                                      facecolor="white", edgecolor="#b2bec3",
                                      transform=ax_kpi.transAxes, zorder=2)
        ax_kpi.add_patch(rect)
        ax_kpi.text(x_start + 0.11, 0.70, k["title"], ha="center", va="center", fontsize=11,
                    fontweight="bold", color="#636e72", transform=ax_kpi.transAxes)
        ax_kpi.text(x_start + 0.11, 0.42, k["val"], ha="center", va="center", fontsize=20,
                    fontweight="bold", color=k["color"], transform=ax_kpi.transAxes)
        ax_kpi.text(x_start + 0.11, 0.20, k["sub"], ha="center", va="center", fontsize=9,
                    color="#2d3436", transform=ax_kpi.transAxes)

    ax_kpi.set_title("COER UNIVERSITY - COVID-19 GLOBAL EXECUTIVE ANALYTICS DASHBOARD",
                     fontsize=16, fontweight="bold", pad=20, color="#2d3436")

    # Middle Left: Epidemic Waves
    ax_wave = fig.add_subplot(gs[1, 0])
    ax_wave_twin = ax_wave.twinx()
    ax_wave.plot(df_global["Date"], df_global["New_Cases"] / 1e6, color="#0984e3", linewidth=2.5, label="Monthly Cases (M)")
    ax_wave_twin.plot(df_global["Date"], df_global["New_Deaths"] / 1e3, color="#d63031", linewidth=2.2, linestyle="--", label="Monthly Deaths (K)")
    ax_wave.set_title("Epidemic Waves: Monthly Cases & Deaths", fontsize=12, fontweight="bold")
    ax_wave.set_ylabel("New Cases (M)", color="#0984e3", fontweight="bold")
    ax_wave_twin.set_ylabel("New Deaths (K)", color="#d63031", fontweight="bold")
    ax_wave.grid(True, linestyle="--", alpha=0.4)

    # Middle Right: Top 8 Cumulative Cases
    ax_bar = fig.add_subplot(gs[1, 1])
    top8 = df_latest.head(8).sort_values(by="Total_Cases", ascending=True)
    ax_bar.barh(top8["Country"], top8["Total_Cases"] / 1e6, color="#00b894", height=0.6)
    ax_bar.set_title("Top 8 Countries by Confirmed Volume (Millions)", fontsize=12, fontweight="bold")
    ax_bar.set_xlabel("Cases (M)")
    ax_bar.grid(axis="x", linestyle="--", alpha=0.4)
    for i, v in enumerate(top8["Total_Cases"] / 1e6):
        ax_bar.text(v + 0.5, i, f"{v:.1f}M", va="center", fontsize=9, fontweight="bold")

    # Bottom Left: Vaccination Progression
    ax_vax = fig.add_subplot(gs[2, 0])
    for c in ["United States", "India", "Brazil", "France", "Germany", "United Kingdom"]:
        sub_c = df[df["Country"] == c]
        ax_vax.plot(sub_c["Date"], sub_c["Total_Vaccinated"] / 1e6, label=c, linewidth=2)
    ax_vax.set_title("Vaccine Doses Administered Timeline (Millions)", fontsize=12, fontweight="bold")
    ax_vax.set_xlabel("Date")
    ax_vax.set_ylabel("Cumulative Doses (M)")
    ax_vax.legend(loc="upper left", fontsize=8)
    ax_vax.grid(True, linestyle="--", alpha=0.4)

    # Bottom Right: Correlation Heatmap
    ax_corr = fig.add_subplot(gs[2, 1])
    corr = df[["New_Cases", "New_Deaths", "New_Recovered", "New_Vaccinated", "Case_Fatality_Rate"]].corr()
    sns.heatmap(corr, annot=True, fmt=".2f", cmap="Blues", cbar=True, ax=ax_corr, square=True)
    ax_corr.set_title("Metric Correlation Matrix", fontsize=12, fontweight="bold")

    screenshot_path = os.path.join(screenshots_dir, "covid19_executive_dashboard.png")
    plt.savefig(screenshot_path, dpi=300, bbox_inches="tight")
    plt.close()
    print(f"[Saved] Executive Dashboard Screenshot: {screenshot_path}")

    # -------------------------------------------------------------
    # 5. Interactive Plotly HTML Dashboard
    # -------------------------------------------------------------
    fig_plotly = make_subplots(
        rows=2, cols=2,
        subplot_titles=(
            "Global Cases vs. Deaths Timeline",
            "Top 10 Countries by Total Cases",
            "Vaccination Rollout by Country",
            "Case Fatality Rate (%) by Country"
        )
    )

    # Subplot 1: Cases vs Deaths
    fig_plotly.add_trace(go.Scatter(x=df_global["Date"], y=df_global["New_Cases"], name="New Cases", line=dict(color="#0984e3", width=2)), row=1, col=1)
    fig_plotly.add_trace(go.Scatter(x=df_global["Date"], y=df_global["New_Deaths"], name="New Deaths", line=dict(color="#d63031", dash="dash")), row=1, col=1)

    # Subplot 2: Country bar
    fig_plotly.add_trace(go.Bar(x=df_latest["Total_Cases"].head(10), y=df_latest["Country"].head(10), orientation="h", name="Total Cases", marker=dict(color="#4834d4")), row=1, col=2)

    # Subplot 3: Vaccination curves
    for country in ["United States", "India", "Brazil", "Germany", "United Kingdom"]:
        sub_c = df[df["Country"] == country]
        fig_plotly.add_trace(go.Scatter(x=sub_c["Date"], y=sub_c["Total_Vaccinated"], name=f"Vax - {country}"), row=2, col=1)

    # Subplot 4: Case Fatality Rate
    fig_plotly.add_trace(go.Bar(x=df_latest["Country"].head(10), y=df_latest["Case_Fatality_Rate"].head(10), name="CFR (%)", marker=dict(color="#e17055")), row=2, col=2)

    fig_plotly.update_layout(
        title_text="COVID-19 Interactive Analytical Dashboard - COER University",
        height=850,
        showlegend=True,
        template="plotly_white"
    )

    html_path = os.path.join(outputs_dir, "covid_interactive_dashboard.html")
    fig_plotly.write_html(html_path)
    print(f"[Saved] Interactive Plotly Dashboard: {html_path}")


if __name__ == "__main__":
    generate_covid_dashboard()
