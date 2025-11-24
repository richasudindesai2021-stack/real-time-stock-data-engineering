Got it — I will rewrite the **entire README** again from scratch,
**matching Jay’s repository structure exactly**,
**but updated to reflect YOUR project**, including:

✔ only **AAPL, GOOGL, AMZN** streamed
✔ same folder structure as Jay
✔ clean, professional format
✔ ready to paste into GitHub

Here is your final polished README.md:

---

# 📈 Real-Time Stock Market Analytics Pipeline — Modern Data Stack Project

This project showcases a complete **real-time data engineering pipeline** using the **Modern Data Stack (MDS)**.
It streams live stock market data, lands it in object storage, orchestrates ingestion into Snowflake, transforms it using dbt, and visualizes insights in Power BI — all fully automated and containerized.

---

## 🏗️ Architecture Overview

```
Finnhub API 
   → Kafka Producer 
   → Kafka Broker 
   → Kafka Consumer 
   → MinIO (Bronze Storage)
   → Airflow DAG 
   → Snowflake (Bronze → Silver → Gold via dbt)
   → Power BI Analytics Dashboard
```

---

## ⚡ Tech Stack

### **Data Ingestion & Streaming**

* Python (API ingestion)
* Finnhub Stock Market API
* Apache Kafka (Producer + Consumer)

### **Object Storage**

* MinIO (S3 compatible)

### **Orchestration**

* Apache Airflow (managed in Docker)

### **Warehouse & Transformations**

* Snowflake Cloud Data Warehouse
* dbt Core (Bronze → Silver → Gold models)

### **Infrastructure**

* Docker & Docker Compose
* Postgres (Airflow backend)

### **Visualization**

* Power BI Dashboard connected to Snowflake

---

## 📌 Key Features

* Real-time streaming of live stock prices from Finnhub API
* Kafka pipeline (Producer → Broker → Consumer)
* Storage of raw JSON into MinIO (Bronze layer)
* Automated ingestion to Snowflake via Airflow
* dbt transformations for clean Silver & analytical Gold layer
* Power BI dashboards built directly on Snowflake Gold models
* Fully containerized using Docker Compose

⚠️ **Note:**
In this project run, data was successfully streamed for:

* **AAPL**
* **GOOGL**
* **AMZN**

TSLA and MSFT were configured but **not streamed during ingestion time** and therefore do not appear in downstream layers.

---

## 📂 Repository Structure

*(Matches Jay’s structure exactly as you requested)*

```
real-time-stocks-mds/
│
├── infra/
│   ├── docker-compose.yml              # Kafka, Zookeeper, Airflow, MinIO, Postgres
│   ├── producer/
│   │   └── producer.py                 # Fetches API data → Kafka
│   ├── consumer/
│   │   └── consumer.py                 # Kafka consumer → MinIO
│   └── dags/
│       └── minio_to_snowflake.py       # Airflow DAG for Snowflake ingestion
│
├── dbt_stocks/
│   ├── models/
│   │   ├── bronze/
│   │   │   ├── bronze_stg_stock_quotes.sql
│   │   │   └── sources.yml
│   │   ├── silver/
│   │   │   └── silver_clean_stock_quotes.sql
│   │   └── gold/
│   │       ├── gold_candlestick.sql
│   │       ├── gold_kpi.sql
│   │       └── gold_treechart.sql
│   ├── macros/
│   └── dbt_project.yml
│
├── powerbi/
│   └── stock_dashboard.pbix
│
├── requirements.txt
└── README.md
```

---

## 🚀 Implementation Steps

### **1. Kafka Setup (Docker)**

* `docker-compose.yml` initializes Kafka, Zookeeper, Airflow, MinIO, Postgres.
* Kafka topic created: `stocks-quotes`

---

### **2. Live Market Producer (Python)**

* Uses Finnhub API to fetch real-time stock prices.
* Streams JSON records into Kafka every 6 seconds.
* Symbols used: AAPL, GOOGL, AMZN (TSLA & MSFT not streamed this time).

---

### **3. Kafka Consumer → MinIO (Bronze Layer)**

* Consumes messages from Kafka
* Saves each message as a JSON file to MinIO:

```
s3://bronze-transactions/<symbol>/<timestamp>.json
```

---

### **4. Airflow Orchestration**

DAG: `minio_to_snowflake.py`
Runs every 1 minute to:

1. Download raw JSON files from MinIO
2. Upload them to Snowflake internal stage
3. Run a `COPY INTO` into Snowflake Bronze table

---

### **5. Snowflake Setup**

Created:

* Warehouse: `COMPUTE_WH`
* Database: `STOCKS_MDS`
* Schema: `COMMON`
* Table: `BRONZE_STOCK_QUOTES_RAW`

Contains raw JSON data from MinIO.

---

### **6. dbt Transformations**

#### **Bronze → Silver**

Bronze:

* Flatten raw JSON fields
* Cast datatypes
* Standardize naming

Silver:

* Clean up nulls
* Fix timestamp formatting
* Calculate derived metrics

#### **Gold Models**

* **gold_kpi** — key price changes & percent movement
* **gold_candlestick** — OHLC candlestick chart data
* **gold_treechart** — aggregated stock trend view

---

## 📊 Power BI Dashboard

Connected directly to Snowflake Gold layer via DirectQuery.

Includes:

* Candlestick OHLC chart
* Tree map of price trends
* KPIs & metrics
* Real-time comparison visuals for AAPL, AMZN, GOOGL

---

## 🏁 Final Outcomes

✔ Fully functional real-time data pipeline
✔ Raw → Bronze → Silver → Gold modeling complete
✔ Automated Airflow ingestion
✔ dbt transformations executed successfully
✔ Analytics dashboard built in Power BI
✔ Professional, portfolio-ready data engineering project

---

## 👩‍💻 Author

**Richa Desai**
USC MSBA | Data Engineering | Analytics | Cloud
*www.linkedin.com/in/richadesaiusc*


