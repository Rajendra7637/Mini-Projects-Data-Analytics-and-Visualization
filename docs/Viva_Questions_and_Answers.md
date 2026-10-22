# Comprehensive Viva Questions and Answers
## Lab Sheet-09: Mini Projects on Data Analytics and Visualization
### MCA III Semester (Session 2026–2027) — COER University

---

## Part A: Data Analytics & Exploratory Data Analysis (EDA)

### Q1: What is Exploratory Data Analysis (EDA) and why is it essential?
**Answer:** Exploratory Data Analysis (EDA), pioneered by John Tukey, is an analytical approach to analyzing datasets to summarize their main statistical characteristics, discover underlying patterns, detect anomalies and outliers, test hypotheses, and verify assumptions using both numerical summaries and graphical representations. EDA is essential because:
1. It reveals data distribution, skewness, and kurtosis.
2. It detects data quality defects (missing values, typos, invalid dates, outliers).
3. It guides appropriate feature engineering and machine learning model selection.

---

### Q2: What are the primary types of missing data mechanisms?
**Answer:** Donald Rubin defined three fundamental missing data mechanisms:
1. **Missing Completely at Random (MCAR):** The probability of missingness is completely independent of both observed and unobserved data (e.g., a lab technician accidentally dropping a test tube).
2. **Missing at Random (MAR):** The missingness is systematically related to other observed variables, but not the missing value itself (e.g., younger individuals being less likely to report blood pressure).
3. **Missing Not at Random (MNAR):** The probability of missingness depends directly on the unobserved value itself (e.g., high-income individuals refusing to disclose their salary).

---

### Q3: What strategies are available to handle missing values, and how did you select your approach?
**Answer:**
- **Deletion (Listwise/Pairwise):** Dropping rows/columns with nulls. Simple, but discards valuable sample size and introduces selection bias if data is not MCAR.
- **Mean / Median Imputation:** Imputing central tendency. Fast, but underestimates standard deviation and distorts variable distributions. Median is preferred for skewed data.
- **Mode Imputation:** Applied to categorical features (e.g., imputing missing `Ship_Mode` with `"Standard Class"`).
- **Logical / Domain-Specific Imputation:** In our COVID-19 dataset, missing early vaccination counts were imputed with $0$ because vaccinations had not yet commenced. Missing recoveries were imputed using the domain epidemiological equation:
  $$\widehat{\text{Recovered}} = \max(0, \text{New Cases} \times 0.95 - \text{New Deaths})$$

---

### Q4: Explain the difference between Descriptive, Diagnostic, Predictive, and Prescriptive Analytics.
**Answer:**
- **Descriptive Analytics ("What happened?"):** Summarizes historical performance through aggregations, KPIs, and reports (e.g., Total Sales in 2024 = $3.8M).
- **Diagnostic Analytics ("Why did it happen?"):** Discovers root causes and correlations (e.g., Why did furniture profit decline? High discount rates on Tables).
- **Predictive Analytics ("What will happen?"):** Uses historical patterns and statistical/machine learning models to forecast future trajectories (e.g., ARIMA forecasting COVID wave peaks).
- **Prescriptive Analytics ("What should we do?"):** Recommends optimal actions and business policies using optimization and decision theory (e.g., Dynamic pricing caps on tables to eliminate profit loss).

---

### Q5: What is RFM (Recency, Frequency, Monetary) Customer Segmentation?
**Answer:** RFM is a proven behavioral segmentation framework:
- **Recency (R):** How recently did the customer make a purchase? (Lower days = higher engagement).
- **Frequency (F):** How often do they purchase within a given time frame? (Higher orders = greater brand loyalty).
- **Monetary Value (M):** How much total revenue do they generate? (Higher spend = higher customer lifetime value).  
Customers are scored into quintiles (1-5) on each dimension to segment them into Champions, Loyal Customers, At Risk, or Churned.

---

## Part B: Data Visualization Principles & Python Libraries

### Q6: What principles govern effective chart selection?
**Answer:**
1. **Time-Series / Trends:** Line charts (e.g., Monthly Sales and Epidemic Wave Progression).
2. **Part-to-Whole Relationships:** Donut or Stacked Bar charts (e.g., Customer Segment Share), limited to 3-5 categories.
3. **Discrete Category Comparison:** Bar charts / Horizontal bar charts (e.g., Top 10 Countries by Cases; Product Sub-Categories). Horizontal orientation is preferred when category labels are long to prevent tilted, illegible text.
4. **Multivariate Distribution & Correlation:** Heatmaps (e.g., Feature Correlation Matrix, Regional Sales vs Profit matrices).
5. **Distribution & Outlier Detection:** Box plots, Violin plots, or Histograms with KDE.

---

### Q7: Explain Edward Tufte's concept of the "Data-to-Ink Ratio".
**Answer:** Tufte defines the Data-to-Ink Ratio as:
$$\text{Data-to-Ink Ratio} = \frac{\text{Data-Ink}}{\text{Total ink used to print the graphic}}$$
Good visualization design maximizes this ratio by eliminating **chartjunk**—unnecessary 3D effects, excessive gridlines, heavy borders, redundant labels, and ornamental backgrounds—allowing the viewer's cognitive focus to remain entirely on the empirical data trends.

---

### Q8: Contrast Matplotlib, Seaborn, and Plotly.
**Answer:**
- **Matplotlib:** The foundational low-level plotting library in Python. Highly customizable and granular (control over every spine, tick, artist, and grid), but verbose.
- **Seaborn:** A high-level statistical visualization library built on top of Matplotlib. Provides elegant default themes, native Pandas DataFrame integration, and built-in statistical estimators (regressions, heatmaps, violin plots).
- **Plotly:** A modern web-based declarative visualization library built on JavaScript (`plotly.js`). Generates rich, fully interactive charts supporting pan, zoom, hover tooltips, and interactive filtering out-of-the-box in standalone HTML files.

---

### Q9: Why is a dual-axis chart used, and what precautions must be taken?
**Answer:** A dual-axis (or twin-x) chart plots two variables sharing the same horizontal axis (e.g., Date) but having drastically different vertical scales or units (e.g., Millions of Cases on the primary axis vs. Thousands of Deaths on the secondary axis).  
**Precautions:**
- Always use distinctly colored lines and match the color of each y-axis label to its corresponding series.
- Clearly label axis units (e.g., Millions vs. Thousands) so viewers do not misinterpret raw magnitudes.

---

### Q10: How did you calculate Case Fatality Rate (CFR) and what is the difference between CFR and Infection Fatality Rate (IFR)?
**Answer:**
- **Case Fatality Rate (CFR):**
  $$\text{CFR} = \frac{\text{Confirmed Deaths}}{\text{Confirmed Cases}} \times 100\%$$
- **Infection Fatality Rate (IFR):**
  $$\text{IFR} = \frac{\text{Total Deaths}}{\text{Total Actual Infections (including asymptomatic/untested)}} \times 100\%$$
Because many mild or asymptomatic cases are never formally tested or reported, Confirmed Cases $<$ Total Infections. Therefore, CFR is always higher than IFR.

---

### Q11: What business recommendations did you draw from the Sales Analysis Dashboard?
**Answer:**
1. **Mitigate Furniture Margin Drag:** Sub-categories such as Tables and Bookcases operate at negative or near-zero profit margins due to excessive discounts (>25%). The business should cap discounts on tables at 15% and bundle tables with high-margin chairs.
2. **Double Down on Technology:** Copiers and Accessories deliver gross margins exceeding 30%. Reallocating marketing expenditure toward corporate technology procurement will maximize net profit.
3. **Logistics Optimization in Central Region:** Central region sales deliver lower profit margins due to higher shipping costs. Consolidating regional distribution hubs will lower freight friction.
