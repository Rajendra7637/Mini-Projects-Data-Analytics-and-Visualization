"""
Generates realistic, comprehensive benchmark datasets for:
1. COVID-19 Data Analysis Dashboard (Confirmed, Deaths, Recoveries, Vaccinations, Country-wise)
2. Sales Data Analysis Dashboard (Transactions, Customers, Regions, Products, Categories, Profit)
Exports both datasets into multi-sheet Excel (.xlsx) and CSV (.csv) formats.
"""

import os
import numpy as np
import pandas as pd

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATA_DIR = os.path.join(BASE_DIR, "datasets")
os.makedirs(DATA_DIR, exist_ok=True)

def generate_covid19_dataset():
    print(">>> Generating COVID-19 Multi-Sheet Dataset...")
    np.random.seed(42)

    countries = [
        {"name": "United States", "code": "USA", "pop": 331000000, "cfr_base": 0.012, "peak_scale": 1.0},
        {"name": "India", "code": "IND", "pop": 1380000000, "cfr_base": 0.011, "peak_scale": 0.95},
        {"name": "Brazil", "code": "BRA", "pop": 213000000, "cfr_base": 0.020, "peak_scale": 0.70},
        {"name": "France", "code": "FRA", "pop": 67000000, "cfr_base": 0.008, "peak_scale": 0.45},
        {"name": "Germany", "code": "DEU", "pop": 83000000, "cfr_base": 0.007, "peak_scale": 0.40},
        {"name": "United Kingdom", "code": "GBR", "pop": 68000000, "cfr_base": 0.014, "peak_scale": 0.42},
        {"name": "Italy", "code": "ITA", "pop": 60000000, "cfr_base": 0.019, "peak_scale": 0.38},
        {"name": "Russia", "code": "RUS", "pop": 146000000, "cfr_base": 0.021, "peak_scale": 0.35},
        {"name": "Japan", "code": "JPN", "pop": 126000000, "cfr_base": 0.004, "peak_scale": 0.30},
        {"name": "South Korea", "code": "KOR", "pop": 52000000, "cfr_base": 0.003, "peak_scale": 0.28},
        {"name": "Australia", "code": "AUS", "pop": 26000000, "cfr_base": 0.003, "peak_scale": 0.15},
        {"name": "South Africa", "code": "ZAF", "pop": 59000000, "cfr_base": 0.024, "peak_scale": 0.18}
    ]

    # Generate monthly time series from Jan 2020 to Dec 2022 (36 months)
    dates = pd.date_range(start="2020-01-01", end="2022-12-01", freq="MS")
    rows = []

    for c in countries:
        cum_cases = 0
        cum_deaths = 0
        cum_rec = 0
        cum_vax = 0

        for t_idx, d in enumerate(dates):
            month_num = t_idx + 1
            # Wave dynamics simulation (Wave 1: month 5-10, Wave 2 Delta: 16-20, Wave 3 Omicron: 24-28)
            wave1 = np.exp(-((month_num - 7) ** 2) / 8.0)
            wave2 = np.exp(-((month_num - 18) ** 2) / 10.0) * 1.5
            wave3 = np.exp(-((month_num - 26) ** 2) / 6.0) * 2.5
            wave_factor = 0.05 + wave1 + wave2 + wave3

            # Noise
            noise = np.random.uniform(0.85, 1.15)
            monthly_cases = int(c["pop"] * 0.0015 * c["peak_scale"] * wave_factor * noise)
            monthly_cases = max(100, monthly_cases)

            # Mortality
            cfr = c["cfr_base"] * (1.2 if month_num < 15 else 0.6)  # Drops as vaccines roll out
            monthly_deaths = int(monthly_cases * cfr * np.random.uniform(0.9, 1.1))

            # Recoveries
            monthly_rec = int(monthly_cases * (0.95 - cfr) * np.random.uniform(0.92, 1.05))

            # Vaccinations (Starts around Dec 2020 / month 12)
            if month_num >= 12:
                vax_progress = 1.0 / (1.0 + np.exp(-0.35 * (month_num - 20)))
                target_vax = int(c["pop"] * 1.8 * vax_progress)
                monthly_vax = max(0, target_vax - cum_vax)
            else:
                monthly_vax = 0

            cum_cases += monthly_cases
            cum_deaths += monthly_deaths
            cum_rec += monthly_rec
            cum_vax += monthly_vax

            rows.append({
                "Date": d.strftime("%Y-%m-%d"),
                "Country": c["name"],
                "Country_Code": c["code"],
                "Population": c["pop"],
                "New_Cases": monthly_cases,
                "New_Deaths": monthly_deaths,
                "New_Recovered": monthly_rec,
                "New_Vaccinated": monthly_vax,
                "Total_Cases": cum_cases,
                "Total_Deaths": cum_deaths,
                "Total_Recovered": cum_rec,
                "Total_Vaccinated": cum_vax,
            })

    df_raw = pd.DataFrame(rows)

    # Introduce intentional realistic missing values in Raw Data to satisfy "Handle missing values"
    df_raw_with_nulls = df_raw.copy()
    # Mask 4% of New_Recovered as NaN
    rec_mask = np.random.rand(len(df_raw)) < 0.04
    df_raw_with_nulls.loc[rec_mask, "New_Recovered"] = np.nan
    # Mask 3% of New_Vaccinated as NaN
    vax_mask = np.random.rand(len(df_raw)) < 0.03
    df_raw_with_nulls.loc[vax_mask, "New_Vaccinated"] = np.nan

    # Cleaned DataFrame
    df_clean = df_raw.copy()
    df_clean["New_Recovered"] = df_clean["New_Recovered"].fillna(df_clean["New_Cases"] * 0.95)
    df_clean["New_Vaccinated"] = df_clean["New_Vaccinated"].fillna(0)
    df_clean["Active_Cases"] = df_clean["Total_Cases"] - df_clean["Total_Recovered"] - df_clean["Total_Deaths"]
    df_clean["Case_Fatality_Rate"] = (df_clean["Total_Deaths"] / df_clean["Total_Cases"] * 100).round(2)
    df_clean["Recovery_Rate"] = (df_clean["Total_Recovered"] / df_clean["Total_Cases"] * 100).round(2)
    df_clean["Vaccination_Rate"] = (df_clean["Total_Vaccinated"] / df_clean["Population"] * 100).round(2)

    # Country Summary Sheet (latest status)
    latest_date = df_clean["Date"].max()
    df_latest = df_clean[df_clean["Date"] == latest_date].copy()
    df_country_summary = df_latest[[
        "Country", "Country_Code", "Population", "Total_Cases", "Total_Deaths",
        "Total_Recovered", "Active_Cases", "Total_Vaccinated",
        "Case_Fatality_Rate", "Recovery_Rate", "Vaccination_Rate"
    ]].sort_values(by="Total_Cases", ascending=False).reset_index(drop=True)

    # Global Monthly Timeline Sheet
    df_global_timeline = df_clean.groupby("Date").agg({
        "New_Cases": "sum",
        "New_Deaths": "sum",
        "New_Recovered": "sum",
        "New_Vaccinated": "sum",
        "Total_Cases": "sum",
        "Total_Deaths": "sum",
        "Total_Recovered": "sum",
        "Total_Vaccinated": "sum"
    }).reset_index()

    # Save to Multi-sheet Excel
    excel_path = os.path.join(DATA_DIR, "covid_19_data.xlsx")
    with pd.ExcelWriter(excel_path, engine="openpyxl") as writer:
        df_raw_with_nulls.to_excel(writer, sheet_name="Raw_Recorded_Data", index=False)
        df_clean.to_excel(writer, sheet_name="Cleaned_Data", index=False)
        df_country_summary.to_excel(writer, sheet_name="Country_Summary", index=False)
        df_global_timeline.to_excel(writer, sheet_name="Global_Timeline", index=False)
    print(f"[Saved] COVID-19 Excel: {excel_path}")

    # Also save CSV for easy pandas scripts
    csv_path = os.path.join(DATA_DIR, "covid_19_data.csv")
    df_clean.to_csv(csv_path, index=False)
    print(f"[Saved] COVID-19 CSV: {csv_path}")


def generate_sales_dataset():
    print("\n>>> Generating Retail & Commercial Sales Multi-Sheet Dataset...")
    np.random.seed(101)

    n_orders = 5000
    order_ids = [f"CA-2024-{100000 + i}" for i in range(n_orders)]

    # Dates spanning 2023 to 2025
    start_date = pd.to_datetime("2023-01-01")
    end_date = pd.to_datetime("2025-12-31")
    date_range_days = (end_date - start_date).days
    random_days = np.random.randint(0, date_range_days, size=n_orders)
    order_dates = [start_date + pd.Timedelta(days=int(d)) for d in random_days]

    ship_modes = ["Standard Class", "Second Class", "First Class", "Same Day"]
    ship_mode_probs = [0.60, 0.20, 0.15, 0.05]
    chosen_ship_modes = np.random.choice(ship_modes, size=n_orders, p=ship_mode_probs)

    customer_segments = ["Consumer", "Corporate", "Home Office"]
    segment_probs = [0.52, 0.30, 0.18]
    chosen_segments = np.random.choice(customer_segments, size=n_orders, p=segment_probs)

    regions_states = {
        "West": ["California", "Washington", "Oregon", "Nevada", "Arizona", "Colorado"],
        "East": ["New York", "Pennsylvania", "Ohio", "Massachusetts", "New Jersey"],
        "Central": ["Texas", "Illinois", "Michigan", "Indiana", "Wisconsin", "Minnesota"],
        "South": ["Florida", "North Carolina", "Virginia", "Georgia", "Tennessee"]
    }
    regions = list(regions_states.keys())
    chosen_regions = np.random.choice(regions, size=n_orders, p=[0.32, 0.28, 0.24, 0.16])
    chosen_states = [np.random.choice(regions_states[r]) for r in chosen_regions]

    # Products hierarchy
    product_catalog = {
        "Technology": {
            "Phones": (150, 1100, 0.18),
            "Accessories": (25, 220, 0.35),
            "Machines": (400, 2500, 0.08),
            "Copiers": (600, 3200, 0.30)
        },
        "Furniture": {
            "Chairs": (90, 600, 0.12),
            "Bookcases": (110, 750, -0.05), # Some loss leaders
            "Tables": (180, 1200, -0.08),
            "Furnishings": (15, 180, 0.24)
        },
        "Office Supplies": {
            "Storage": (30, 350, 0.16),
            "Binders": (5, 95, 0.38),
            "Paper": (8, 75, 0.42),
            "Art": (6, 50, 0.28),
            "Appliances": (50, 450, 0.20),
            "Envelopes": (4, 40, 0.36)
        }
    }

    categories = list(product_catalog.keys())
    cat_weights = [0.35, 0.30, 0.35]

    chosen_cats = np.random.choice(categories, size=n_orders, p=cat_weights)
    chosen_subcats = []
    sales = []
    profits = []
    quantities = []
    discounts = []

    for cat in chosen_cats:
        subcats = list(product_catalog[cat].keys())
        subcat = np.random.choice(subcats)
        chosen_subcats.append(subcat)

        min_p, max_p, base_margin = product_catalog[cat][subcat]
        qty = np.random.randint(1, 9)
        unit_price = np.random.uniform(min_p, max_p)
        order_sale = round(unit_price * qty, 2)

        # Discount between 0% and 40% (tables/bookcases sometimes higher discount)
        disc = np.random.choice([0.0, 0.1, 0.2, 0.3, 0.4, 0.5], p=[0.50, 0.15, 0.15, 0.10, 0.07, 0.03])
        # High discount reduces margin
        effective_margin = base_margin - (disc * 0.8) + np.random.normal(0, 0.04)
        order_profit = round(order_sale * effective_margin, 2)

        quantities.append(qty)
        sales.append(order_sale)
        discounts.append(disc)
        profits.append(order_profit)

    # Create Customer IDs
    n_unique_cust = 800
    cust_id_pool = [f"CUST-{1000 + i}" for i in range(n_unique_cust)]
    chosen_cust_ids = np.random.choice(cust_id_pool, size=n_orders)

    df_sales_raw = pd.DataFrame({
        "Order_ID": order_ids,
        "Order_Date": [d.strftime("%Y-%m-%d") for d in order_dates],
        "Ship_Date": [(d + pd.Timedelta(days=int(np.random.randint(2, 6)))).strftime("%Y-%m-%d") for d in order_dates],
        "Ship_Mode": chosen_ship_modes,
        "Customer_ID": chosen_cust_ids,
        "Segment": chosen_segments,
        "Region": chosen_regions,
        "State": chosen_states,
        "Category": chosen_cats,
        "Sub_Category": chosen_subcats,
        "Sales": sales,
        "Quantity": quantities,
        "Discount": discounts,
        "Profit": profits
    })

    # Intentional missing values in raw sales data for cleaning demonstration
    df_sales_with_nulls = df_sales_raw.copy()
    disc_mask = np.random.rand(len(df_sales_raw)) < 0.03
    df_sales_with_nulls.loc[disc_mask, "Discount"] = np.nan
    ship_mask = np.random.rand(len(df_sales_raw)) < 0.02
    df_sales_with_nulls.loc[ship_mask, "Ship_Mode"] = np.nan

    # Cleaned DataFrame
    df_sales_clean = df_sales_raw.copy()
    df_sales_clean["Discount"] = df_sales_clean["Discount"].fillna(0.0)
    df_sales_clean["Ship_Mode"] = df_sales_clean["Ship_Mode"].fillna("Standard Class")
    df_sales_clean["Profit_Margin"] = (df_sales_clean["Profit"] / df_sales_clean["Sales"] * 100).round(2)
    df_sales_clean["Year_Month"] = pd.to_datetime(df_sales_clean["Order_Date"]).dt.to_period("M").astype(str)

    # Monthly Summary Sheet
    df_monthly = df_sales_clean.groupby("Year_Month").agg({
        "Sales": "sum",
        "Profit": "sum",
        "Quantity": "sum",
        "Order_ID": "count"
    }).rename(columns={"Order_ID": "Total_Orders"}).reset_index()
    df_monthly["Profit_Margin"] = (df_monthly["Profit"] / df_monthly["Sales"] * 100).round(2)

    # Customer Segment Sheet
    df_cust_seg = df_sales_clean.groupby("Segment").agg({
        "Sales": "sum",
        "Profit": "sum",
        "Order_ID": "count",
        "Quantity": "sum"
    }).rename(columns={"Order_ID": "Total_Orders"}).reset_index()
    df_cust_seg["Profit_Margin"] = (df_cust_seg["Profit"] / df_cust_seg["Sales"] * 100).round(2)

    # Product Performance Sheet
    df_product = df_sales_clean.groupby(["Category", "Sub_Category"]).agg({
        "Sales": "sum",
        "Profit": "sum",
        "Quantity": "sum",
        "Order_ID": "count"
    }).rename(columns={"Order_ID": "Total_Orders"}).reset_index()
    df_product["Profit_Margin"] = (df_product["Profit"] / df_product["Sales"] * 100).round(2)
    df_product = df_product.sort_values(by="Sales", ascending=False).reset_index(drop=True)

    # Regional Performance Sheet
    df_region = df_sales_clean.groupby(["Region", "State"]).agg({
        "Sales": "sum",
        "Profit": "sum",
        "Order_ID": "count"
    }).rename(columns={"Order_ID": "Total_Orders"}).reset_index().sort_values(by="Sales", ascending=False)

    # Save to Multi-sheet Excel
    excel_path = os.path.join(DATA_DIR, "sales_data.xlsx")
    with pd.ExcelWriter(excel_path, engine="openpyxl") as writer:
        df_sales_with_nulls.to_excel(writer, sheet_name="Raw_Orders_Data", index=False)
        df_sales_clean.to_excel(writer, sheet_name="Cleaned_Orders", index=False)
        df_monthly.to_excel(writer, sheet_name="Monthly_Trends", index=False)
        df_cust_seg.to_excel(writer, sheet_name="Customer_Segmentation", index=False)
        df_product.to_excel(writer, sheet_name="Product_Performance", index=False)
        df_region.to_excel(writer, sheet_name="Regional_Summary", index=False)
    print(f"[Saved] Sales Excel: {excel_path}")

    # Also save CSV
    csv_path = os.path.join(DATA_DIR, "sales_data.csv")
    df_sales_clean.to_csv(csv_path, index=False)
    print(f"[Saved] Sales CSV: {csv_path}")


if __name__ == "__main__":
    generate_covid19_dataset()
    generate_sales_dataset()
