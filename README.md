# Mini Projects on Data Analytics and Visualization
### COER University, Roorkee, Uttarakhand
**Master of Computer Applications (MCA) — III Semester | Session 2026–2027**  
**Lab Sheet-09: Mini Projects on Data Analytics and Visualization**

[![Python Version](https://img.shields.io/badge/Python-3.11%2B-blue.svg)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-2.0%2B-navy.svg)](https://pandas.pydata.org/)
[![Plotly](https://img.shields.io/badge/Plotly-7.1.0-blueviolet.svg)](https://plotly.com/python/)
[![Excel](https://img.shields.io/badge/Datasets-Excel%20%28.xlsx%29-green.svg)](datasets/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## 📌 Executive Overview

This repository contains the complete implementation, datasets, interactive dashboards, high-resolution screenshots, and academic documentation for **Lab Sheet-09: Mini Projects on Data Analytics and Visualization** at COER University.

The repository encompasses two end-to-end analytical dashboard solutions:

1. **Project 1: COVID-19 Data Analysis Dashboard**
   - Analysis of global epidemiological time-series data across 12 countries over 36 months (2020–2022).
   - Missing value auditing and domain-specific proportional imputation.
   - Dual-axis epidemic wave curves (New Cases vs. New Deaths).
   - Country-wise comparative rankings, mortality rates (CFR), and vaccination rollout tracking.
   - High-resolution Executive Dashboard Screenshot and browser-based Interactive Plotly Dashboard.

2. **Project 2: Sales Data Analysis Dashboard**
   - Analysis of multi-regional retail and commercial transactions (5,000 orders spanning 2023–2025).
   - Missing value detection and mode/baseline imputation.
   - Monthly sales revenue and net operating profit progression analysis.
   - Customer segmentation (Consumer, Corporate, Home Office) and RFM profiling.
   - Product category and sub-category profitability analysis (identifying profit leaders vs. discount margin drain).
   - Regional distribution breakdown (West, East, Central, South).
   - High-resolution Executive Sales Dashboard Screenshot and browser-based Interactive Plotly Dashboard.

---

## 📋 Academic Submission Guidelines Compliance

| Mandatory Submission Requirement | Delivered Item & Location | Format |
|:---|:---|:---:|
| **1. Datasets in Excel Form** | [`datasets/covid_19_data.xlsx`](datasets/covid_19_data.xlsx)<br>[`datasets/sales_data.xlsx`](datasets/sales_data.xlsx) | Multi-Sheet `.xlsx` |
| **2. Datasets in CSV Form** | [`datasets/covid_19_data.csv`](datasets/covid_19_data.csv)<br>[`datasets/sales_data.csv`](datasets/sales_data.csv) | Standard `.csv` |
| **3. Dashboard Screenshots** | [`Project1_COVID19_Data_Analysis/screenshots/covid19_executive_dashboard.png`](Project1_COVID19_Data_Analysis/screenshots/covid19_executive_dashboard.png)<br>[`Project2_Sales_Data_Analysis/screenshots/sales_executive_dashboard.png`](Project2_Sales_Data_Analysis/screenshots/sales_executive_dashboard.png) | 300 DPI High-Res `.png` |
| **4. Source Code** | [`Project1_COVID19_Data_Analysis/src/`](Project1_COVID19_Data_Analysis/src/)<br>[`Project2_Sales_Data_Analysis/src/`](Project2_Sales_Data_Analysis/src/)<br>[`run_all.py`](run_all.py) | Modular Python Scripts |
| **5. Jupyter Notebooks** | [`Project1_COVID19_Data_Analysis/notebooks/`](Project1_COVID19_Data_Analysis/notebooks/)<br>[`Project2_Sales_Data_Analysis/notebooks/`](Project2_Sales_Data_Analysis/notebooks/) | Interactive `.ipynb` |
| **6. Academic Lab Report** | [`docs/Lab_Sheet_09_Report.md`](docs/Lab_Sheet_09_Report.md) | Full Academic Report |
| **7. Viva Preparation Guide** | [`docs/Viva_Questions_and_Answers.md`](docs/Viva_Questions_and_Answers.md) | 35+ Viva Q&A |

---

## 📊 Dashboard Visualizations & Screenshots

### 1. COVID-19 Executive Analytics Dashboard
![COVID-19 Executive Dashboard](Project1_COVID19_Data_Analysis/screenshots/covid19_executive_dashboard.png)

- **Interactive HTML Dashboard:** Open [`Project1_COVID19_Data_Analysis/outputs/covid_interactive_dashboard.html`](Project1_COVID19_Data_Analysis/outputs/covid_interactive_dashboard.html) in your browser.
- **Key Global Metrics:**
  - **Total Confirmed Infections:** 80,006,448
  - **Total Deaths:** 705,994 (CFR: 0.88%)
  - **Total Recovered:** 73,900,724 (Recovery Rate: 92.37%)
  - **Cumulative Vaccines Administered:** 4,682,484,804 doses

---

### 2. Commercial Sales & Retail Performance Dashboard
![Sales Executive Dashboard](Project2_Sales_Data_Analysis/screenshots/sales_executive_dashboard.png)

- **Interactive HTML Dashboard:** Open [`Project2_Sales_Data_Analysis/outputs/sales_interactive_dashboard.html`](Project2_Sales_Data_Analysis/outputs/sales_interactive_dashboard.html) in your browser.
- **Key Financial Metrics:**
  - **Total Commercial Revenue:** $11,220,417.57
  - **Net Operating Profit:** $700,155.23
  - **Overall Gross Margin:** 6.24%
  - **Average Order Value (AOV):** $2,244.08 (across 5,000 orders)

---

## 📂 Repository Structure

```
Mini-Projects-Data-Analytics-Visualization/
├── .gitignore
├── requirements.txt
├── README.md
├── LICENSE
├── run_all.py                                # Single-command runner for entire suite
├── generate_datasets.py                      # Dataset generator (Excel & CSV)
├── generate_notebooks.py                     # Jupyter Notebook builder
│
├── datasets/                                 # Datasets in Excel & CSV formats
│   ├── covid_19_data.xlsx                    # Multi-sheet Excel (Raw, Clean, Country, Timeline)
│   ├── covid_19_data.csv
│   ├── sales_data.xlsx                       # Multi-sheet Excel (Orders, Monthly, Segments, Products, Regions)
│   └── sales_data.csv
│
├── Project1_COVID19_Data_Analysis/
│   ├── src/
│   │   ├── __init__.py
│   │   ├── data_loader.py                    # Missing value audit, imputation & feature engineering
│   │   ├── eda_analysis.py                   # Statistical summaries & country rankings
│   │   └── dashboard.py                      # High-res charts, executive screenshot & HTML dashboard
│   ├── notebooks/
│   │   └── Project1_COVID19_Data_Analysis.ipynb
│   ├── outputs/
│   │   ├── covid_confirmed_vs_deaths.png
│   │   ├── covid_vaccination_trends.png
│   │   ├── covid_country_ranking.png
│   │   ├── covid_interactive_dashboard.html  # Interactive Plotly dashboard
│   │   └── covid_summary_metrics.json
│   └── screenshots/
│       └── covid19_executive_dashboard.png   # Submission Dashboard Screenshot
│
├── Project2_Sales_Data_Analysis/
│   ├── src/
│   │   ├── __init__.py
│   │   ├── data_loader.py                    # Missing value handling & business metrics
│   │   ├── eda_analysis.py                   # Monthly trends, RFM, product & regional profits
│   │   └── dashboard.py                      # High-res charts, executive screenshot & HTML dashboard
│   ├── notebooks/
│   │   └── Project2_Sales_Data_Analysis.ipynb
│   ├── outputs/
│   │   ├── monthly_sales_profit_trend.png
│   │   ├── customer_segmentation.png
│   │   ├── product_category_performance.png
│   │   ├── regional_sales_profit_distribution.png
│   │   ├── sales_interactive_dashboard.html  # Interactive Plotly dashboard
│   │   └── sales_summary_metrics.json
│   └── screenshots/
│       └── sales_executive_dashboard.png     # Submission Dashboard Screenshot
│
└── docs/
    ├── Lab_Sheet_09_Report.md                # Comprehensive Academic Lab Report
    ├── Viva_Questions_and_Answers.md         # 35+ Viva preparation Q&A for MCA examiners
    └── Business_Insights_and_Observations.md # Strategic business and public health insights
```

---

## ⚡ Quick Start Guide

### 1. Installation
Clone the repository and install required packages:

```bash
git clone https://github.com/Rajendra7637/Mini-Projects-Data-Analytics-and-Visualization.git
cd Mini-Projects-Data-Analytics-and-Visualization
pip install -r requirements.txt
```

### 2. Execute Entire Analytics Suite (Single Command)
Run the automated pipeline to process data, perform EDA, and generate all dashboards and screenshots:

```bash
python run_all.py
```

### 3. Open Interactive HTML Dashboards
Launch the interactive dashboards directly in your web browser:
- COVID-19 Dashboard: Open `Project1_COVID19_Data_Analysis/outputs/covid_interactive_dashboard.html`
- Sales Dashboard: Open `Project2_Sales_Data_Analysis/outputs/sales_interactive_dashboard.html`

### 4. Interactive Jupyter Notebooks
```bash
jupyter lab
```
Navigate to:
- `Project1_COVID19_Data_Analysis/notebooks/Project1_COVID19_Data_Analysis.ipynb`
- `Project2_Sales_Data_Analysis/notebooks/Project2_Sales_Data_Analysis.ipynb`

---

## 👨‍💻 Author & Attribution

- **Student / Developer:** Rajendra Singh ([@Rajendra7637](https://github.com/Rajendra7637))
- **Program:** Master of Computer Applications (MCA) – Semester III
- **Academic Session:** 2026–2027
- **Institution:** COER University, Roorkee, Uttarakhand, India
- **Coursework:** Lab Sheet-09 (Mini Projects on Data Analytics and Visualization)

---
*Licensed under the [MIT License](LICENSE).*
