# ⚙️ Steel Sulphur Prediction Model
## 🔬 Machine Learning-Based Predictive Model for DeSulphurization (DS) Optimization
## 📌 **Overview**

The Steel Sulphur Prediction Model is a terminal-based machine learning project developed to predict the Sulphur percentage (DS_S) in molten steel during the DeSulphurization (DS) process.
This project leverages Linear Regression and data optimization techniques to enhance process control, minimize downgraded heats, and ensure consistent product quality in steel manufacturing.
---
🧩 Problem Statement

High Sulphur content in steel leads to downgrading, affecting delivery schedules and sales performance.
Mr. Suresh Babu sought an analytics-driven solution to accurately predict and control Sulphur levels during the DS process.

The goal:

Predict Sulphur levels precisely before and after desulphurization.

Optimize reagent usage and reduce reprocessing.

Improve delivery timelines and production efficiency.
---

# 🎯 Objectives

✅ Improve predictive accuracy of Sulphur percentage.
✅ Enhance control over the DeSulphurization process.
✅ Minimize downgraded heats and losses.
✅ Support process engineers with actionable data insights.
---

#⚗️ About the DS (DeSulphurization) Process

The DeSulphurization process (DS) removes excess Sulphur from molten steel to meet quality standards.

Traditional Reagents: Calcium Carbide (CaC₂) and Magnesium (Mg)

Modern Approach: Limestone, as an eco-friendly and cost-effective substitute

Purpose: Lower Sulphur levels improve steel strength, ductility, and weldability
---

#🧠 Data Optimization Pipeline

Your model applies a clean, optimized data science workflow for maximum reliability:

🧹 Null Value Removal: Ensures consistent and complete input data.

📊 Feature Selection: Uses relevant variables like temperature, reagent amounts, and chemistry.

⚙️ Scaling: Applies StandardScaler for normalized feature distribution.

🧩 Splitting: 67%-33% split between training and testing datasets.

🧠 Model Training: Uses Linear Regression to fit the data.

🧾 Evaluation: Measures performance using MSE, R², and a custom “Hit Rate” metric (±0.003 tolerance).
---

#🚀 Features

🔹 Predictive Modeling – Estimates final Sulphur (DS_S) values with optimized accuracy.
🔹 Linear Regression Algorithm – Establishes a direct relationship between steel composition and Sulphur outcomes.
🔹 Automated Evaluation – Computes MSE, R², and Hit Rate for both training and test sets.
🔹 Pickle-Based Model Saving – Exports the model for future reuse and deployment.
🔹 Terminal Output – Lightweight, fully functional command-line project (no frontend required).
---

# 🧮 Algorithm Used – Linear Regression

A supervised learning algorithm that learns from labeled datasets (known output values).

Fits an optimized linear equation to map process parameters (inputs) to predicted Sulphur content (output).

Enables interpretability and continuous improvement in process analytics.
---


#🛠️ Tech Stack

Python, Pandas, NumPy, Scikit-learn, Pickle
Dataset: DSDataLastThreeMonths.csv
---

#💻 Run Instructions

pip install -r requirements.txt
python sulphur_prediction.py
---

#🧾 Outcome

✅ Improved prediction accuracy
✅ Better DS process control
✅ Reduced downgraded heats
---
