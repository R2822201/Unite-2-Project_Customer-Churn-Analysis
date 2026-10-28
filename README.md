
💳 Credit Card Customer Churn Analysis & Predictive Intelligence

01. Project Presentation & Executive Summary

What is it?

The Credit Card Customer Churn Analysis is an end-to-end data science and business intelligence solution built on a comprehensive dataset of 10,127 bank customers (BankChurners.csv). It integrates a rigorous Python-based ETL and exploratory data analysis pipeline (Pandas, NumPy, Seaborn), supervised machine learning classification models (Scikit-Learn), and a fully interactive, multi-page executive dashboard hosted on Tableau Public.

What is it for? (Scope & Target Audience)

Designed specifically for retail banking executives, risk portfolio managers, and customer retention teams, this application transforms raw transactional logs into transparent risk indicators. It bridges the gap between complex statistical data and frontline decision-making by categorizing cardholders into distinct behavioral, financial, and demographic profiles.

Why is it? (The Business Problem)

In the competitive financial services sector, acquiring a new credit cardholder is significantly more expensive—often up to five times—than retaining an existing one. Banks frequently suffer silent attrition, losing high-value accounts due to undetected customer dissatisfaction or prolonged inactivity. Traditional reporting often reacts after a customer closes their account. This project was built to shift the paradigm from reactive churn reporting to proactive, predictive risk mitigation.

What is the Benefit? (Strategic Impact & Value)

⚬ Early Risk Visibility: Uncovers leading behavioral indicators—such as critical thresholds in Months_Inactive_12_mon and descending transaction volume tiers—enabling proactive intervention.
⚬ Data-Driven Retention Strategy: Equips retention specialists with targeted insights to deploy personalized incentives or credit limit adjustments before a cardholder cancels.
⚬ Measurable ROI: Minimizes portfolio revenue leakage, preserves long-term customer lifetime value (LTV), and optimizes marketing spend by focusing retention efforts strictly on high-propensity churn segments.

02. Business Requirements

To deliver actionable business intelligence and proactive risk management for financial institutions, this project addresses two core user personas and operational goals:

1. Portfolio Managers & Risk Analysts:
  ⚬ Require automated tracking of key behavioral and financial metrics (such as credit limits, revolving balances, and transaction frequency) that signal early warning indicators of customer attrition.
  ⚬ Need clean data structures and exploratory dashboards to monitor overall portfolio health, demographic concentrations, and income bracket risk factors.
2. Customer Retention Teams:
  ⚬ Require predictive customer segmentation (via machine learning classification models like Random Forest and Decision Tree) to identify high-risk accounts before they close.
  ⚬ Need actionable insights into leading churn drivers—such as low transaction counts and decreased engagement over a 12-month period—to deploy targeted retention campaigns and minimize revenue loss effectively.

03. Dataset Content

⚬ Source & Structure: The project utilizes the BankChurners dataset (BankChurners.csv), hosted locally within the project repository under data/raw/ and processed under data/processed/.
⚬ Dimensions: The dataset consists of 10,127 customer records and 23 features, providing a robust sample size that is lightweight, fully optimized for performance, and well within standard repository limits.
⚬ Feature Categorization: The data covers comprehensive customer attributes categorized into four main pillars:
  ⚬ Demographics & Geography: Customer Age, Gender, Dependent count, Education Level, Marital Status, and Income Category.
  ⚬ Financial Behavior: Credit Limit, Total Revolving Balance, Open-to-Buy Credit (Avg_Open_To_Buy), and Average Utilization Ratio (Avg_Utilization_Ratio).
  ⚬ Transactional Activity: Total Transaction Amount, Total Transaction Count, Total Relationship Count, Months on Book, and Inactive Months over a 12-month period.
  ⚬ Target Variable: Attrition_Flag (distinguishing between retained Existing Customers and churned Attrited Customers).

04. Hypothesis & Validation

⚬ Core Hypothesis:
  "Customer churn in credit card services is not random; it is strongly predictable by analyzing a combination of demographic segments, transactional velocity, credit utilization ratios, and inactive duration patterns."
⚬ Validation Methodology:
  1. Exploratory Data Analysis & Visualization: Generated comparative distributions and visual plots (histograms, box plots) to examine statistical variations between retained (Existing) and churned (Attrited) customers across key metrics like customer age, credit limits, and transaction totals.
  2. Supervised Machine Learning Modeling: Trained three distinct classification models (Random Forest, Decision Tree, and Logistic Regression) using an 80/20 stratified train-test split to test whether customer behavior patterns allow accurate classification.
  3. Performance & Feature Importance Metrics: Validated the hypothesis using high ROC-AUC scores (~97.9% via Random Forest) and feature importance analysis, confirming that transactional velocity (Total_Trans_Amt, Total_Trans_Ct) and revolving balances are robust predictors of account closure.

05. Data Management & Cleaning Approach

⚬ Collection & Hygiene: The raw BankChurners.csv dataset containing 10,127 records and 23 columns was ingested into Python (Pandas, NumPy). Missing value checks (df.isnull().sum()) and duplicate verification confirmed structural integrity prior to modeling.
⚬ Feature Engineering & Preprocessing: Data types were validated, unnecessary metadata columns were dropped, and features were scaled and split (stratify=y) to prepare clean inputs for machine learning classification.

06. Technical Analysis Techniques Used & Model Evaluation

⚬ Methods Used: Exploratory Data Analysis (EDA) using descriptive statistics and data distribution plots; comparative feature analysis; and supervised machine learning classification models (Random Forest, Decision Tree, and Logistic Regression).
⚬ Limitations & Alternatives: While Logistic Regression provides a strong linear baseline, it struggles with complex, non-linear interactions. To overcome this limitation, ensemble tree-based models (Random Forest) were implemented as an alternative approach, yielding superior predictive accuracy and robust handling of multi-feature financial behavior.

Model Performance Comparison

Three classification models were trained and evaluated using an 80/20 stratified train-test split in 02_machine_learning.ipynb:

Model	Accuracy	ROC-AUC Score	Primary Advantage
Random Forest Classifier	94.47%	97.91%	Superior performance in capturing non-linear interactions and reducing overfitting.
Decision Tree Classifier	93.14%	94.69%	High interpretability with clear decision rules for stakeholders.
Logistic Regression	89.98%	91.26%	Robust, mathematically sound linear baseline utilizing feature scaling.

07. Rationale: Mapping Business Requirements to Data Visualizations

To ensure every technical insight directly supports stakeholder goals, business requirements were mapped to our data visualizations and Tableau dashboard sections as follows:

1. Tracking Portfolio Health & Demographics (Mapped to Business Requirement 1):
  ⚬ Rationale: Portfolio managers and risk analysts need visibility over customer demographics and baseline attributes to spot high-risk segments early.
  ⚬ Visualizations: Demographics histograms (Age/Gender distribution) and Education Level vs. Churn matrices (docs/screenshots/customer_age_distribution.png) were implemented to highlight vulnerable age and income brackets.
2. Monitoring Credit & Financial Risk (Mapped to Business Requirement 1):
  ⚬ Rationale: Assessing financial exposure requires clear comparisons of revolving balances and credit limits between active and churned accounts.
  ⚬ Visualizations: Box plots for credit limits and revolving balances (docs/screenshots/credit_limit_by_attrition.png) map directly to this requirement, instantly signaling financial thresholds where customers tend to churn.
3. Proactive Customer Retention & Engagement (Mapped to Business Requirement 2):
  ⚬ Rationale: Retention teams need to identify declining account usage before a customer closes their card.
  ⚬ Visualizations: Transaction amount and count distribution histograms (docs/screenshots/total_transaction_amount_distribution.png) map directly to this requirement, visually exposing how low transaction velocity over a 12-month period correlates with attrition.

08. Dashboard Visualisation & Architecture

The interactive Executive Dashboard was published and hosted via Tableau Public, ensuring secure cloud accessibility for stakeholders without requiring local software installations.

⚬ Live Dashboard Access: View Live Tableau Public Dashboard

Dashboard Pages & Content

⚬ Page 1: Overview & Demographics
  ⚬ High-level KPI summary cards for total customer count and overall churn rate; demographic distribution histograms (Age, Gender breakdown); and an Education Level vs. Churn matrix.
⚬ Page 2: Financial & Behavioral Analysis
  ⚬ Income category distribution charts; credit limit box plots; marital status overviews; and inactive months tracking (12-month duration analysis).
⚬ Page 3: Transactional Performance & Trends
  ⚬ Card category performance indicators; behavioral trend line charts; and total transaction amount & count distribution histograms.

Dashboard Previews

09. Key Findings & Conclusions

⚬ Months Inactive: Customers with 3 or more inactive months over a 12-month period exhibited a sharply higher propensity to churn.
⚬ Transaction Volume: Total transaction amounts and total transaction counts are among the strongest leading indicators of customer retention; lower transaction tiers cluster heavily among churned accounts.
⚬ Credit Limits & Revolving Balances: Variance in revolving balances and credit utilization ratios provided critical behavioral boundaries separating existing cardholders from attrited customers.

10. Ethical Considerations, Limitations & Challenges

⚬ Data Privacy & Compliance: The BankChurners.csv dataset consists of anonymized customer banking records obtained from public educational repositories, ensuring full compliance with data privacy standards and ethical usage.
⚬ Algorithmic Fairness: Exploratory data analysis and predictive modeling were conducted with careful oversight to minimize demographic bias, ensuring that customer retention recommendations remain objective across all age and income brackets.
⚬ Class Imbalance & Mitigations: Churn prediction models inherently encounter class imbalance (fewer attrited customers than existing ones), which was addressed using stratified splitting (stratify=y) and evaluated using precision, recall, and ROC-AUC metrics rather than accuracy alone.

11. Development Roadmap & Future Improvements

⚬ Real-Time API Integration: Implement automated webhooks or API endpoints to ingest live customer transaction data for real-time churn risk scoring.
⚬ Advanced Deep Learning: Explore neural network architectures (such as Multi-Layer Perceptrons) to capture non-linear behavioral patterns in cardholder attrition.
⚬ Enterprise BI Automation: Deepen expertise in advanced Tableau dashboard actions, calculated fields, and automated cloud data refresh schedules.

12. Local Setup & Execution

To run this project locally:

1. Clone the repository and navigate to the project directory:
   git clone https://github.com/resmie-palova/Credit_Card_Churn_Analysis.git
   cd Credit_Card_Churn_Analysis
   
2. Activate your Python 3.12.8 virtual environment:
   source .venv/bin/activate
   
3. Install required dependencies:
   pip install -r requirements.txt
   
4. Run Jupyter Notebooks to explore the ETL, EDA, and machine learning pipelines:
   jupyter notebook
   

13. Credits & Acknowledgements

⚬ Content & Data Sources:
  ⚬ Dataset: The original bank customer churn dataset (BankChurners.csv) sourced from public data repositories, providing 10,127 records for demographic, financial, and behavioral attribution analysis.
⚬ Media & Visual Assets:
  ⚬ Dashboard Visualization: Built and hosted via Tableau Public, utilizing native visual layouts, color palettes, and interactive filters.
  ⚬ Graphical Assets & Artifacts: High-resolution visual outputs (dpi=300) stored systematically in docs/screenshots/.
⚬ Acknowledgements & Support:
  ⚬ Special thanks to course facilitators Vasi, Emma, and learning support manager Paul Thomas O'Riordan for continuous guidance, code reviews, and invaluable feedback throughout the development lifecycle.
  ⚬ Appreciation for the Code Institute LMS modules, live masterclasses, and collaborative AI tools that supported code optimization and project documentation standards. 