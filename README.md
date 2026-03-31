# Pokémon ETL Pipeline with Airflow

## Project Overview

This project implements a complete **data engineering pipeline** that extracts Pokémon data from the public PokéAPI, transforms it into structured tables, and loads it into a PostgreSQL database.

The pipeline is orchestrated using **Apache Airflow** and deployed using **Docker containers** to simulate a production-style environment.

This project demonstrates core data engineering concepts including:

* ETL pipeline development
* API data ingestion
* Data transformation with Python
* PostgreSQL data storage
* Workflow orchestration with Airflow
* Containerized infrastructure using Docker

---

# Architecture

```
          PokéAPI
             │
             ▼
        Extract (Python)
             │
             ▼
        Transform
             │
             ▼
           Load
             │
             ▼
        PostgreSQL
             ▲
             │
          Airflow
     (pipeline scheduler)
```

---

# Tech Stack

**Languages**

* Python

**Data Engineering Tools**

* Apache Airflow
* PostgreSQL
* Docker
* SQLAlchemy
* Pandas

**API**

* PokéAPI

---

# Pipeline Workflow

The ETL pipeline consists of three primary stages:

### Extract

Data is retrieved from the PokéAPI using HTTP requests.

Information collected includes:

* Pokémon name
* height
* weight
* stats
* types

---

### Transform

The raw JSON response is transformed into structured datasets:

**pokemon table**

| pokemon_id | name | height | weight |

**pokemon_stats table**

| pokemon_id | stat_name | base_stat |

**pokemon_types table**

| pokemon_id | type_name |

---

### Load

Transformed data is loaded into PostgreSQL using **UPSERT logic** to prevent duplicate records.

---

# Airflow DAG

Airflow orchestrates the pipeline through a DAG called:

```
pokemon_etl_pipeline
```

The DAG runs the ETL process on a scheduled basis.

---

# Running the Project

## Clone the repository

```
git clone https://github.com/yourusername/pokemon-etl-airflow-pipeline.git
cd pokemon-etl-airflow-pipeline
```

---

## Start the infrastructure

```
docker compose up -d
```

---

## Access Airflow

Open:

```
http://localhost:8081
```

Login:

```
username: admin
password: admin
```

---

## Trigger the pipeline

From the Airflow UI:

```
pokemon_etl_pipeline → Trigger DAG
```

---

# Database Schema

### pokemon

| Column     | Description       |
| ---------- | ----------------- |
| pokemon_id | unique Pokémon ID |
| name       | Pokémon name      |
| height     | height value      |
| weight     | weight value      |

---

### pokemon_stats

| Column     | Description |
| ---------- | ----------- |
| pokemon_id | foreign key |
| stat_name  | stat type   |
| base_stat  | stat value  |

---

### pokemon_types

| Column     | Description  |
| ---------- | ------------ |
| pokemon_id | foreign key  |
| type_name  | Pokémon type |

---

# Example Output

After execution the database contains normalized Pokémon data ready for analytics or downstream pipelines.

---

# Key Learning Outcomes

This project demonstrates practical experience with:

* Building production-style ETL pipelines
* Data ingestion from external APIs
* Containerized data engineering workflows
* Airflow orchestration
* Relational data modeling

---

# Future Improvements

Potential upgrades include:

* breaking ETL into multiple Airflow tasks
* adding data validation checks
* implementing retry policies
* adding monitoring and alerting
* scaling with distributed Airflow executors

---

# Author

Efe Dincaslan

Virginia Tech
Cybersecurity Management & Analytics
