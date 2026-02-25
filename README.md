# 🏦 Loan Default Risk Analysis & Prediction Pipeline

**Author:** Bhavaneeth Parnapalli | Data Science @ University of Texas at Dallas  
**Tech Stack:** Python, SQL, Pandas, Scikit-Learn, XGBoost, Tableau  

![Dashboard Preview](Dashboard 1.png)
*(👉 **[Click here to interact with the live Tableau Dashboard](https://public.tableau.com/views/Loan_Default_Risk_Analysis/Dashboard1?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)**)*

---

## 📌 Project Overview
This project is an end-to-end Machine Learning and Business Intelligence pipeline designed to predict loan defaults and translate those predictive probabilities into actionable financial strategies. 

Using a 1.6GB dataset of historical lending data, I engineered a pipeline that processes the raw data, trains multiple classification models to identify high-risk borrowers, and outputs a dynamic risk-assessment dashboard for bank executives.

## 🎯 Business Problem
Financial institutions lose millions annually to loan defaults. Traditional credit scoring often misses non-linear relationships between borrower characteristics. The goal of this project was to:
1. Identify historical patterns leading to "Charged Off" or "Defaulted" loans.
2. Build an algorithm to assign an exact probability of default to new applicants.
3. Determine the optimal risk-score threshold to minimize financial loss while maximizing loan approval volume.

---

## 🛠️ The Data Pipeline & Methodology

### 1. Data Extraction & Engineering (SQL & Pandas)
* Built a custom `db_manager.py` script to manage local SQLite databases (`loan_data.db`).
* Queried a massive 1.6GB local database to aggregate loan statuses and isolate completed loans (Fully Paid vs. Defaulted).
* Handled a severe class imbalance (80% Paid / 20% Default) by establishing a binary target variable (`is_default`).
* Cleaned messy text columns (e.g., stripping `%` symbols from interest rates, extracting integers from employment lengths) and imputed missing values using statistical medians.

### 2. Machine Learning Modeling (Scikit-Learn & XGBoost)
Navigated the precision/recall trade-off across three algorithms, optimizing for the detection of risky loans:
* **Logistic Regression:** Established a strong baseline by utilizing `class_weight='balanced'` to force the model to prioritize the minority default class.
* **Random Forest Classifier:** Captured non-linear relationships. Explicitly managed the `max_depth` parameter to navigate the bias-variance tradeoff and prevent severe overfitting.
* **XGBoost (Extreme Gradient Boosting):** Selected as the final model for its superior handling of tabular data. Utilized `scale_pos_weight` to optimize recall, successfully identifying roughly 68% of all actual defaults while minimizing false positives to protect the bank's profit margins.

### 3. Business Intelligence (Tableau)
Extracted the exact probability of default (`predict_proba`) from the XGBoost model and exported the refined dataset (`xgboost_risk_scores.csv`) to Tableau to build a 3-part executive dashboard:
* **Risk Distribution Histogram:** Visually proves the model's efficacy by showing the stark separation between paid loans (left-skewed) and defaulted loans (right-skewed).
* **Business Impact Dual-Axis Chart:** A financial cutoff visual mapping the exact dollar amount of bad loans prevented vs. good loans sacrificed at every probability threshold.
* **High-Risk Profile Heatmap:** Highlights specific high-danger combinations (e.g., Grade F/G loans for Small Businesses) for the underwriting team to avoid.

---

## 📂 Repository Structure

```text
├── dashboard/
│   └── Loan_Default_Risk_Analysis      # Tableau workbook files
├── data/
│   ├── database/
│   │   └── loan_data.db                # Local SQLite database
│   ├── processed/
│   │   └── xgboost_risk_scores.csv     # Cleaned ML-ready data & risk scores
│   └── raw/
│       └── accepted_2007_to_...        # Original 1.6GB raw dataset (ignored in git)
├── models/                             # Saved machine learning models (.pkl)
├── notebooks/
│   └── 01_eda.ipynb                    # Jupyter notebook for exploratory data analysis and modeling
├── src/
│   └── db_manager.py                   # Python script for database pipeline management
├── .gitignore                          # Git ignore rules for virtual environments and large files
├── Dashboard 1.png                     # Static visual export of the Tableau dashboard
├── LICENSE                             # Project license
└── README.md                           # Project documentation