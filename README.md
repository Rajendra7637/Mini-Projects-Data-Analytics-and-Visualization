# Mini Projects on Data Analytics and Visualization
### Rajendra Singh Bisht Master of Computer Applications (MCA) — III Semester | Session 2026–2027
**Lab Sheet-09: Mini Projects on Data Analytics and Visualization**

[![Python Version](https://img.shields.io/badge/Python-3.11%2B-blue.svg)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-2.0%2B-navy.svg)](https://pandas.pydata.org/)
[![Plotly](https://img.shields.io/badge/Plotly-7.1.0-blueviolet.svg)](https://plotly.com/python/)
[![Excel Datasets](https://img.shields.io/badge/Datasets-Excel%20%28.xlsx%29-green.svg)](datasets/)

---

## 📌 Executive Overview

This repository contains the complete implementation, datasets in Excel format, high-resolution dashboard screenshots, interactive web dashboards, and source code for **Lab Sheet-09: Mini Projects on Data Analytics and Visualization**.

The repository comprises two end-to-end analytical projects:

1. **Project 1: COVID-19 Data Analysis Dashboard**
   - Comprehensive analysis of global epidemiological time-series data across 12 countries over 36 months (2020–2022).
   - Missing value auditing and proportional domain-specific imputation.
   - Dual-axis epidemic wave curves (New Cases vs. New Deaths).
   - Country-wise comparative rankings, mortality rates (Case Fatality Rate - CFR), and vaccination rollout tracking.
   - High-resolution Executive Dashboard Screenshot and browser-based Interactive Plotly Dashboard.

2. **Project 2: Sales Data Analysis Dashboard**
   - Analysis of multi-regional commercial sales transactions (5,000 orders spanning 2023–2025).
   - Missing value detection and mode/baseline imputation.
   - Monthly sales revenue and net operating profit progression analysis.
   - Customer segmentation (Consumer, Corporate, Home Office).
   - Product category and sub-category profitability analysis (identifying profit leaders vs. loss leaders).
   - Regional distribution breakdown (West, East, Central, South).
   - High-resolution Executive Sales Dashboard Screenshot and browser-based Interactive Plotly Dashboard.

---

## 📋 Submission Guidelines Compliance Checklist

| Mandatory Submission Requirement | Delivered Repository Asset | Format & Description |
|:---|:---|:---:|
| **1. Datasets in Excel Form** | [`datasets/covid_19_data.xlsx`](datasets/covid_19_data.xlsx)<br>[`datasets/sales_data.xlsx`](datasets/sales_data.xlsx) | **Multi-Sheet Microsoft Excel (`.xlsx`)** workbooks with raw data, cleaned data, and multi-dimensional summary sheets. |
| **2. Datasets in CSV Form** | [`datasets/covid_19_data.csv`](datasets/covid_19_data.csv)<br>[`datasets/sales_data.csv`](datasets/sales_data.csv) | Standard `.csv` |
| **3. Dashboard Screenshots** | [`Project1_COVID19_Data_Analysis/screenshots/covid19_executive_dashboard.png`](Project1_COVID19_Data_Analysis/screenshots/covid19_executive_dashboard.png)<br>[`Project2_Sales_Data_Analysis/screenshots/sales_executive_dashboard.png`](Project2_Sales_Data_Analysis/screenshots/sales_executive_dashboard.png) | **300 DPI High-Resolution Executive Dashboard Screenshots** |
| **4. Source Code** | [`Project1_COVID19_Data_Analysis/src/`](Project1_COVID19_Data_Analysis/src/)<br>[`Project2_Sales_Data_Analysis/src/`](Project2_Sales_Data_Analysis/src/) | Modular Python Scripts (Data loader, EDA, Dashboard generator) |
| **5. Interactive Web Dashboards** | [`Project1_COVID19_Data_Analysis/outputs/covid_interactive_dashboard.html`](Project1_COVID19_Data_Analysis/outputs/covid_interactive_dashboard.html)<br>[`Project2_Sales_Data_Analysis/outputs/sales_interactive_dashboard.html`](Project2_Sales_Data_Analysis/outputs/sales_interactive_dashboard.html) | Standalone interactive **Plotly HTML dashboards** with tooltips and zooming |
| **6. Jupyter Notebooks** | [`Project1_COVID19_Data_Analysis/notebooks/Project1_COVID19_Data_Analysis.ipynb`](Project1_COVID19_Data_Analysis/notebooks/Project1_COVID19_Data_Analysis.ipynb)<br>[`Project2_Sales_Data_Analysis/notebooks/Project2_Sales_Data_Analysis.ipynb`](Project2_Sales_Data_Analysis/notebooks/Project2_Sales_Data_Analysis.ipynb) | Interactive step-by-step `.ipynb` notebooks |

---

## 📊 Dashboard Visualizations & Screenshots

### 1. COVID-19 Executive Analytics Dashboard
![COVID-19 Executive Dashboard](Project1_COVID19_Data_Analysis/screenshots/covid19_executive_dashboard.png)

- **Interactive HTML Dashboard:** Open [`Project1_COVID19_Data_Analysis/outputs/covid_interactive_dashboard.html`](Project1_COVID19_Data_Analysis/outputs/covid_interactive_dashboard.html) in any browser.
- **Key Global Epidemiological Metrics:**
  - **Total Confirmed Infections:** 80,006,448
  - **Total Deaths:** 705,994 (Global CFR: 0.88%)
  - **Total Recovered:** 73,900,724 (Global Recovery Rate: 92.37%)
  - **Cumulative Vaccines Administered:** 4,682,484,804 doses

---

### 2. Commercial Sales & Retail Performance Dashboard
![Sales Executive Dashboard](Project2_Sales_Data_Analysis/screenshots/sales_executive_dashboard.png)

- **Interactive HTML Dashboard:** Open [`Project2_Sales_Data_Analysis/outputs/sales_interactive_dashboard.html`](Project2_Sales_Data_Analysis/outputs/sales_interactive_dashboard.html) in any browser.
- **Key Financial Metrics:**
  - **Total Commercial Revenue:** $11,220,417.57
  - **Net Operating Profit:** $700,155.23
  - **Overall Gross Margin:** 6.24%
  - **Average Order Value (AOV):** $2,244.08 (across 5,000 orders)

---


