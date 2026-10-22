# COER UNIVERSITY, ROORKEE, UTTARAKHAND
## Department of Computer Science & Applications
### MCA III Semester (Session 2026–2027)

---

# Lab Sheet-09: Mini Projects on Data Analytics and Visualization

- **Course:** Master of Computer Applications (MCA) – III Semester
- **Subject:** Data Analytics and Visualization Laboratory
- **Author / GitHub User:** Rajendra7637
- **Institution:** COER University, Roorkee-Haridwar Highway, Vardhmanpuram, Roorkee-247 667, District Haridwar, Uttarakhand, India

---

## 1. Laboratory Objectives

1. **Exploratory Data Analysis (EDA):** Perform systematic descriptive and inferential statistical exploration across public health and commercial enterprise domains.
2. **Missing Value Management:** Identify, audit, and impute missing data utilizing domain-appropriate imputation techniques without introducing bias.
3. **Data Visualization Principles:** Apply principles of effective visual communication (chart selection, color theory, readability, data-to-ink ratio) using **Pandas**, **NumPy**, **Matplotlib**, **Seaborn**, and **Plotly**.
4. **Interactive Dashboarding:** Construct multi-panel executive dashboard screenshots and browser-based interactive dashboards.
5. **Business & Epidemiological Intelligence:** Translate raw tabular data into strategic executive summaries, root-cause analyses, and decision-making insights.

---

## 2. Submission Compliance Checklist

| Submission Item | Required by Lab Sheet | File Location in Repository | Format / Verification |
|:---|:---:|:---|:---|
| **Datasets in Excel Form** | Yes | [`datasets/covid_19_data.xlsx`](file:///C:/Users/rajen/.gemini/antigravity/scratch/Mini-Projects-Data-Analytics-Visualization/datasets/covid_19_data.xlsx)<br>[`datasets/sales_data.xlsx`](file:///C:/Users/rajen/.gemini/antigravity/scratch/Mini-Projects-Data-Analytics-Visualization/datasets/sales_data.xlsx) | Multi-sheet Microsoft Excel (`.xlsx`) with raw, cleaned, and summary sheets |
| **Datasets in CSV Form** | Yes | [`datasets/covid_19_data.csv`](file:///C:/Users/rajen/.gemini/antigravity/scratch/Mini-Projects-Data-Analytics-Visualization/datasets/covid_19_data.csv)<br>[`datasets/sales_data.csv`](file:///C:/Users/rajen/.gemini/antigravity/scratch/Mini-Projects-Data-Analytics-Visualization/datasets/sales_data.csv) | Standard CSV |
| **Dashboard Screenshots** | Yes | [`Project1_COVID19_Data_Analysis/screenshots/covid19_executive_dashboard.png`](file:///C:/Users/rajen/.gemini/antigravity/scratch/Mini-Projects-Data-Analytics-Visualization/Project1_COVID19_Data_Analysis/screenshots/covid19_executive_dashboard.png)<br>[`Project2_Sales_Data_Analysis/screenshots/sales_executive_dashboard.png`](file:///C:/Users/rajen/.gemini/antigravity/scratch/Mini-Projects-Data-Analytics-Visualization/Project2_Sales_Data_Analysis/screenshots/sales_executive_dashboard.png) | 300 DPI Publication-grade composite dashboard screenshots |
| **Source Code** | Yes | [`Project1_COVID19_Data_Analysis/src/`](file:///C:/Users/rajen/.gemini/antigravity/scratch/Mini-Projects-Data-Analytics-Visualization/Project1_COVID19_Data_Analysis/src/)<br>[`Project2_Sales_Data_Analysis/src/`](file:///C:/Users/rajen/.gemini/antigravity/scratch/Mini-Projects-Data-Analytics-Visualization/Project2_Sales_Data_Analysis/src/)<br>[`run_all.py`](file:///C:/Users/rajen/.gemini/antigravity/scratch/Mini-Projects-Data-Analytics-Visualization/run_all.py) | Clean modular Python scripts + unified runner |
| **Jupyter Notebooks** | Yes | [`Project1_COVID19_Data_Analysis/notebooks/`](file:///C:/Users/rajen/.gemini/antigravity/scratch/Mini-Projects-Data-Analytics-Visualization/Project1_COVID19_Data_Analysis/notebooks/)<br>[`Project2_Sales_Data_Analysis/notebooks/`](file:///C:/Users/rajen/.gemini/antigravity/scratch/Mini-Projects-Data-Analytics-Visualization/Project2_Sales_Data_Analysis/notebooks/) | Fully executed interactive `.ipynb` notebooks |
| **Viva Guide & Documentation**| Yes | [`docs/Viva_Questions_and_Answers.md`](file:///C:/Users/rajen/.gemini/antigravity/scratch/Mini-Projects-Data-Analytics-Visualization/docs/Viva_Questions_and_Answers.md)<br>[`docs/Business_Insights_and_Observations.md`](file:///C:/Users/rajen/.gemini/antigravity/scratch/Mini-Projects-Data-Analytics-Visualization/docs/Business_Insights_and_Observations.md) | 35+ Viva Q&A + In-depth business reports |

---

## 3. Project 1: COVID-19 Data Analysis Dashboard

### 3.1 Dataset Description
The COVID-19 dataset models global epidemiology across 12 representative nations spanning North America, Europe, Asia, South America, and Africa over 36 continuous months (January 2020 to December 2022).
- **Primary Attributes:** Date, Country, Population, New_Cases, New_Deaths, New_Recovered, New_Vaccinated, Total_Cases, Total_Deaths, Total_Recovered, Total_Vaccinated.
- **Engineered Attributes:**
  - $\text{Active Cases} = \text{Total Cases} - (\text{Total Recovered} + \text{Total Deaths})$
  - $\text{Case Fatality Rate (CFR \%)} = \frac{\text{Total Deaths}}{\text{Total Cases}} \times 100$
  - $\text{Recovery Rate (\%)} = \frac{\text{Total Recovered}}{\text{Total Cases}} \times 100$
  - $\text{Vaccination Rate (\%)} = \frac{\text{Total Vaccinated}}{\text{Population}} \times 100$

### 3.2 Handling Missing Values
In historical epidemic surveillance, reporting discrepancies occur during weekend lags or prior to national vaccine authorizations:
1. `New_Recovered` (4% missing entries): Imputed using dynamic proportional estimation:
   $$\widehat{\text{New Recovered}} = \max(0, \text{New Cases} \times 0.95 - \text{New Deaths})$$
2. `New_Vaccinated` (3% missing entries / pre-vaccine period): Imputed logically with $0$ (representing periods prior to national vaccination rollouts).

### 3.3 Key Findings & Epidemiological Insights
- **Global Case & Death Burden:** Across the surveyed countries, **80,006,448** confirmed infections and **705,994** deaths were recorded, yielding an overall global Case Fatality Rate of **0.88%** and a recovery rate of **92.37%**.
- **Vaccination Decoupling Effect:** Over **4.68 Billion doses** were administered. Statistical correlation indicates a strong inverse relationship between cumulative vaccination coverage and CFR: once adult vaccination crossed $65\%$, mortality per 100,000 plummeted by over $78\%$, even during large case surges (Omicron wave).
- **Country Disparities:**
  - **India:** Largest absolute case count ($52.2\text{M}$) and highest recovery volume ($48.3\text{M}$), supported by high-volume domestic vaccine administration ($2.2\text{B}$ doses).
  - **United States:** Highest per-capita reported case ascertainment ($12.8\text{M}$ cases, $113.4\text{K}$ deaths).
  - **Brazil & Russia:** Displayed higher initial CFR ($1.51\%$ and $1.56\%$) due to delayed public health interventions in early waves.

---

## 4. Project 2: Sales Data Analysis Dashboard

### 4.1 Dataset Description
The Sales dataset models a multi-regional retail and commercial enterprise spanning 5,000 transactions across 800 unique customers from 2023 to 2025.
- **Transactional Attributes:** Order ID, Order Date, Ship Date, Ship Mode, Customer ID, Segment, Country, Region, State, Category, Sub-Category, Sales, Quantity, Discount, Profit.
- **Engineered Attributes:**
  - $\text{Profit Margin (\%)} = \frac{\text{Profit}}{\text{Sales}} \times 100$
  - $\text{Average Order Value (AOV)} = \frac{\text{Total Sales}}{\text{Total Orders}}$
  - $\text{Shipping Duration (Days)} = \text{Ship Date} - \text{Order Date}$

### 4.2 Handling Missing Values
1. `Discount` (3% missing values): Imputed with $0.0$ baseline (standard non-discounted catalog price).
2. `Ship_Mode` (2% missing values): Imputed using mode imputation (`"Standard Class"` representing 60% of all deliveries).

### 4.3 Key Business Insights & Financial Metrics
- **Executive Performance:** Total Revenue reached **$11,220,417.57** with Net Profit of **$700,155.23**, representing an overall gross margin of **6.24%** and an Average Order Value (AOV) of **$2,244.08**.
- **Customer Segmentation:**
  - **Consumer Segment:** Generates the largest revenue share (**52.4%**, ~$5.88M), driving high sales velocity.
  - **Corporate Segment:** Contributes **29.8%** of revenue with the highest average transaction value.
  - **Home Office Segment:** Accounts for **17.8%**, exhibiting consistent repeat purchases.
- **Product Category Profitability:**
  - **Technology:** Most profitable category, led by Copiers ($+30\%$ margin) and Accessories ($+35\%$ margin).
  - **Furniture:** Suffers from severe margin erosion due to over-discounting on Tables ($-8\%$ margin) and Bookcases ($-5\%$ margin).
  - **Office Supplies:** Generates steady high-margin cash flow (Paper: $+42\%$, Binders: $+38\%$).
- **Regional Performance:**
  - **West Region:** Highest sales volume ($32\%$) and healthy margins.
  - **East Region:** Second largest contributor ($28\%$).
  - **Central & South Regions:** Experience higher shipping friction and discount pressures, requiring regional pricing adjustments.

---

## 5. Visual Dashboard Screenshots

High-resolution composite executive dashboards (300 DPI) were generated and saved for academic review:
1. **COVID-19 Executive Dashboard:** [`Project1_COVID19_Data_Analysis/screenshots/covid19_executive_dashboard.png`](file:///C:/Users/rajen/.gemini/antigravity/scratch/Mini-Projects-Data-Analytics-Visualization/Project1_COVID19_Data_Analysis/screenshots/covid19_executive_dashboard.png)
2. **Sales Performance Dashboard:** [`Project2_Sales_Data_Analysis/screenshots/sales_executive_dashboard.png`](file:///C:/Users/rajen/.gemini/antigravity/scratch/Mini-Projects-Data-Analytics-Visualization/Project2_Sales_Data_Analysis/screenshots/sales_executive_dashboard.png)

Both projects also generated fully interactive browser dashboards:
- [`outputs/covid_interactive_dashboard.html`](file:///C:/Users/rajen/.gemini/antigravity/scratch/Mini-Projects-Data-Analytics-Visualization/Project1_COVID19_Data_Analysis/outputs/covid_interactive_dashboard.html)
- [`outputs/sales_interactive_dashboard.html`](file:///C:/Users/rajen/.gemini/antigravity/scratch/Mini-Projects-Data-Analytics-Visualization/Project2_Sales_Data_Analysis/outputs/sales_interactive_dashboard.html)
