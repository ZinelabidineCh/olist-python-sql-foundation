# Phase 1: Local Data Engineering & Exploratory Analysis (Python/SQL)

## 🎯 Objective
This was the first phase of my Olist E-commerce trilogy. The goal was to build a local data foundation by ingesting raw datasets into a relational database and performing deep-dive exploratory data analysis (EDA) to uncover the "why" behind sales and satisfaction trends.

## 📦 Data Source
The dataset consists of ~100k orders from 2016 to 2018 in Brazil, provided by Olist.

## 🏗️ Technical Architecture (The Ground Floor)
This project focuses on **Local Data Engineering**. I developed a modular pipeline of Python scripts to automate the ingestion and analysis process:

1.  **`01_create_database.py`**: Uses `SQLAlchemy` to programmatically read 9 CSV files and build a structured SQLite database.
2.  **`02_customer_analysis.py`**: SQL-driven analysis of customer geographic concentration.
3.  **`03_product_revenue_analysis.py`**: Financial analysis using multi-table joins to identify top-performing categories.
4.  **`04_satisfaction_analysis.py`**: Advanced SQL query using `JULIANDAY` to calculate average delivery times per review score.
5.  **`05_visualize_customer_distribution.py`**: Statistical visualization using `Seaborn` and `Matplotlib`.

## 📊 Key Findings
* **Market Concentration:** São Paulo (SP) is the primary hub, followed by RJ and MG.
* **Revenue Leaders:** `beleza_saude` and `relogios_presentes` emerged as the most profitable categories.
* **Logistics & Satisfaction:** I discovered a critical correlation—1-star reviews are directly tied to longer delivery windows (calculated as an average of days between purchase and delivery).

## 🚀 The Journey Continues
After mastering the local analysis, I moved this project forward into two more advanced phases:
* **[Phase 2: Business Intelligence (Power BI)](https://github.com/ZinelabidineCh/olist-bi-powerbi-dashboard)** - Turning these insights into an executive-level interactive dashboard.
* **[Phase 3: Production Cloud ELT (GCP)](https://github.com/ZinelabidineCh/olist-elt-pipeline-gcp-looker)** - Scaling the entire pipeline to the cloud using BigQuery and Dataform.

## 💻 Tech Stack
- **Languages:** Python, SQL (SQLite)
- **Libraries:** Pandas, SQLAlchemy, Seaborn, Matplotlib
