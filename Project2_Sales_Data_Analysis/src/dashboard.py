"""
Dashboard generation module for Sales Data Analysis.
Produces individual analytical charts, an interactive Plotly HTML dashboard,
and a publication-ready Executive Sales Dashboard Screenshot for academic submission.
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

from data_loader import load_and_preprocess_sales_data


def generate_sales_dashboard():
    df, meta = load_and_preprocess_sales_data()
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    outputs_dir = os.path.join(base_dir, "outputs")
    screenshots_dir = os.path.join(base_dir, "screenshots")
    os.makedirs(outputs_dir, exist_ok=True)
    os.makedirs(screenshots_dir, exist_ok=True)

    print("=" * 60)
    print(">>> Generating Sales Visualizations and Executive Dashboard Screenshots")
    print("=" * 60)

    # Aggregations
    # 1. Monthly
    df_monthly = df.groupby("Year_Month").agg({
        "Sales": "sum",
        "Profit": "sum",
        "Order_ID": "count"
    }).reset_index()

    # 2. Customer Segment
    df_seg = df.groupby("Segment").agg({
        "Sales": "sum",
        "Profit": "sum",
        "Order_ID": "count"
    }).reset_index()

    # 3. Product Sub-Category
    df_subcat = df.groupby(["Category", "Sub_Category"]).agg({
        "Sales": "sum",
        "Profit": "sum"
    }).reset_index().sort_values(by="Sales", ascending=True)

    # 4. Regional
    df_region = df.groupby("Region").agg({
        "Sales": "sum",
        "Profit": "sum"
    }).reset_index().sort_values(by="Sales", ascending=False)

    # -------------------------------------------------------------
    # Chart 1: Monthly Sales & Profit Trend
    # -------------------------------------------------------------
    fig, ax1 = plt.subplots(figsize=(13, 6))
    ax2 = ax1.twinx()

    x_idx = range(len(df_monthly))
    ax1.plot(x_idx, df_monthly["Sales"] / 1e3, color="#0984e3", marker="o", linewidth=2.5, label="Sales ($K)")
    ax2.plot(x_idx, df_monthly["Profit"] / 1e3, color="#00b894", marker="s", linewidth=2.5, linestyle="--", label="Profit ($K)")

    ax1.set_xticks(x_idx[::3])
    ax1.set_xticklabels(df_monthly["Year_Month"].iloc[::3], rotation=45, ha="right")
    ax1.set_title("Monthly Sales Revenue and Gross Profit Trends (2023–2025)", fontsize=14, fontweight="bold", pad=15)
    ax1.set_xlabel("Year-Month", fontsize=11)
    ax1.set_ylabel("Sales ($ in Thousands)", color="#0984e3", fontsize=11, fontweight="bold")
    ax2.set_ylabel("Profit ($ in Thousands)", color="#00b894", fontsize=11, fontweight="bold")
    ax1.grid(True, linestyle="--", alpha=0.5)

    chart1_path = os.path.join(outputs_dir, "monthly_sales_profit_trend.png")
    plt.tight_layout()
    plt.savefig(chart1_path, dpi=300)
    plt.close()
    print(f"[Saved] Monthly sales & profit trend: {chart1_path}")

    # -------------------------------------------------------------
    # Chart 2: Customer Segmentation Donut
    # -------------------------------------------------------------
    fig, ax = plt.subplots(figsize=(8, 7))
    colors = ["#4834d4", "#f0932b", "#6ab04c"]
    wedges, texts, autotexts = ax.pie(
        df_seg["Sales"],
        labels=df_seg["Segment"],
        autopct="%1.1f%%",
        startangle=140,
        colors=colors,
        wedgeprops=dict(width=0.4, edgecolor="white", linewidth=2),
        pctdistance=0.75
    )
    plt.setp(autotexts, size=11, weight="bold", color="white")
    plt.setp(texts, size=11, weight="bold")
    ax.set_title("Revenue Contribution by Customer Segment", fontsize=14, fontweight="bold", pad=15)

    chart2_path = os.path.join(outputs_dir, "customer_segmentation.png")
    plt.tight_layout()
    plt.savefig(chart2_path, dpi=300)
    plt.close()
    print(f"[Saved] Customer segmentation chart: {chart2_path}")

    # -------------------------------------------------------------
    # Chart 3: Product Sub-Category Performance
    # -------------------------------------------------------------
    fig, ax = plt.subplots(figsize=(11, 7))
    bars = ax.barh(df_subcat["Sub_Category"], df_subcat["Sales"] / 1e3, color="#6c5ce7", height=0.65)
    ax.set_title("Sales Revenue by Product Sub-Category ($ in Thousands)", fontsize=14, fontweight="bold", pad=15)
    ax.set_xlabel("Sales ($K)", fontsize=11)
    ax.grid(axis="x", linestyle="--", alpha=0.5)

    for bar, (_, row) in zip(bars, df_subcat.iterrows()):
        profit_k = row["Profit"] / 1e3
        color = "#00b894" if profit_k >= 0 else "#d63031"
        ax.text(bar.get_width() + 5, bar.get_y() + bar.get_height() / 2, f"${profit_k:.1f}K profit",
                va="center", fontsize=8.5, fontweight="bold", color=color)

    ax.set_xlim(0, df_subcat["Sales"].max() / 1e3 * 1.25)
    chart3_path = os.path.join(outputs_dir, "product_category_performance.png")
    plt.tight_layout()
    plt.savefig(chart3_path, dpi=300)
    plt.close()
    print(f"[Saved] Product category performance: {chart3_path}")

    # -------------------------------------------------------------
    # Chart 4: Regional Sales & Profit
    # -------------------------------------------------------------
    fig, ax = plt.subplots(figsize=(10, 6))
    x = np.arange(len(df_region))
    w = 0.35

    ax.bar(x - w/2, df_region["Sales"] / 1e3, width=w, label="Sales ($K)", color="#0984e3")
    ax.bar(x + w/2, df_region["Profit"] / 1e3, width=w, label="Profit ($K)", color="#00b894")

    ax.set_xticks(x)
    ax.set_xticklabels(df_region["Region"], fontsize=11, fontweight="bold")
    ax.set_title("Regional Distribution of Sales and Net Profit ($K)", fontsize=14, fontweight="bold", pad=15)
    ax.set_ylabel("Amount ($ in Thousands)", fontsize=11)
    ax.legend(fontsize=11)
    ax.grid(axis="y", linestyle="--", alpha=0.5)

    chart4_path = os.path.join(outputs_dir, "regional_sales_profit_distribution.png")
    plt.tight_layout()
    plt.savefig(chart4_path, dpi=300)
    plt.close()
    print(f"[Saved] Regional sales & profit distribution: {chart4_path}")

    # -------------------------------------------------------------
    # 5. COMPOSITE EXECUTIVE SALES DASHBOARD SCREENSHOT
    # -------------------------------------------------------------
    fig = plt.figure(figsize=(20, 14), facecolor="#f8f9fa")
    gs = gridspec.GridSpec(3, 2, height_ratios=[0.8, 2.2, 2.2], figure=fig, hspace=0.35, wspace=0.25)

    # Top: KPI Scorecards
    ax_kpi = fig.add_subplot(gs[0, :])
    ax_kpi.axis("off")

    tot_rev = df["Sales"].sum() / 1e6
    tot_prof = df["Profit"].sum() / 1e3
    margin = (df["Profit"].sum() / df["Sales"].sum()) * 100
    aov = df["Sales"].sum() / len(df)

    kpis = [
        {"title": "TOTAL REVENUE", "val": f"${tot_rev:.2f} M", "sub": "3-Year Commercial Sales", "color": "#0984e3"},
        {"title": "NET PROFIT", "val": f"${tot_prof:.1f} K", "sub": "Total Operating Profit", "color": "#00b894"},
        {"title": "PROFIT MARGIN", "val": f"{margin:.2f}%", "sub": "Overall Return on Sales", "color": "#6c5ce7"},
        {"title": "AVG ORDER VALUE", "val": f"${aov:.2f}", "sub": f"{len(df):,} Total Orders", "color": "#f0932b"}
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

    ax_kpi.set_title("RETAIL & COMMERCIAL SALES EXECUTIVE DASHBOARD",
                     fontsize=16, fontweight="bold", pad=20, color="#2d3436")

    # Middle Left: Monthly Trend
    ax_m = fig.add_subplot(gs[1, 0])
    ax_m_twin = ax_m.twinx()
    ax_m.plot(range(len(df_monthly)), df_monthly["Sales"] / 1e3, color="#0984e3", linewidth=2.5, label="Sales ($K)")
    ax_m_twin.plot(range(len(df_monthly)), df_monthly["Profit"] / 1e3, color="#00b894", linewidth=2.2, linestyle="--", label="Profit ($K)")
    ax_m.set_xticks(range(0, len(df_monthly), 4))
    ax_m.set_xticklabels(df_monthly["Year_Month"].iloc[::4], rotation=40, ha="right")
    ax_m.set_title("Monthly Revenue & Profit Progression", fontsize=12, fontweight="bold")
    ax_m.set_ylabel("Sales ($K)", color="#0984e3", fontweight="bold")
    ax_m_twin.set_ylabel("Profit ($K)", color="#00b894", fontweight="bold")
    ax_m.grid(True, linestyle="--", alpha=0.4)

    # Middle Right: Customer Segment Donut
    ax_donut = fig.add_subplot(gs[1, 1])
    wedges, texts, autotexts = ax_donut.pie(
        df_seg["Sales"], labels=df_seg["Segment"], autopct="%1.1f%%",
        colors=["#4834d4", "#f0932b", "#6ab04c"],
        wedgeprops=dict(width=0.4, edgecolor="white", linewidth=2), pctdistance=0.75
    )
    plt.setp(autotexts, size=10, weight="bold", color="white")
    plt.setp(texts, size=10, weight="bold")
    ax_donut.set_title("Customer Segment Revenue Share", fontsize=12, fontweight="bold")

    # Bottom Left: Product Sub-Category Bars
    ax_sub = fig.add_subplot(gs[2, 0])
    top_sub = df_subcat.tail(10)
    bars_sub = ax_sub.barh(top_sub["Sub_Category"], top_sub["Sales"] / 1e3, color="#6c5ce7", height=0.6)
    ax_sub.set_title("Top 10 Sub-Categories by Revenue ($K)", fontsize=12, fontweight="bold")
    ax_sub.set_xlabel("Sales ($K)")
    ax_sub.grid(axis="x", linestyle="--", alpha=0.4)
    for b in bars_sub:
        ax_sub.text(b.get_width() + 5, b.get_y() + b.get_height() / 2, f"${b.get_width():.0f}K",
                    va="center", fontsize=8, fontweight="bold")

    # Bottom Right: Regional Sales & Profit
    ax_reg = fig.add_subplot(gs[2, 1])
    rx = np.arange(len(df_region))
    rw = 0.35
    ax_reg.bar(rx - rw/2, df_region["Sales"] / 1e3, width=rw, label="Sales ($K)", color="#0984e3")
    ax_reg.bar(rx + rw/2, df_region["Profit"] / 1e3, width=rw, label="Profit ($K)", color="#00b894")
    ax_reg.set_xticks(rx)
    ax_reg.set_xticklabels(df_region["Region"], fontweight="bold")
    ax_reg.set_title("Regional Sales & Profit Distribution", fontsize=12, fontweight="bold")
    ax_reg.set_ylabel("Amount ($K)")
    ax_reg.legend(fontsize=9)
    ax_reg.grid(axis="y", linestyle="--", alpha=0.4)

    sales_screenshot_path = os.path.join(screenshots_dir, "sales_executive_dashboard.png")
    plt.savefig(sales_screenshot_path, dpi=300, bbox_inches="tight")
    plt.close()
    print(f"[Saved] Executive Sales Dashboard Screenshot: {sales_screenshot_path}")

    # -------------------------------------------------------------
    # 6. Interactive Plotly HTML Dashboard
    # -------------------------------------------------------------
    fig_plotly = make_subplots(
        rows=2, cols=2,
        specs=[
            [{"type": "xy"}, {"type": "domain"}],
            [{"type": "xy"}, {"type": "xy"}]
        ],
        subplot_titles=(
            "Monthly Sales and Profit Trend",
            "Customer Segment Contribution",
            "Product Sub-Category Sales & Profits",
            "Regional Performance (Sales vs. Profit)"
        )
    )

    # Subplot 1: Monthly
    fig_plotly.add_trace(go.Scatter(x=df_monthly["Year_Month"], y=df_monthly["Sales"], name="Sales", line=dict(color="#0984e3", width=2.5)), row=1, col=1)
    fig_plotly.add_trace(go.Scatter(x=df_monthly["Year_Month"], y=df_monthly["Profit"], name="Profit", line=dict(color="#00b894", dash="dash")), row=1, col=1)

    # Subplot 2: Segment Pie
    fig_plotly.add_trace(go.Pie(labels=df_seg["Segment"], values=df_seg["Sales"], name="Segment", hole=0.4), row=1, col=2)

    # Subplot 3: Sub-Category Bar
    fig_plotly.add_trace(go.Bar(x=df_subcat["Sales"], y=df_subcat["Sub_Category"], orientation="h", name="Sub-Category Sales", marker=dict(color="#6c5ce7")), row=2, col=1)

    # Subplot 4: Regional Grouped Bar
    fig_plotly.add_trace(go.Bar(x=df_region["Region"], y=df_region["Sales"], name="Regional Sales", marker=dict(color="#0984e3")), row=2, col=2)
    fig_plotly.add_trace(go.Bar(x=df_region["Region"], y=df_region["Profit"], name="Regional Profit", marker=dict(color="#00b894")), row=2, col=2)

    fig_plotly.update_layout(
        title_text="Sales Analytics Interactive Dashboard",
        height=850,
        showlegend=True,
        template="plotly_white"
    )

    html_path = os.path.join(outputs_dir, "sales_interactive_dashboard.html")
    fig_plotly.write_html(html_path)
    print(f"[Saved] Interactive Plotly Sales Dashboard: {html_path}")


if __name__ == "__main__":
    generate_sales_dashboard()
