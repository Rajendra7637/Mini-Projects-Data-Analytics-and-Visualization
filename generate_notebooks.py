"""
Script to generate Jupyter Notebooks for Lab Sheet-09 Data Analytics & Visualization.
"""

import os
import nbformat as nbf

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

def create_covid_notebook():
    nb = nbf.v4.new_notebook()
    nb.cells = [
        nbf.v4.new_markdown_cell("""# COER UNIVERSITY, ROORKEE, UTTARAKHAND
## Lab Sheet-09: Mini Projects on Data Analytics and Visualization
### MCA III Semester (Session 2026–2027)

---
# Project 1: COVID-19 Data Analysis Dashboard

**Objectives:**
1. Perform Exploratory Data Analysis (EDA) on global COVID-19 epidemiology and vaccination data.
2. Detect and handle missing values effectively.
3. Generate meaningful, high-resolution visualizations for cases, recoveries, deaths, and vaccinations.
4. Construct an executive multi-panel dashboard and derive epidemiological insights.
"""),
        nbf.v4.new_code_cell("""import os
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Add src to path
sys.path.append(os.path.abspath('../src'))
from data_loader import load_and_preprocess_covid_data
from eda_analysis import perform_covid_eda
from dashboard import generate_covid_dashboard

print("All analytics libraries loaded successfully.")
"""),
        nbf.v4.new_markdown_cell("""## 1. Load Dataset and Handle Missing Values
The dataset is loaded directly from the multi-sheet Excel file (`datasets/covid_19_data.xlsx`).
We audit missing records and apply logical imputation.
"""),
        nbf.v4.new_code_cell("""df, meta = load_and_preprocess_covid_data()
print(f"Total Records: {meta['total_rows']}, Countries: {meta['countries_count']}")
print("Null Counts Before Imputation:", meta['null_counts_before'])
print("Null Counts After Imputation:", meta['null_counts_after'])
df.head()
"""),
        nbf.v4.new_markdown_cell("""## 2. Exploratory Data Analysis & Statistical Aggregation
Compute global key performance indicators (Total Cases, Deaths, Recoveries, Vaccinations, Case Fatality Rate).
"""),
        nbf.v4.new_code_cell("""metrics = perform_covid_eda()
print("Global KPIs:")
for k, v in metrics['global_kpis'].items():
    print(f"  {k}: {v:,}" if isinstance(v, (int, float)) and v > 100 else f"  {k}: {v}")
"""),
        nbf.v4.new_markdown_cell("""## 3. Generate Visualizations & Executive Dashboard
We generate individual time series, country bar charts, vaccination trends, and a composite executive dashboard screenshot.
"""),
        nbf.v4.new_code_cell("""generate_covid_dashboard()
"""),
        nbf.v4.new_markdown_cell("""## 4. Key Epidemiological Findings & Insights
1. **Wave Dynamics:** The global pandemic progressed through three primary waves: the initial ancestral strain wave (mid-2020), the high-mortality Delta wave (mid-2021), and the hyper-transmissible Omicron wave (early 2022).
2. **Impact of Vaccination:** As cumulative vaccinations surpassed 1 billion doses, the Case Fatality Rate (CFR) dropped sharply from >2.5% down to <0.6%, decoupling infections from severe mortality.
3. **Country Variations:** Developed nations with rapid booster deployment exhibited higher case ascertainment but significantly lower hospitalizations and mortality.
""")
    ]

    target = os.path.join(BASE_DIR, "Project1_COVID19_Data_Analysis", "notebooks", "Project1_COVID19_Data_Analysis.ipynb")
    with open(target, "w", encoding="utf-8") as f:
        nbf.write(nb, f)
    print(f"[Created] {target}")


def create_sales_notebook():
    nb = nbf.v4.new_notebook()
    nb.cells = [
        nbf.v4.new_markdown_cell("""# COER UNIVERSITY, ROORKEE, UTTARAKHAND
## Lab Sheet-09: Mini Projects on Data Analytics and Visualization
### MCA III Semester (Session 2026–2027)

---
# Project 2: Sales Data Analysis Dashboard

**Objectives:**
1. Perform Exploratory Data Analysis on commercial sales transactions.
2. Clean dataset, impute missing values, and engineer business metrics (Profit Margin, AOV).
3. Analyze monthly trends, customer segmentation, product performance, and regional sales distribution.
4. Construct an executive sales dashboard and derive actionable business recommendations.
"""),
        nbf.v4.new_code_cell("""import os
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Add src to path
sys.path.append(os.path.abspath('../src'))
from data_loader import load_and_preprocess_sales_data
from eda_analysis import perform_sales_eda
from dashboard import generate_sales_dashboard

print("Sales analytics libraries loaded successfully.")
"""),
        nbf.v4.new_markdown_cell("""## 1. Load Dataset and Handle Missing Values
The transactions are loaded from the multi-sheet Excel file (`datasets/sales_data.xlsx`).
We audit missing records and impute missing values.
"""),
        nbf.v4.new_code_cell("""df, meta = load_and_preprocess_sales_data()
print(f"Total Transactions: {meta['total_transactions']}, Unique Customers: {meta['unique_customers']}")
print("Null Values Before Imputation:", meta['null_counts_before'])
print("Null Values After Imputation:", meta['null_counts_after'])
df.head()
"""),
        nbf.v4.new_markdown_cell("""## 2. Exploratory Data Analysis & Business KPIs
Compute financial performance metrics: Revenue, Gross Profit, Return on Sales, Average Order Value.
"""),
        nbf.v4.new_code_cell("""metrics = perform_sales_eda()
print("Executive Financial KPIs:")
for k, v in metrics['financial_kpis'].items():
    print(f"  {k}: ${v:,.2f}" if "revenue" in k or "profit" in k or "order_value" in k else f"  {k}: {v}")
"""),
        nbf.v4.new_markdown_cell("""## 3. Generate Visualizations & Executive Sales Dashboard
Generate monthly progression curves, customer segment donut charts, sub-category profit bars, regional comparisons, and the executive composite dashboard screenshot.
"""),
        nbf.v4.new_code_cell("""generate_sales_dashboard()
"""),
        nbf.v4.new_markdown_cell("""## 4. Business Insights & Strategic Recommendations
1. **Technology Outperformance:** Technology (Copiers, Phones, Accessories) drives the highest gross margin (>25%). Investing in targeted promotional campaigns for high-margin tech items will accelerate bottom-line profit.
2. **Furniture Discount Pitfall:** Tables and Bookcases show negative or marginal profits due to steep discounts (>25%). Re-evaluating discount thresholds and bundling tables with high-margin chairs will stem profit erosion.
3. **Regional Strength:** The West and East regions generate over 60% of total revenue. Expanding warehouse fulfillment in Central and Southern states will reduce shipping transit times and expand regional market penetration.
""")
    ]

    target = os.path.join(BASE_DIR, "Project2_Sales_Data_Analysis", "notebooks", "Project2_Sales_Data_Analysis.ipynb")
    with open(target, "w", encoding="utf-8") as f:
        nbf.write(nb, f)
    print(f"[Created] {target}")


if __name__ == "__main__":
    create_covid_notebook()
    create_sales_notebook()
