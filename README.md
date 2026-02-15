# E-Commerce Intelligence Engine: RFM & Churn Pipeline

## 🚀 Overview
This repository contains an end-to-end data engineering pipeline that transforms raw Brazilian e-commerce data (Olist) into a structured Feature Store for Machine Learning and Business Intelligence.

The engine calculates **RFM Metrics** to segment customers, allowing businesses to differentiate between "Champion" users and those at risk of churning.



## 🛠️ Tech Stack
* **Language:** Python 3.12
* **Database:** PostgreSQL (Relational Storage)
* **Orchestration:** SQLAlchemy & Psycopg2
* **Data Processing:** Pandas (Feature Engineering)
* **Visualization:** Matplotlib & Seaborn
* **Environment:** Dotenv for secure credential management

## 🏗️ System Architecture
1.  **Automated Ingestion:** A robust script that cleans filenames and maps CSVs to a PostgreSQL schema, ensuring data grain integrity.
2.  **Analytical Layer:** Advanced SQL queries (using CTEs) that aggregate payments at the order level to prevent value duplication.
3.  **Feature Store:** A processed CSV output containing Recency, Frequency, and Monetary scores for every unique customer.
4.  **Intelligence Layer:** Visualizations that map the "Money Map" of the business using logarithmic scaling for high-variance spend data.

## 📊 Key Insights
* **One-Purchase Reality:** The data reveals that the majority of the customer base consists of one-time buyers, highlighting a massive opportunity for retention-focused Agentic AI.
* **Logarithmic Spend:** Customer spending follows a power-law distribution, with "Whale" customers spending up to 100x more than the average user.

## 🏃 How to Run
1.  **Environment Setup:**
    ```bash
    python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```
2.  **Database Ingestion:**
    ```bash
    python src/db_ingest.py
    ```
3.  **Generate Analytics:**
    ```bash
    python src/analytics_queries.py
    python src/visualize_rfm.py
    ```

## 📈 Future Roadmap
* **Agentic AI Integration:** Automatically generating personalized email campaigns for the "Champion" segment.
* **Churn Prediction:** Training a Random Forest model on the RFM features to predict the probability of a user leaving.
