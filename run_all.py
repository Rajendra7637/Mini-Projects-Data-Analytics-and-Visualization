"""
Unified Execution Runner for Lab Sheet-09: Mini Projects on Data Analytics and Visualization.
MCA III Semester (Session 2026-2027) - COER University
"""

import os
import sys
import time

def run_project1():
    print("\n" + "#" * 70)
    print("# PROJECT 1: COVID-19 DATA ANALYSIS DASHBOARD")
    print("#" * 70)

    p1_src = os.path.abspath(os.path.join(os.path.dirname(__file__), "Project1_COVID19_Data_Analysis", "src"))
    sys.path.insert(0, p1_src)

    from eda_analysis import perform_covid_eda
    from dashboard import generate_covid_dashboard

    print("\n>>> Step 1.1: Performing Exploratory Data Analysis & KPI Calculation...")
    perform_covid_eda()

    print("\n>>> Step 1.2: Generating Visualizations & Executive Dashboard Screenshot...")
    generate_covid_dashboard()

    sys.path.pop(0)
    for mod in ["eda_analysis", "data_loader", "dashboard"]:
        if mod in sys.modules:
            del sys.modules[mod]


def run_project2():
    print("\n" + "#" * 70)
    print("# PROJECT 2: SALES DATA ANALYSIS DASHBOARD")
    print("#" * 70)

    p2_src = os.path.abspath(os.path.join(os.path.dirname(__file__), "Project2_Sales_Data_Analysis", "src"))
    sys.path.insert(0, p2_src)

    from eda_analysis import perform_sales_eda
    from dashboard import generate_sales_dashboard

    print("\n>>> Step 2.1: Performing Sales EDA & Business Financial Metrics...")
    perform_sales_eda()

    print("\n>>> Step 2.2: Generating Visualizations & Executive Sales Dashboard Screenshot...")
    generate_sales_dashboard()

    sys.path.pop(0)
    for mod in ["eda_analysis", "data_loader", "dashboard"]:
        if mod in sys.modules:
            del sys.modules[mod]


def main():
    total_start = time.time()
    print("=" * 70)
    print(" COER UNIVERSITY, ROORKEE - MCA III SEMESTER")
    print(" LAB SHEET-09: MINI PROJECTS ON DATA ANALYTICS & VISUALIZATION")
    print("=" * 70)

    run_project1()
    run_project2()

    total_time = time.time() - total_start
    print("\n" + "=" * 70)
    print(f" ALL DATASETS, VISUALIZATIONS & DASHBOARDS EXECUTED IN {total_time:.2f}s!")
    print(" Datasets in Excel form:     datasets/*.xlsx")
    print(" Dashboard Screenshots in:   */screenshots/*.png")
    print(" Interactive Dashboards in:  */outputs/*.html")
    print(" Comprehensive Docs in:      docs/")
    print("=" * 70)


if __name__ == "__main__":
    main()
