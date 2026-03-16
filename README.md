# Loan Approval and Loan Amount Prediction System

## Project Overview

This project builds a **two-stage machine learning system** for loan decision support used by financial institutions.

The system first determines whether a loan application should be approved or rejected. If the application is approved, the system then estimates the appropriate loan amount that can be safely granted to the applicant.

This approach reflects how many real-world banking systems work, where eligibility is evaluated first before determining the loan value.

The dataset used in this project is sourced from Kaggle and contains financial and demographic details of loan applicants.

---

# System Architecture

The project follows a **two-stage prediction pipeline**:

### Stage 1: Loan Approval Prediction (Classification)

In this stage, the model predicts whether the loan application should be:

* Approved
* Rejected

This is treated as a **binary classification problem**.

The model analyzes applicant attributes such as:

* Income
* Credit score
* Number of dependents
* Employment status
* Asset values
* Loan term

Output:

```
Loan Status → Approved / Rejected
```

Only applications predicted as **Approved** move to the next stage.

---

### Stage 2: Loan Amount Estimation (Regression)

If the loan application is approved, the second model estimates **how much loan amount can safely be granted**.

This is treated as a **regression problem**.

The regression model predicts:

```
Loan Amount → Continuous numerical value
```

This stage ensures that the approved loan amount is aligned with the applicant's financial capability and risk profile.

---

# Dataset

The dataset contains **4,269 records and 13 features** describing loan applicants.

### Features

| Feature                  | Description                               |
| ------------------------ | ----------------------------------------- |
| loan_id                  | Unique identifier                         |
| no_of_dependents         | Number of dependents                      |
| education                | Education level                           |
| self_employed            | Employment status                         |
| income_annum             | Annual income                             |
| loan_amount              | Requested loan amount                     |
| loan_term                | Loan duration                             |
| cibil_score              | Credit score                              |
| residential_assets_value | Value of residential assets               |
| commercial_assets_value  | Value of commercial assets                |
| luxury_assets_value      | Value of luxury assets                    |
| bank_asset_value         | Value of bank assets                      |
| loan_status              | Loan approval status (Target for Stage 1) |

---

# Machine Learning Pipeline

1. Data Collection
2. Data Cleaning
3. Exploratory Data Analysis
4. Feature Encoding
5. Train/Test Split
6. Stage 1: Classification Model
7. Stage 2: Regression Model
8. Model Evaluation
9. Prediction Pipeline

---

# Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* Jupyter Notebook

---

# Project Structure

```
Loan-Approval-System
│
├── data
│   └── loan_approval_dataset.csv
│
├── notebooks
│   └── loan_analysis.ipynb
│
├── src
│   ├── preprocessing.py
│   ├── classification_model.py
│   └── regression_model.py
│
├── models
│
├── README.md
│
└── requirements.txt
```

---

# Current Progress

✔ Dataset collected from Kaggle
✔ Problem statement defined
✔ Two-stage model architecture designed

---

# Future Work

* Perform detailed exploratory data analysis
* Train classification models for loan approval
* Train regression models for loan amount prediction
* Compare multiple machine learning algorithms
* Deploy the prediction system

---

# Author

Tasnim Shamsuddin
Master's in Computer Science
Aspiring Data Scientist

