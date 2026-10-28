# Project XYZ

Unite 2 Project Credit Card Customer Churn Analysis - Finance 

Predictive Analytics & Customer Attrition Intelligence: A Data-Driven Framework for Credit Card Portfolio Retention

## 01 Project Presentation & Executive Summary

### 1. What is it?
The **Credit Card Customer Churn Analysis** is an end-to-end data science and business intelligence solution built on a comprehensive dataset of 10,127 bank customers (`BankChurners.csv`). It integrates a rigorous Python-based ETL and exploratory data analysis pipeline (`Pandas`, `NumPy`, `Seaborn`), supervised machine learning classification models (`Scikit-Learn`), and a fully interactive, multi-page executive dashboard hosted on **Tableau Public**.

### 2. What is it for? (The Scope & Target Audience)
Designed specifically for retail banking executives, risk portfolio managers, and customer retention teams, this application transforms raw transactional logs into transparent risk indicators. It bridges the gap between complex statistical data and frontline decision-making by categorizing cardholders into distinct behavioral, financial, and demographic profiles.

### 3. Why is it? (The Business Problem)
In the competitive financial services sector, acquiring a new credit cardholder is significantly more expensive—often up to five times—than retaining an existing one. Banks frequently suffer silent attrition, losing high-value accounts due to undetected customer dissatisfaction or prolonged inactivity. Traditional reporting often reacts *after* a customer closes their account. This project was built to shift the paradigm from **reactive churn reporting to proactive, predictive risk mitigation**.

### 4. What is the Benefit? (The Strategic Impact & Value)
* **Early Risk Visibility:** Uncovers leading behavioral indicators—such as critical thresholds in `Months_Inactive_12_mon` and descending transaction volume tiers—enabling proactive intervention.
* **Data-Driven Retention Strategy:** Equips retention specialists with targeted insights to deploy personalized incentives or credit limit adjustments before a cardholder cancels.
* **Measurable ROI:** Minimizes portfolio revenue leakage, preserves long-term customer lifetime value (LTV), and optimizes marketing spend by focusing retention efforts strictly on high-propensity churn segments.

### 5. Technical Hypotheses & Statistical Validation

To structure our exploratory data analysis and machine learning models, we formulated and tested three core hypotheses:
* **Hypothesis 1 (Inactivity Duration & Churn):**
  * *Statement:* Customers with prolonged periods of inactivity (3+ months inactive) exhibit a significantly higher attrition rate.
  * *Validation:* Confirmed via exploratory data analysis and Random Forest feature importance ranking (`Months_Inactive_12_mon`).
* **Hypothesis 2 (Transaction Volume & Retention):**
  * *Statement:* Lower total transaction amounts and lower total transaction counts over a 12-month period strongly correlate with customer churn.
  * *Validation:* Confirmed through comparative distribution plots and Tableau transaction analysis.
* **Hypothesis 3 (Credit Limit & Revolving Balances):**
  * *Statement:* Cardholders maintaining lower revolving balances and lower credit limits exhibit higher propensity to churn due to low product engagement.
  * *Validation:* Confirmed through financial metrics EDA comparing existing versus attrited customer segments.

### 6. Business Reflection & Strategic Learnings

From a commercial perspective, this project demonstrated that customer attrition in banking is rarely random; it follows distinct behavioral signatures. By moving beyond descriptive reporting into predictive classification, banks can transition from a passive stance to an active retention posture. The integration of the Tableau dashboard ensures that non-technical stakeholders (such as relationship managers and marketing teams) can immediately interpret risk tiers and execute targeted retention campaigns, protecting portfolio profitability and customer lifetime value.

### 7. Learning Journey

This project represents the culmination of advanced technical training and practical application. I would like to extend my sincere gratitude and appreciation to:
* **The Code Institute Course Materials & LMS:** Providing structured, industry-aligned learning modules covering Python, ETL pipelines, exploratory data analysis, and version control best practices.
* **Course Facilitators & Mentors:** Offering continuous guidance, constructive code reviews, and invaluable feedback throughout the development lifecycle.
* **Masterclasses & Peer Collaboration:** The live masterclasses and community sessions provided critical insights into data visualization storytelling, model evaluation, and software engineering standards.


## 02 Project Overview

The **Credit Card Customer Churn Analysis** project is an end-to-end data science and business intelligence solution designed to address financial attrition within a banking portfolio comprising 10,127 customer records. In the competitive financial services sector, retaining existing cardholders is significantly more cost-effective than acquiring new ones. This project bridges raw transactional data and strategic decision-making by uncovering the core demographic, financial, and behavioral drivers behind customer attrition.

## 03 Key Objectives & Business Requirements
* **Portfolio Health & Risk Visibility:** Provide risk analysts and portfolio managers with granular visibility into customer demographics, credit limits, and revolving balances to spot high-risk segments early.

* **Predictive Attrition Modeling:** Implement supervised machine learning classification models (Random Forest, Decision Tree, and Logistic Regression) to accurately predict which active customers exhibit high probability of closing their accounts.

* **Interactive Stakeholder Dashboards:** Deploy a comprehensive, multi-page executive dashboard via Tableau Public to translate complex statistical findings into actionable, color-coded visual insights for non-technical stakeholders and retention teams.

## 04 Methodology & Technical Pipeline
1. **ETL & Exploratory Data Analysis (EDA):** Executed comprehensive data cleaning, artifact removal, and statistical distribution checks using Python (`Pandas`, `NumPy`), followed by automated high-resolution visualization generation (`Matplotlib`, `Seaborn`) stored systematically within `docs/screenshots/`.
2. **Machine Learning Modeling:** Implemented rigorous data preprocessing, feature scaling, and stratified train-test splitting (`stratify=y`) within a controlled Python 3.12.8 environment (`.venv`) to train and evaluate robust classification models.
3. **Cloud Deployment & Visualization:** Connected cleaned datasets directly to **Tableau Public** to deliver an interactive, secure, browser-based executive dashboard categorized into demographic, financial, and transactional analytical views.


**Project XYZ** is a comprehensive data analysis tool designed to streamline data exploration, analysis, and visualisation. The tool supports multiple data formats and provides an intuitive interface for both novice and expert data scientists.

# ![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

## 05 Dataset Content

* Describe your dataset. Choose a dataset of reasonable size to avoid exceeding the repository's 100GB limit.

* The project utilizes the **BankChurners dataset** (`BankChurners.csv`), which is hosted locally within the project repository under `data/raw/` and processed under `data/processed/`. 

* The dataset consists of **10,127 customer records and 23 features**, providing a robust sample size that is lightweight, fully optimized for performance, and well within standard repository limits.

* The data covers comprehensive customer attributes categorized into four main pillars:
  * Demographics & Geography:** Customer Age, Gender, Dependent count, Education Level, Marital Status, and Income Category.

  * Financial Behavior:** Credit Limit, Total Revolving Balance, Open-to-Buy Credit (`Avg_Open_To_Buy`), and Average Utilization Ratio (`Avg_Utilization_Ratio`).

  * Transactional Activity:** Total Transaction Amount, Total Transaction Count, Total Relationship Count, Months on Book, and Inactive Months over a 12-month period.

  * Target Variable:** `Attrition_Flag` (distinguishing between retained *Existing Customers* and churned *Attrited Customers*).


## 06 Business Requirements

* Describe your business requirements

To deliver actionable business intelligence and proactive risk management for financial institutions, this project addresses two core user personas and operational goals:

* 1. Portfolio Managers & Risk Analysts:
  * Require automated tracking of key behavioral and financial metrics (such as credit limits, revolving balances, and transaction frequency) that signal early warning indicators of customer attrition.
  * Need clean data structures and exploratory dashboards to monitor overall portfolio health, demographic concentrations, and income bracket risk factors.

* 2. Customer Retention Teams:
  * Require predictive customer segmentation (via machine learning classification models like Random Forest and Decision Tree) to identify high-risk accounts before they close.
  * Need actionable insights into leading churn drivers—such as low transaction counts and decreased engagement over a 12-month period—to deploy targeted retention campaigns and minimize revenue loss effectively.


## 07 Hypothesis and how to validate?

* List here your project hypothesis(es) and how you envision validating it (them) 

Core Project Hypothesis:** 
  * *"Customer churn in credit card services is not random; it is strongly predictable by analyzing a combination of demographic segments, transactional velocity, credit utilization ratios, and inactive duration patterns."*

* How the Hypothesis was Validated:**
  * **1. Exploratory Data Analysis & Visualization:** Generated comparative distributions and visual plots (histograms, box plots) to examine statistical variations between retained (*Existing*) and churned (*Attrited*) customers across key metrics like customer age, credit limits, and transaction totals.

  * 2. Supervised Machine Learning Modeling:** Trained three distinct classification models (Random Forest, Decision Tree, and Logistic Regression) using an 80/20 stratified train-test split to test whether customer behavior patterns allow accurate classification.

  * 3. Performance & Feature Importance Metrics:** Validated the hypothesis using high ROC-AUC scores (~97.9% via Random Forest) and feature importance analysis, confirming that transactional velocity (`Total_Trans_Amt`, `Total_Trans_Ct`) and revolving balances are robust predictors of account closure.


## 08 Project Plan

* Outline the high-level steps taken for the analysis.

* Outline the high-level steps taken for the analysis:
  * 1. Project Conception & Scoping:** Defined business requirements, user personas, and core hypotheses around credit card customer churn.
  * 2. Environment Setup & Data Ingestion:** Configured a reproducible Python 3.12.8 virtual environment (`.venv`) and loaded the `BankChurners.csv` dataset (10,127 records) into `01_etl_and_eda.ipynb`.
  * 3. ETL & Data Cleaning:** Cleared unlabelled metadata, handled missing values, verified zero duplicate rows, and engineered the binary target column (`Churn`).
  * 4. Exploratory Data Analysis (EDA):** Generated demographic, financial, and transactional plots, automatically saving high-resolution visualizations to `docs/screenshots/`.
  * 5. Machine Learning Modeling:** Built and compared three classification models (Random Forest, Decision Tree, and Logistic Regression) using an 80/20 stratified split in `02_machine_learning.ipynb`.
  * 6. Executive Dashboard & Documentation:** Exported processed data (`data/processed/`) to Tableau Public for interactive storytelling and finalized the `README.md`.


* How was the data managed throughout the collection, processing, analysis and interpretation steps?
  * **Collection & Storage:** Raw data was safely isolated in `data/raw/` to ensure the source file remained pristine. Processed outputs were saved in `data/processed/`.

  * **Version Control & Organization:** Maintained a clean repository structure (`/notebooks`, `/data`, `/docs/screenshots`) and used modular Python scripts to ensure full reproducibility and transparency.

  * **Processing & Analysis:** Managed via structured Jupyter Notebooks with strict type enforcement, missing value audits, and automated visualization outputs.


* Why did you choose the research methodologies you used?
* I choose the research methodologies to used?
  * **Hybrid Agile/Waterfall Approach:** Allowed structured milestone planning while maintaining the flexibility to iterate through data cleaning, EDA, and model tuning.

  * **Stratified Train-Test Splitting:** Chosen to maintain class balance between retained and churned customers, preventing model bias during evaluation.

  * **Ensemble Machine Learning (Random Forest & Decision Tree):** Selected because tree-based models excel at capturing complex, non-linear relationships within financial and behavioral customer data while offering high interpretability for stakeholders.

  Hypothesis Testing & Attrition Validation

To drive our exploratory data analysis and predictive modeling, we formulated and tested three core hypotheses regarding bank customer churn:

* **Hypothesis 1 (Inactivity Duration & Churn):**
  * *Statement:* Customers with prolonged periods of inactivity (e.g., 3+ months inactive) have a significantly higher attrition rate than active cardholders.
  * *Validation Result:* Confirmed via exploratory data analysis and our feature importance models. The Tableau "Months Inactive Analysis" dashboard and our Random Forest feature rankings demonstrated that `Months_Inactive_12_mon` is a critical leading indicator of account closure.

* **Hypothesis 2 (Transaction Volume & Customer Retention):**
  * *Statement:* Lower total transaction amounts and lower total transaction counts over a 12-month period strongly correlate with customer churn.
  * *Validation Result:* Confirmed. Comparative distribution plots (`Matplotlib/Seaborn`) and the Tableau "Total Transactions Analysis" page verified that churned customers cluster heavily in the lower transaction volume tiers.

* **Hypothesis 3 (Credit Limit & Revolving Balances):**
  * *Statement:* Customers maintaining lower revolving balances and lower credit limits exhibit higher propensity to churn due to low product engagement.
  * *Validation Result:* Confirmed through our financial metrics EDA, showing clear variance in revolving balances between existing and attrited customer segments.


  ## 09 Dashboard Visualisation

Here are previews of the interactive Tableau Public executive dashboard for the Credit Card Churn Analysis project:

![Tableau Executive Overview](docs/screenshots/01_dashboard_overview.png)
![Financial & Behavioral Metrics](docs/screenshots/09_financial_metrics_M_F.png)

You can explore the live, fully interactive version of the dashboard hosted on Tableau Public here:
[View Live Tableau Public Dashboard](https://public.tableau.com/app/profile/resmie.palova8392/viz/Credit_Card_Churn_Analysis/Dashboard1?publish=yes)


## 10 The rationale to map the business requirements to the Data Visualisations

* List your business requirements and a rationale for mapping them to the Data Visualisations

To ensure every technical insight directly supports stakeholder goals, business requirements were mapped to our data visualisations and Tableau dashboard sections as follows:

* **1. Tracking Portfolio Health & Demographics (Mapped to Business Requirement 1):**
  * **Rationale:** Portfolio managers and risk analysts need visibility over customer demographics and baseline attributes to spot high-risk segments early.
  * **Visualisations:** Demographics histograms (Age/Gender distribution) and Education Level vs. Churn matrices (`docs/screenshots/customer_age_distribution.png`) were implemented to highlight vulnerable age and income brackets.

* **2. Monitoring Credit & Financial Risk (Mapped to Business Requirement 1):**
  * **Rationale:** Assessing financial exposure requires clear comparisons of revolving balances and credit limits between active and churned accounts.
  * **Visualisations:** Box plots for credit limits and revolving balances (`docs/screenshots/credit_limit_by_attrition.png`) map directly to this requirement, instantly signaling financial thresholds where customers tend to churn.

* **3. Proactive Customer Retention & Engagement (Mapped to Business Requirement 2):**
  * **Rationale:** Retention teams need to identify declining account usage before a customer closes their card.
  * **Visualisations:** Transaction amount and count distribution histograms (`docs/screenshots/total_transaction_amount_distribution.png`) map directly to this requirement, visually exposing how low transaction velocity over a 12-month period correlates with attrition.


## 11 Analysis techniques used

* List the data analysis methods used and explain limitations or alternative approaches.

* **List the data analysis methods used and explain limitations or alternative approaches:**
  * **Methods Used:** Exploratory Data Analysis (EDA) using descriptive statistics and data distribution plots; comparative feature analysis; and supervised machine learning classification models (Random Forest, Decision Tree, and Logistic Regression).
  * **Limitations & Alternatives:** While Logistic Regression provides a strong linear baseline, it struggles with complex, non-linear interactions. To overcome this limitation, ensemble tree-based models (Random Forest) were implemented as an alternative approach, yielding superior predictive accuracy and robust handling of multi-feature financial behavior.

* How did you structure the data analysis techniques? Justify your response.

* **How did you structure the data analysis techniques? Justify your response:**
  * **Structure:** The analysis followed a sequential pipeline starting with ETL data cleaning and artifact removal in `01_etl_and_eda.ipynb`, followed by visual statistical exploration, and culminating in predictive modeling in `02_machine_learning.ipynb`.
  * **Justification:** This phased approach ensures that data integrity and feature distributions are fully understood and cleaned before feeding into machine learning algorithms, preventing garbage-in-garbage-out errors and ensuring reliable model evaluation.

* Did the data limit you, and did you use an alternative approach to meet these challenges?

* **Did the data limit you, and did you use an alternative approach to meet these challenges?**
  * **Data Limitations:** The dataset was well-structured with 10,127 clean records and zero missing values after cleaning, but featured potential class imbalance between existing and churned customers.
  * **Alternative Approach:** To meet this challenge, stratified train-test splitting (`stratify=y`) was enforced to maintain consistent class proportions across training and testing sets, ensuring unbiased model performance metrics.

* How did you use generative AI tools to help with ideation, design thinking and code optimisation?

* **How did you use generative AI tools to help with ideation, design thinking and code optimisation?**
  * **Ideation & Design Thinking:** Utilized AI collaborators to brainstorm executive dashboard layouts, structure business requirements, and align visual mappings with stakeholder goals.
  * **Code Optimisation:** Leveraged AI assistance to refine modular Python plotting functions, automate high-resolution plot exports (`dpi=300`) directly into `docs/screenshots/`, and optimize scikit-learn pipeline configurations.


## 12 Ethical considerations (optional)

* Feel free to delete this section if this is a data visualisation only (unit 1 or 2) project submission.
* Were there any data privacy, bias or fairness issues with the data?

* **Were there any data privacy, bias or fairness issues with the data?**
 * **Data Privacy:** The dataset (`BankChurners.csv`) is anonymized and contains aggregated customer banking attributes without direct personal identifiers (such as names, specific account numbers, or contact details), ensuring individual privacy compliance.

  * **Bias & Fairness:** Financial and demographic features (such as income categories or age brackets) were carefully monitored during Exploratory Data Analysis to prevent discriminatory modeling or algorithmic bias against specific customer segments.

* How did you overcome any legal or societal issues?

* **How did you overcome any legal or societal issues?**
  * **Compliance & Transparency:** Maintained full transparency by documenting all data cleaning steps, handling metadata responsibly, and ensuring the predictive models serve supportive business retention strategies rather than punitive customer exclusion.
  * **Open Repository Standards:** Adhered to secure data management guidelines by keeping raw data isolated and ensuring processed outputs comply with standard open-source and institutional sharing practices.

* **Data Privacy & Compliance:** The `BankChurners.csv` dataset consists of anonymized customer banking records obtained from public educational repositories, ensuring full compliance with data privacy standards and ethical usage.
* **Algorithmic Fairness:** Exploratory data analysis and predictive modeling were conducted with careful oversight to minimize demographic bias, ensuring that customer retention recommendations remain objective across all age and income brackets.

## 13 Unfixed Bugs & Challenges Faced
* **Class Imbalance:** Churn prediction models inherently encounter class imbalance (fewer attrited customers than existing ones), which required careful evaluation using precision, recall, and F1-score rather than accuracy alone.
* **Feature Correlation:** Multicollinearity among certain financial and transaction metrics required systematic feature selection prior to training our classification algorithms (Random Forest, Decision Tree, and Logistic Regression).

## 14 Knowledge Gaps & How They Were Addressed
* **Advanced Machine Learning Pipelines:** Researched hyperparameter tuning and stratified train-test splitting (`stratify=y`) to optimize classification performance.
* **Interactive Business Intelligence:** Utilized Tableau Public data hierarchies and multi-page filtering actions to translate complex statistical outputs into user-friendly executive dashboards.

## 15 Developmental Roadmap & Future Improvements
* **Real-Time API Integration:** Implement automated webhooks or API endpoints to ingest live customer transaction data for real-time churn risk scoring.
* **Advanced Deep Learning:** Explore neural network architectures (such as Multi-Layer Perceptrons) to capture non-linear behavioral patterns in cardholder attrition.



## 16 Dashboard Design (optional)

* Feel free to delete this section if this is a data visualisation only (unit 1 or 2) project submission.
* List all dashboard pages and their content, either blocks of information or widgets, like buttons, checkboxes, images, or any other item that your dashboard library supports.

* **Listing all dashboard pages and their content, either blocks of information or widgets, like buttons, checkboxes, images, or any other item that your dashboard library supports:**
  * **Page 1: Overview & Demographics**
    * *Widgets & Blocks:* High-level KPI summary cards for total customer count and overall churn rate; demographic distribution histograms (Age, Gender breakdown); and an Education Level vs. Churn matrix.

  * **Page 2: Financial & Behavioral Analysis**
    * *Widgets & Blocks:* Income category distribution charts; credit limit box plots; marital status overviews; and inactive months tracking (12-month duration analysis).

  * **Page 3: Transactional Performance & Trends**
    * *Widgets & Blocks:* Card category performance indicators; behavioral trend line charts; and total transaction amount & count distribution histograms.

* Later, during project development, you may revisit your dashboard plan to update a feature (for example, at the beginning of the project, you were confident you would use a given plot to display an insight, but later you used another plot type).
* How were data insights communicated to technical and non-technical audiences?

* **How were data insights communicated to technical and non-technical audiences?**
  * **Technical Audiences:** Insights were communicated via detailed confusion matrices, feature importance rankings (Random Forest), and ROC-AUC evaluation metrics in Jupyter notebooks.
  * **Non-Technical Audiences:** Complex statistical findings were translated into intuitive visual stories, color-coded risk flags, and clean interactive dashboards on Tableau Public so stakeholders could easily grasp key attrition drivers without reviewing raw code.

* Explain how the dashboard was designed to communicate complex data insights to different audiences. 

* **Explain how the dashboard was designed to communicate complex data insights to different audiences:**
  * **Structure & Layout:** Designed with a logical top-to-bottom flow—starting from high-level portfolio health down to granular transactional behaviors.
  * **Visual Hierarchy:** Utilized clean color palettes, clear labels, and segmented tabs to ensure that risk analysts and retention teams can quickly identify high-risk customer segments and make data-driven decisions.


## 17 Unfixed Bugs

* Please list any unfixed bugs and explain why they were not fixed. This section should include shortcomings of the frameworks or technologies used. Although time can be a significant variable to consider, paucity of time and difficulty understanding implementation are not valid reasons to leave bugs unfixed.

* **Please list any unfixed bugs and explain why they were not fixed:**
  * *Status:* No critical application errors, data pipeline blockers, or broken machine learning predictions remain in the codebase. Minor styling adjustments on secondary Tableau filter interactions were noted during testing but do not impact core stakeholder functionality or analytical outcomes.

* Did you recognise gaps in your knowledge, and how did you address them?

* **Did you recognise gaps in your knowledge, and how did you address them?**
  * *Knowledge Gaps & Resolution:* During model comparison, optimizing multi-class feature importance interpretation presented a minor learning curve. This was addressed by reviewing official scikit-learn documentation, consulting course facilitators, and leveraging structured testing within the virtual environment (`.venv`).

* If applicable, include evidence of feedback received (from peers or instructors) and how it improved your approach or understanding.

* **If applicable, include evidence of feedback received (from peers or instructors) and how it improved your approach or understanding:**
  * *Feedback Integration:* Feedback from code reviews and peer check-ins emphasized the importance of robust feature scaling and modular directory structures (`docs/screenshots/`). This guidance directly improved the reproducibility of the ETL pipelines and ensured clear visual presentation across all project notebooks.


## 18 Development Roadmap

* What challenges did you face, and what strategies were used to overcome these challenges?

* **What challenges did you face, and what strategies were used to overcome these challenges?**
  * *Challenge 1 (Environment & Version Control):* Ensuring package compatibility and virtual environment consistency across Jupyter Notebooks.
    * *Strategy:* Configured a standardized Python 3.12.8 virtual environment (`.venv`) and maintained modular requirements tracking.
  * *Challenge 2 (Automated Visualizations):* Managing asset paths and output resolutions for documentation.
    * *Strategy:* Implemented automated directory creation (`os.makedirs`) and high-resolution export parameters (`dpi=300`) to sync all plots cleanly into `docs/screenshots/`.

* What new skills or tools do you plan to learn next based on your project experience? 

* **What new skills or tools do you plan to learn next based on your project experience?**
  * *Advanced Machine Learning & MLOps:* Plan to explore automated hyperparameter tuning libraries (Optuna/GridSearchCV) and model deployment pipelines to serve predictive models via interactive web apps (Streamlit).
  * *Enterprise Data Visualization:* Aim to deepen expertise in advanced Tableau dashboard actions, calculated fields, and automated cloud data refresh schedules for real-time financial monitoring.


## 19 Deployment (optional)

* If this is a Unit 3 Streamlit, Power BI or Tableau Public project, then you can include a link here and explain how you hosted the dashboard.

* **Unit 2 Project, Streamlit, Tableau Public project, then you can include a link here and explain how you hosted the dashboard:**
  * **Dashboard Hosting:** The interactive Executive Dashboard was published and hosted via **Tableau Public**, ensuring secure cloud accessibility for stakeholders without requiring local software installations.
  * **Live Dashboard Access:**  Tableau Public Dashboard Link Here:
   https://public.tableau.com/app/profile/resmie.palova8392/viz/Credit_Card_Churn_Analysis/Dashboard1?publish=yes

   Streamlit link here: http://localhost:8502/
   
  * **Deployment Workflow:** Processed datasets from `data/processed/cleaned_bank_churners.csv` were connected directly to Tableau Public, where visual hierarchies, filtering actions, and multi-page layouts (Overview, Financial Analysis, and Transactional Trends) were deployed to empower risk analysts and customer retention teams.


### 20 Heroku (optional)

* This section is necessary only if you are deploying a Streamlit app to Heroku as part of your submission for units 2 and 3. 
* The App live link is: https://YOUR_APP_NAME.herokuapp.com/ 
* Set the `.python-version` Python version to a [Heroku-22](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version.
* The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. From the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click the button Open App at the top of the page to access your App.
6. If the slug size is too large, then add large files not required for the app to the `.slugignore` file.

* **Deployment Overview:** 
  * As this project utilizes **Tableau Public** for cloud-based interactive visualization rather than a Python web framework (such as Streamlit or Flask), traditional Heroku cloud deployment was not required.

  * All analytical computations, ETL pipelines, and predictive modeling were executed locally within a controlled Python 3.12.8 virtual environment (`.venv`), with outputs synchronized for reporting.

* **Alternative Hosting Strategy:**

  * **Cloud Visualization:** Deployed via Tableau Public to ensure secure, browser-based accessibility for stakeholders.

  * **Version Control & Documentation:** Maintained via GitHub repository version control, ensuring full code reproducibility and complete technical documentation.


## 21 Main Data Analysis Libraries
[https://public.tableau.com/app/profile/resmie.palova8392/viz/Credit_Card_Churn_Analysis/Dashboard1?publish=yes](https://public.tableau.com/app/profile/resmie.palova8392/viz/Credit_Card_Churn_Analysis/Dashboard1?publish=yes)

* Here you should list the libraries you used in the project and provide an example(s) of how you used these libraries.

* **Pandas:** Utilized for data manipulation, cleaning, DataFrame structuring, and missing value checks across the `BankChurners.csv` dataset.

* **NumPy:** Applied for efficient numerical operations, mathematical array transformations, and statistical calculations.

* **Matplotlib & Seaborn:** Used for exploratory data analysis (EDA), generating histograms, box plots, and comparative visualizations to examine customer demographic and behavioral distributions.

* **Scikit-Learn:** Employed for data preprocessing, train-test splitting (`stratify=y`), and training supervised classification models (Random Forest, Decision Tree, and Logistic Regression) to predict customer churn.


## 22 Credits

* In this section, you need to reference where you got your content, media and extra help from. It is common practice to use code from other repositories and tutorials; however, it is important to be very specific about these sources to avoid plagiarism. 

* **Content & Data Sources:**
  * **Dataset:** The original bank customer churn dataset (`BankChurners.csv`) was sourced from public data repositories, providing 10,127 records for demographic, financial, and behavioral attribution analysis.
  * **Project Framework:** Structure, methodologies, and template guidelines were adapted from Code Institute data science and analytics academic standards.

* You can break the credits section into Content and Media, depending on what you include in your project. 

* **Media & Visual Assets:**
  * **Dashboard Visualization:** Built and hosted via **Tableau Public**, utilizing native visual layouts, color palettes, and interactive filters.

  * **Graphical Assets & Icons:** Standard Markdown elements and repository icons sourced via open-source educational templates.

* **Acknowledgements & Help:**
  * Special thanks to course facilitators Vasi, Emma, peer code reviewers, and AI collaborative tools for guidance on pipeline optimization, data visualization structuring,lms, and documentation best practices.


### 23 Content 

- The text for the Home page was taken from the Wikipedia Article A
- Instructions on how to implement form validation were taken from a [Specific YouTube Tutorial](https://www.youtube.com/)
- The icons in the footer were taken from [Font Awesome](https://fontawesome.com/)

* **Dataset Documentation:** 
  * The primary dataset (`BankChurners.csv`) containing 10,127 records was utilized for exploratory data analysis, feature engineering, and customer churn attribution modeling.

* **Documentation Templates:** 
  * Project structure and Markdown formatting guidelines were adapted from Code Institute academic standards and institutional templates.

* **Icons & Styling:** 
  * Standard repository markdown styling elements and icons were sourced via open-source development guidelines and standard web practices.

   💳 Credit Card Bank Customer Churn Analytics & Predictive Modeling

Dataset Content
* The project utilizes the **BankChurners dataset** containing **10,127 records and 23 features**. 
* The data covers comprehensive customer attributes, categorized into:
  * **Demographics & Geography:** Customer Age, Gender, Dependent count, Education Level, Marital Status, and Income Category.
  * **Financial Behavior:** Credit Limit, Total Revolving Balance, Open-to-Buy Credit, and Average Utilization Ratio.
  * **Transactional Activity:** Total Transaction Amount, Total Transaction Count, and Total Relationship Count over a 12-month period.
  * **Target Variable:** `Attrition_Flag` (distinguishing between Existing Customers and Attrited/Churned Customers).

---

Business Requirements
To deliver actionable business intelligence for financial institutions, this project addresses two core user personas:
1. **Portfolio Managers & Risk Analysts:** Require automated tracking of key behavioral metrics (such as transaction velocity and credit utilization) that signal early risk of customer attrition.
2. **Customer Retention Teams:** Require predictive segmentation to identify high-risk accounts and deploy targeted retention campaigns proactively.

---

Hypothesis & Validation
* **Core Hypothesis:** *"Customer churn in credit card services is not random; it is strongly predictable by analyzing a combination of demographic segments, transactional velocity, credit utilization ratios, and inactive duration patterns."*
* **Validation:** Validated through exploratory data visualization and machine learning feature importance modeling, confirming that `Total_Trans_Amt`, `Total_Trans_Ct`, and `Total_Revolving_Bal` are the strongest statistical predictors of churn.

---

Tableau Executive Dashboard Rationale & Roadmap
To satisfy stakeholder requirements for interactive data exploration, clean processed datasets were exported to `data/processed/` and connected to **Tableau Public** to build an executive dashboard structured across three logical sections:
1. **Overview & Demographics:** Summarizes Overall Churn Distribution, Demographics Histograms (Age/Gender), and Education Level vs. Churn matrix.
2. **Financial & Behavioral Analysis:** Displays Income Category breakdowns, Credit Limit tables, Marital Status overviews, and Inactive Months tracking.
3. **Transactional Performance & Trends:** Showcases Card Category performance, Behavioral Line Trends, and Total Transaction Amount & Count distributions.

---

Data Cleaning & ETL Pipeline
* **Artifact Removal:** Dropped redundant Kaggle metadata and unlabelled index columns.
* **Missing Value & Duplicate Audit:** Inspected null counts and removed duplicate rows to maintain 10,127 clean records.
* **Feature Engineering:** Created a binary target column (`Churn`) where `1` represents *Attrited Customers* and `0` represents *Existing Customers*.
* **Data Type Enforcement:** Standardized numerical columns using Python (`pandas`, `numpy`) within a Python 3.12.8 virtual environment (`.venv`).

---

Machine Learning Model Evaluation & Comparison
Three classification models were trained and evaluated using an 80/20 stratified train-test split in `02_machine_learning.ipynb`:

| Model | Accuracy | ROC-AUC Score | Primary Advantage |
| :--- | :---: | :---: | :--- |
| **Random Forest Classifier** | **94.47%**[span_1](start_span)[span_1](end_span) | **97.91%**[span_2](start_span)[span_2](end_span) | Superior performance in capturing non-linear interactions and reducing overfitting. |
| **Decision Tree Classifier** | **93.14%**[span_3](start_span)[span_3](end_span) | **94.69%**[span_4](start_span)[span_4](end_span) | High interpretability with clear decision rules for stakeholders. |
| **Logistic Regression** | **89.98%**[span_5](start_span)[span_5](end_span) | **91.26%**[span_6](start_span)[span_6](end_span) | Robust, mathematically sound linear baseline utilizing feature scaling. |

* **Confusion Matrices & Feature Importance:** Evaluated classification error rates and confirmed transaction metrics as leading indicators of churn.

---

Key Visualizations & Screenshots
Stored in `docs/screenshots/`:
* `docs/screenshots/customer_age_distribution.png`
* `docs/screenshots/credit_limit_by_attrition.png`
* `docs/screenshots/total_transaction_amount_distribution.png`
* `docs/screenshots/model_confusion_matrices.png`
* `docs/screenshots/random_forest_feature_importance.png`

---

Testing & Validation
* **Notebook Testing:** Rigorously tested each cell in `01_etl_and_eda.ipynb` and `02_machine_learning.ipynb` to ensure clean execution without dependency errors.
* **Stratified Splitting:** Ensured class balance during train-test splitting (`stratify=y`) to prevent model bias.

---

Deployment & Local Setup
To run this project locally:
1. Clone the repository and navigate to the project directory.
2. Activate your virtual environment:
   ```bash
   source .venv/bin/activate


### 24 Media

- The photos used on the home and sign-up page are from This Open-Source site
- The images used for the gallery page were taken from this other open-source site

* **Dashboard Visualizations:** 
  * All interactive charts, demographic breakdowns, financial distribution graphs, and transaction matrices were created and hosted via **Tableau Public**.

* **Project Screenshots & Artifacts:** 
  * High-resolution visual outputs (`dpi=300`) generated during exploratory data analysis and machine learning modeling were systematically organized and stored in `docs/screenshots/`.


## 26 Business Requirements

The goal of this project is to uncover data-driven insights and predictive intelligence regarding credit card customer churn across 10,127 records[span_5](start_span)[span_5](end_span). Specifically, we aim to:
* **Identify At-Risk Segments:** Determine which demographic, financial, and behavioral attributes correlate with high credit card churn rates.

* **Predictive Attrition Modeling:** Train supervised classification models (Random Forest, Decision Tree, Logistic Regression) to accurately predict account closures before they occur.

* **Interactive Visualization:** Deploy an executive Tableau Public dashboard to provide risk analysts and retention teams with real-time portfolio visibility.


## 27 Data Management & Cleaning Approach

* **Collection & Hygiene:** The raw `BankChurners.csv` dataset containing 10,127 records and 23 columns was ingested into Python (`Pandas`, `NumPy`)[span_6](start_span)[span_6](end_span)[span_7](start_span)[span_7](end_span). Missing value checks (`df.isnull().sum()`) and duplicate verification confirmed structural integrity prior to modeling[span_8](start_span)[span_8](end_span)[span_9](start_span)[span_9](end_span).

* **Feature Engineering & Preprocessing:** Data types were validated, unnecessary metadata columns were dropped, and features were scaled and split (`stratify=y`) to prepare clean inputs for machine learning classification.


## 28 Key Findings & Conclusions

* **Months Inactive:** Customers with 3 or more inactive months over a 12-month period exhibited a sharply higher propensity to churn.

* **Transaction Volume:** Total transaction amounts and total transaction counts are among the strongest leading indicators of customer retention; lower transaction tiers cluster heavily among churned accounts.

* **Credit Limits & Revolving Balances:** Variance in revolving balances and credit utilization ratios provided critical behavioral boundaries separating existing cardholders from attrited customers.

## 29 Limitations & Alternative Approaches

* **Class Imbalance:** Churn datasets often suffer from class imbalance (fewer churned customers than existing ones), which was addressed using stratified splitting and robust evaluation metrics.

* **Future Enhancements:** Future iterations could incorporate real-time webhook alerts for high-risk accounts and deploy deep learning architectures for advanced behavioral forecasting.

## 25 Acknowledgements (optional)

* Thank the people who supported this project.

* **Support & Guidance:**
  * Special thanks to course facilitators and mentors for their continuous guidance throughout the development of the Credit Card Churn Analysis project.
* **Peer Reviews & Collaboration:**
  * Grateful to peers and code reviewers for valuable feedback on exploratory data analysis structuring, model validation, and visualization clarity.
* **Resources & AI Tools:**
  * Appreciation for open-source data communities, official documentation libraries (Pandas, Scikit-Learn, Tableau), and collaborative AI tools that supported code optimization and project documentation best practices.






