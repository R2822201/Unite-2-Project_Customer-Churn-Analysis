# Credit Card Customer Churn Analytics

## Project Purpose & Business Rationale
This project addresses customer churn within credit card operations using the `BankChurners.csv` dataset. By leveraging advanced data analytics, statistical hypothesis testing, and supervised machine learning, we identify key indicators of churn risk to enable proactive customer retention strategies and minimize revenue loss.

## Target Audience
* **Portfolio Managers & Risk Analysts:** To monitor key behavior metrics (such as transaction frequency) that signal customer attrition.
* **Customer Retention Teams:** To implement targeted interventions for accounts identified as high-risk by predictive models.

## Repository Architecture
```text
Unite2_Project/
├── data/
│   ├── processed/
│   │   └── cleaned_bank_churners.csv
│   └── raw/
│       └── BankChurners.csv
├── notebooks/
│   ├── 01_etl_and_eda.ipynb
│   └── 02_machine_learning.ipynb
├── .gitignore
├── Procfile
├── README.md
├── requirements.txt
└── setup.sh

---

## Data Analysis & Pipeline Overview

### 1. Data Extraction, Transformation, and Loading (ETL)
* **Extraction:** Loaded raw data containing 10,127 rows and 23 columns.
* **Cleaning & Transformation:** 
  * Dropped non-predictive identifier columns (`CLIENTNUM`) and Naive Bayes benchmark attributes.
  * Encoded the primary target variable `Attrition_Flag` into binary integer format (`Churn`: `1` for Attrited, `0` for Existing).
  * Converted categorical attributes (`Gender`, `Marital_Status`, `Education_Level`, `Income_Category`, `Card_Category`) into numerical features via one-hot and binary encoding (expanding the feature set to 34 columns).
* **Loading:** Exported the cleaned, engineered dataset to `data/processed/cleaned_bank_churners.csv`.

### 2. Statistical Analysis & Hypothesis Testing
* **Hypothesis ($H_1$):** Customers with significantly lower 12-month transaction counts (`Total_Trans_Ct`) exhibit a higher probability of churning.
* **Methodology:** Executed a two-sample Welch's $t$-test comparing transaction volumes between churned ($N=1,627$) and retained ($N=8,500$) customer segments.
* **Results:** 
  * $t$-statistic: `-54.14`
  * $p$-value: `0.0000` ($p < 0.05$)
* **Conclusion:** Null hypothesis ($H_0$) rejected. Transaction frequency is a statistically significant indicator of customer churn.

### 3. Machine Learning Classification
* **Model Selection:** Implemented a Decision Tree Classifier (`max_depth=5`) to establish a fast, interpretable rule-based model for risk segmentation.
* **Evaluation Metrics:**
  * **Overall Accuracy:** `93%`
  * **Precision (Churn Class 1):** `0.83`
  * **Recall (Churn Class 1):** `0.73`
  * **ROC-AUC Score:** `0.9469`

---

## Mapping to Assessment Criteria & Learning Outcomes

* **LO1: Statistical Principles & Machine Learning**
  * **1.1 & 1.2:** Applied descriptive metrics and conducted formal hypothesis testing using Welch's $t$-test to validate differences in transaction distributions.
  * **1.3:** Implemented and evaluated a supervised decision tree classification algorithm using `scikit-learn`.

* **LO2: Project Structure & Planning**
  * **2.1:** Organised project directories (`data/`, `notebooks/`) according to standard data analytics conventions and built an automated ETL workflow.
  * **2.2:** Justified the selection of decision trees for transparent interpretability when communicating customer risk drivers to business stakeholders.

* **LO3: Real-World Problem Solving**
  * **3.1 & 3.3:** Investigated credit card churn using structured cleaning, hypothesis testing, and model validation methodologies.

* **LO4: Adaptation to Analytics Tools**
  * **4.1 & 4.2:** Demonstrated proficiency with Python data science libraries (`pandas`, `scipy`, `scikit-learn`), VS Code Jupyter environments, and Git version control.

---

## Retrospective & Learning Reflection
Through this project, key technical milestones were achieved in optimizing execution speed across large feature matrices, structuring modular Jupyter workflows, and isolating environments with `.venv`. Managing version control through atomic Git commits ensured continuous delivery and repository stability throughout the development lifecycle.


## Interactive Stakeholder Prototype (Tableau / Power BI Rationale)
To satisfy stakeholder requirements for interactive data exploration:
* **Proposed Interactive Tool:** Tableau Public / Power BI Desktop.
* **Interactive Features:** 
  * Dynamic filters for customer demographics (`Card_Category`, `Income_Category`, `Gender`).
  * Real-time churn risk indicators based on transaction volume thresholds derived from statistical testing ($p < 0.05$).
* **Business Utility:** Enables non-technical retention teams to isolate high-risk customer segments without running raw Python code.
