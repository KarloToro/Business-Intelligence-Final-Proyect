# 📊 BI Project — Fictional Company with Synthetic Data

A comprehensive **Business Intelligence** solution developed for a fictional company using **Python**, **Power BI**, and data mining techniques. The project covers the entire analytics pipeline, from reproducible synthetic data generation to building a dimensional data warehouse, executive dashboards, and analytical models that support business decision-making.

## 🚀 Project Objective

Design a Business Intelligence solution capable of transforming synthetic transactional data into actionable business insights, answering key managerial questions related to sales, customers, products, promotions, customer churn, segmentation, market basket analysis, and demand forecasting.

## 🧩 Main Components

| Part | Focus                | Expected Outcome                                                    |
| ---- | -------------------- | ------------------------------------------------------------------- |
| 0    | Data Generation      | Reproducible synthetic datasets with controlled data quality issues |
| 1    | Analytical Data Mart | Star schema dimensional model and ETL process                       |
| 2    | Data Visualization   | Executive Power BI dashboard and business insights                  |
| 3    | Classification       | Customer churn or propensity prediction                             |
| 4    | Segmentation         | Customer clustering using RFM analysis and K-Means                  |
| 5    | Association Analysis | Market basket rules for cross-selling recommendations               |
| 6    | Regression           | Sales or demand forecasting                                         |

## 🛠️ Technology Stack

* **Python 3.10+**
* **Jupyter Notebooks**
* **Pandas / NumPy**
* **Matplotlib / Seaborn / Plotly**
* **scikit-learn**
* **mlxtend**
* **Faker**
* **Power BI Desktop**
* **Git / GitHub**

## 📁 Repository Structure

```text
bi-project/
├── README.md
├── requirements.txt
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/
│   ├── 00_data_generation.ipynb
│   ├── 01_datamart_etl.ipynb
│   ├── 02_visualization.ipynb
│   ├── 03_classification.ipynb
│   ├── 04_segmentation.ipynb
│   ├── 05_association.ipynb
│   └── 06_regression.ipynb
├── powerbi/
├── prompts/
├── report/
└── docs/
```

## 🔁 Reproducibility

The project can be fully reproduced by executing the notebooks in the following order:

```bash
pip install -r requirements.txt
```

Then launch Jupyter and run:

```text
00_data_generation.ipynb
01_datamart_etl.ipynb
02_visualization.ipynb
03_classification.ipynb
04_segmentation.ipynb
05_association.ipynb
06_regression.ipynb
```

All datasets are entirely synthetic and generated using a fixed random seed to ensure reproducibility and consistent results.

## 📈 Expected Deliverables

* Analytical data mart based on a star schema.
* Executive dashboard built with Power BI.
* DAX measures for sales, profit margin, average ticket size, and business growth.
* Classification model for customer churn prediction.
* Customer segments with differentiated business strategies.
* Association rules for cross-selling opportunities.
* Sales or demand forecasting model.
* Final report including findings, recommendations, and ethical considerations.

## 🔐 Data Disclaimer

This repository does not contain any real personal or corporate data. All datasets are synthetic and were generated exclusively for academic purposes.
