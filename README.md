# 💳 Unite 2 Project Credit Card Customer Churn Analysis & Predictive Intelligence

## 01. Executive Summary & Business Problem
### Project Overview
The Credit Card Customer Churn Analysis is an end-to-end data science and business intelligence solution built on a dataset of 10,127 bank customers (`BankChurners.csv`). It integrates a Python-based ETL and exploratory data analysis pipeline (`Pandas`, `NumPy`, `Seaborn`), supervised machine learning classification models (`Scikit-Learn`), and an interactive multi-page executive dashboard hosted on Tableau Public.

### Business Problem
In retail banking, acquiring a new credit cardholder costs up to five times more than retaining an existing one. Banks frequently suffer silent attrition, losing high-value accounts due to undetected customer dissatisfaction or prolonged inactivity. Traditional reporting reacts after account closure; this project shifts the paradigm to proactive, predictive risk mitigation.

### Strategic Value & Impact
- Early Risk Visibility: Identifies leading behavioral indicators—such as critical thresholds in `Months_Inactive_12_mon` and descending transaction volume tiers.
- Data-Driven Retention Strategy: Equips retention specialists with targeted insights to deploy personalized incentives or credit limit adjustments prior to cancellation.
- Measurable ROI: Minimizes portfolio revenue leakage, preserves customer lifetime value (LTV), and focuses retention spend strictly on high-propensity churn segments.

## 02. Business Requirements & User Personas
To deliver actionable business intelligence, this project addresses two core operational personas:

1. Portfolio Managers & Risk Analysts:
   - Require automated tracking of key behavioral and financial metrics (credit limits, revolving balances, utilization rates) to monitor baseline portfolio health.
   - Need clear data structures and exploratory visual distributions to identify vulnerable demographic and income segments early.
2. Customer Retention Teams:
   - Require predictive customer segmentation (via classification models like Random Forest and Decision Tree) to detect high-risk accounts before cancellation.
   - Need actionable insights into primary churn drivers (low transaction frequency and decreasing 12-month engagement) to launch targeted retention campaigns.

## 03. Dataset Content & Hygiene
- Source & File Location: Sourced from public educational repositories as `BankChurners.csv`, isolated in `data/raw/` and exported clean to `data/processed/cleaned_bank_churners.csv`.
- Dimensions: 10,127 customer records and 23 features, optimized for rapid local computation and repository compliance.
- Pillars of Analysis:
  - Demographics & Geography: Customer Age, Gender, Dependent Count, Education Level, Marital Status, Income Category.
  - Financial Attributes: Credit Limit, Total Revolving Balance, Open-to-Buy Credit (`Avg_Open_To_Buy`), Average Utilization Ratio (`Avg_Utilization_Ratio`).
  - Transactional Activity: Total Transaction Amount (`Total_Trans_Amt`), Total Transaction Count (`Total_Trans_Ct`), Total Relationship Count, Months on Book, Inactive Months (`Months_Inactive_12_mon`).
  - Target Variable: `Attrition_Flag` (engineered into binary `Churn`: `1` = Attrited, `0` = Existing).

## 04. Core Hypotheses & Statistical Validation
- Hypothesis 1 (Inactivity Duration & Attrition):
  - Statement: Customers with prolonged inactivity (3+ months in a 12-month period) exhibit significantly higher attrition rates.
  - Validation: Confirmed through exploratory distribution plots and feature ranking; `Months_Inactive_12_mon` emerged as a top predictor of cancellation.
- Hypothesis 2 (Transaction Velocity & Retention):
  - Statement: Lower total transaction amounts and transaction counts over 12 months strongly correlate with customer churn.
  - Validation: Confirmed via comparative box plots and Tableau transactional trend analysis showing churned accounts heavily clustering in lower volume tiers.
- Hypothesis 3 (Revolving Balances & Product Engagement):
  - Statement: Cardholders maintaining lower revolving balances and utilization ratios have a higher propensity to churn due to low engagement.
  - Validation: Confirmed via financial metric EDA; active cardholders maintain substantially higher revolving balances than attrited customers.

## 05. Data Management, Cleaning & ETL Pipeline
1. Environment Configuration: Built within a reproducible Python 3.12.8 virtual environment (`.venv`) with pinned dependencies in `requirements.txt`.
2. Artifact & Metadata Removal: Dropped redundant Kaggle naive Bayes classifier trailing columns and index identifiers.
3. Integrity Verification: Audited for missing values (`df.isnull().sum()`) and confirmed zero duplicate records across all 10,127 rows.
4. Feature Encoding & Preprocessing: Encoded binary target variables, standardized continuous numeric columns, and implemented stratified train-test splitting (`stratify=y`) to handle class distribution.

### Project Management & Version Control
This project followed Agile methodologies managed via GitHub Projects:
- Project Board: [View Live Agile Project Board](https://github.com/users/resmiepalova/projects/YOUR_PROJECT_BOARD_NUMBER)
- Source Code Repository: [View GitHub Source Code](https://github.com/resmiepalova/unite-1-credit-card-customer-churn-analysis)

## 06. Technical Analysis & Machine Learning Evaluation
### Methodology & Alternatives
Exploratory Data Analysis (EDA) was executed in `notebooks/01_etl_and_eda.ipynb` using descriptive statistics and visual plots exported directly to `docs/screenshots/`. Machine learning classification was executed in `notebooks/02_machine_learning.ipynb`. While Logistic Regression provided a solid linear baseline, ensemble tree-based models (Random Forest) were implemented to handle non-linear interactions across financial metrics.

### Model Performance Summary (80/20 Stratified Split)
| Model | Accuracy | ROC-AUC Score | Primary Advantage |
| :--- | :---: | :---: | :--- |
| Random Forest Classifier | 94.47% | 97.91% | Superior handling of non-linear financial interactions and resistance to overfitting. |
| Decision Tree Classifier | 93.14% | 94.69% | High interpretability with explicit decision rules for business stakeholders. |
| Logistic Regression | 89.98% | 91.26% | Robust, mathematically sound linear baseline utilizing feature scaling. |

## 07. Business Requirements to Data Visualizations Mapping
To ensure technical outputs directly support business users, requirements were explicitly mapped to visual assets:

1. Portfolio Health & Demographics Tracking (Requirement 1):
   - Mapping: Demographic histograms (`customer_age_distribution.png`) and Education vs. Churn matrices map directly to monitoring baseline portfolio demographics.
2. Financial Risk & Utilization Monitoring (Requirement 1):
   - Mapping: Credit Limit and Revolving Balance box plots (`credit_limit_by_attrition.png`) highlight financial thresholds where account closure accelerates.
3. Proactive Customer Retention Campaigns (Requirement 2):
   - Mapping: Transaction amount and count distribution plots (`total_transaction_amount_distribution.png`) visually indicate falling transaction velocity, triggering retention outreach.

## 08. Executive Dashboard Architecture (Tableau Public)
The interactive Executive Dashboard was deployed to Tableau Public for secure, browser-based stakeholder access without local installation requirements:

- 🔗 Live Dashboard Link: [View Interactive Tableau Public Dashboard](https://public.tableau.com/app/profile/resmie.palova8392/viz/Credit_Card_Churn_Analysis/Dashboard1?publish=yes)

### Dashboard Page Breakdown
- Page 1: Portfolio Overview & Demographics: High-level KPI cards (Total Customers, Churn Rate), demographic distribution histograms (Age, Gender), and Education Level risk matrices.
- Page 2: Financial Exposure & Behavioral Metrics: Income Category distribution charts, Credit Limit box plots, Marital Status breakdowns, and 12-Month Inactive Duration analysis.
- Page 3: Transactional Performance & Volume Trends:** Card Category performance indicators, behavioral trend line charts, and Total Transaction Amount vs. Count scatter plots.

## 09. Key Findings & Business Conclusions
- Inactive Duration: 3 or more inactive months within a 12-month period serves as a critical operational tipping point for customer churn.
- Transaction Volume: Transaction count and transaction amount are the strongest statistical predictors of customer retention; low-frequency users should be targeted for re-engagement.
- Revolving Balances: Customers with zero or minimal revolving balances exhibit significantly higher churn rates than actively utilizing cardholders.

## 10. Data Governance, Ethics & Limitations
- Privacy & Compliance: `BankChurners.csv` contains anonymized banking records free of Personally Identifiable Information (PII) such as customer names or account numbers.
- Algorithmic Fairness: Explored demographic variables to ensure predictive retention models do not apply biased scoring based on age or gender.
- Class Imbalance Management: Addressed the natural imbalance of churn datasets by utilizing stratified train-test splitting (`stratify=y`) and evaluating models using ROC-AUC, precision, and recall alongside raw accuracy.

## 📌 Project Resources & Quick Links
- 📁 GitHub Repository: [Unit 2 Project Repository](https://github.com/resmiepalova/unite-1-credit-card-customer-churn-analysis)
- 📋 GitHub Project Board: [Unit 2 Agile Project Board](https://github.com/users/resmiepalova/projects/YOUR_PROJECT_BOARD_NUMBER)
- 📊 Interactive Dashboard: [View Interactive Tableau Public Dashboard](https://public.tableau.com/app/profile/resmie.palova8392/viz/Credit_Card_Churn_Analysis/Dashboard1?publish=yes)

## 11. Unfixed Bugs & Troubleshooting
- Codebase & Pipeline Integrity: No critical bugs, execution errors, or data pipeline blockers exist within the repository.
- Tableau Interactions: Minor visual filter resets on secondary dashboard cards were noted during browser testing but do not affect data accuracy or analytical conclusions.

## 12. Local Setup & Execution Guide
1. Clone the Repository:
   ```bash
   git clone [https://github.com/resmie-palova/Credit_Card_Churn_Analysis.git](https://github.com/resmie-palova/Credit_Card_Churn_Analysis.git)
   cd Credit_Card_Churn_Analysis
