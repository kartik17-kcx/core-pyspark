# 📘 PySpark Projects & Examples Repository

Explanation of all PySpark RDD, DataFrame and SQL examples present in this project are available at  
👉 **[Apache PySpark Tutorial](https://sparkbyexamples.com/pyspark-tutorial/)**  
All these examples are coded in Python language and tested in a local development environment using PySpark.

---

# 🧭 Table of Contents

1. [PySpark Basic Examples](#pyspark-basic-examples)  
2. [PySpark DataFrame Examples](#pyspark-dataframe-examples)  
3. [PySpark SQL Functions](#pyspark-sql-functions)  
4. [PySpark Datasources](#pyspark-datasources)  
5. [End-to-End PySpark Projects (Beginner → Intermediate)](#end-to-end-pyspark-projects)

---

# 🔹 PySpark Basic Examples

- How to create SparkSession  
- PySpark – Accumulator  
- PySpark – Repartition vs Coalesce  
- PySpark – Broadcast variables  
- PySpark – `repartition()` vs `coalesce()`  
- PySpark – Parallelize  
- PySpark – RDD  
- PySpark – Web/Application UI  
- PySpark – SparkSession  
- PySpark – Cluster Managers  
- PySpark – Install on Windows  
- PySpark – Modules & Packages  
- PySpark – Advantages  
- PySpark – Features  
- PySpark – What is it? & Who uses it?

---

# 🔹 PySpark DataFrame Examples

- PySpark – Create a DataFrame  
- PySpark – Create an empty DataFrame  
- PySpark – Convert RDD to DataFrame  
- PySpark – Convert DataFrame to Pandas  
- PySpark – StructType & StructField  
- PySpark – Using Row on DataFrame and RDD  
- Select columns from PySpark DataFrame  
- PySpark `collect()` – Retrieve full data  
- PySpark `withColumn()` to update/add columns  
- PySpark `where` filter function  
- PySpark `distinct()` to drop duplicates  
- PySpark `orderBy()` and `sort()` explained  
- PySpark `groupBy()` with examples  
- PySpark Join types explained  
- PySpark Union and UnionAll  
- PySpark UDF (User Defined Functions)  
- PySpark `flatMap()` transformation  
- PySpark `map()` transformation  

---

# 🔹 PySpark SQL Functions

- PySpark Aggregate Functions  
- PySpark Window Functions  

---

# 🔹 PySpark Datasources

- Read CSV into DataFrame  
- Read & Write Parquet Files  

---

# 🚀 End-to-End PySpark Projects

This section contains real-world projects built using PySpark. They cover beginner to intermediate levels and are suitable for practicing **ETL, analytics, RDDs, DataFrames, SQL, and Big Data concepts**.

---

## 1️⃣ Movie Ratings Analysis (Beginner — DataFrames)

**Dataset:** MovieLens Small Dataset  
**Skills:** DataFrames, joins, aggregations

### 📌 Tasks
- Load `movies.csv` and `ratings.csv`
- Top 10 highest-rated movies  
- Most-rated movies  
- Average rating per genre  
- Most active users  

**Spark Concepts:**  
`select`, `filter`, `groupBy`, `agg`, `orderBy`, joins

---

## 2️⃣ Apache Log File Analyzer (Beginner — RDD + DataFrame)

**Dataset:** Apache access.log  
**Skills:** RDD parsing, regex extraction

### 📌 Tasks
- Count total requests  
- Count hits per URL  
- Extract IP addresses  
- Peak traffic hour  

**Spark Concepts:**  
RDD → DataFrame conversion, `map`, `filter`, `reduceByKey`, SQL queries

---

## 3️⃣ Retail Sales ETL Pipeline (Intermediate — DataFrames)

**Dataset:** Kaggle Retail Sales  
**Skills:** Data cleaning, ETL, aggregations

### 📌 Steps
- Read CSV from local/S3  
- Clean missing values  
- Normalize data types  
- Enrich with profit & margin  
- Aggregate by region, category, segment  
- Write clean data to Parquet  

**Spark Concepts:**  
ETL pipeline, window functions, Parquet writing, partitioning

---

## 4️⃣ NYC Taxi Trip Analytics (Intermediate — Big Data)

**Dataset:** NYC Taxi Trip Data  
**Skills:** Big Data analytics, Parquet optimization

### 📌 Tasks
- Load multi-GB taxi parquet data  
- Avg trip distance & fare per borough  
- Peak pickup hours  
- Outlier detection  

**Spark Concepts:**  
Predicate pushdown, column pruning, large DataFrame optimization

---

## 5️⃣ Airbnb Price Predictor (MLlib)

**Dataset:** Airbnb Listings  
**Skills:** Machine Learning with Spark MLlib

### 📌 Build
- Clean dataset  
- One-hot encoding  
- Train ML pipeline  
- Predict price using Linear Regression or Random Forest  
- Evaluate RMSE  

**Spark Concepts:**  
VectorAssembler, ML Pipelines, train-test split

---

## 6️⃣ Real-Time Streaming Log Processor (Structured Streaming)

**Dataset:** Kafka → Spark Streaming  
**Skills:** Real-time pipelines

### 📌 Workflow
- Kafka producer → JSON logs  
- Spark Streaming processes logs  
- Compute:
  - Event count  
  - Errors per minute  
  - Avg response time  
- Output results to console/parquet  

**Spark Concepts:**  
Structured Streaming, window aggregations, triggers

---

## 7️⃣ YouTube/Twitter Trending Analysis (API + PySpark)

**Dataset:** YouTube/Twitter API  
**Skills:** JSON ingestion + analysis

### 📌 Tasks
- Fetch trending videos/tweets  
- Normalize nested JSON  
- Extract:
  - Most-used hashtags  
  - Trending categories  
  - Top creators  

**Spark Concepts:**  
`explode`, nested JSON parsing, aggregations

---

# 🎯 Repository Goal

This repository is designed to act as a **complete learning tracker** for PySpark, covering:

✔ RDDs  
✔ DataFrames  
✔ SQL & Window functions  
✔ ETL Pipelines  
✔ Big Data projects  
✔ Streaming  
✔ Machine Learning  
