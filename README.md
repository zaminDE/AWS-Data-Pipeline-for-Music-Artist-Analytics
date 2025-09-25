# 🎵 AWS Music Data Pipeline

This project showcases a serverless AWS Data Engineering Pipeline for the music industry, ingesting raw API data into S3, processing it with AWS Glue, and querying it via Athena for analytics.

## 📌 Problem Statement

Music industry stakeholders need insights on:
- Most popular artists.
- Demand for artist types (solo, group, band).
- Popularity trends over time.

Raw CSV/JSON data from music websites requires a robust ETL pipeline for analytics.

## ✅ Solution Overview

The pipeline automates:
- Data ingestion via Lambda.
- Raw data storage in S3 (Staging Layer).
- Schema discovery with AWS Glue Crawlers.
- Data cleaning and transformation using AWS Glue ETL (PySpark).
- Curated data storage in S3 (Data Warehouse Layer).
- SQL-based querying with Amazon Athena.

## 🏗️ Architecture Flow

- **API (Music Data Source)** → Provides raw JSON/CSV data.
- **Amazon EventBridge** → Triggers Lambda on schedule.
- **AWS Lambda** → Fetches and uploads data to S3 staging.
- **Amazon S3 (Staging Layer)** → Stores raw data.
- **AWS Glue Crawler (Staging)** → Detects schema, updates Glue Catalog.
- **AWS Glue ETL Job (PySpark)** → Cleans, deduplicates, converts to Parquet.
- **Amazon S3 (Data Warehouse Layer)** → Stores curated data.
- **AWS Glue Crawler (Curated)** → Updates schema for curated data.
- **Amazon Athena** → Enables SQL queries for analysis.

## 📊 Architecture Diagram

![Architecture Diagram](architecture-diagram.png)

## ⚡ Lambda Function

The Lambda function ingests data, saving it to S3 (staging). It currently uses sample JSON but can integrate with APIs like Spotify.

### Example Code Snippet
```python
s3.put_object(
    Bucket="your-bucket-name",
    Key="staging/music_data.json",
    Body=json.dumps(data)
)
```

## 🚀 Deployment Steps

1. Create an S3 bucket with `staging/` and `data-warehouse/` folders.
2. Create a Lambda function, upload `lambda_function.py`.
3. Assign an IAM Role with S3 access.
4. Set up an EventBridge Rule to trigger Lambda on schedule.
5. Run a Glue Crawler on `staging/` to detect schema.
6. Create a Glue ETL Job to transform data into `data-warehouse/`.
7. Run a Glue Crawler on `data-warehouse/` to update schema.
8. Query curated data in Athena.

## 📂 Repository Contents

- `lambda_function.py` → Lambda code for ingestion.
- `architecture-diagram.png` → Pipeline architecture diagram.
- `README.md` → Project documentation.

## 📊 Business Impact

- Transforms raw data into analytics-ready datasets.
- Automates ETL with serverless AWS services.
- Enables stakeholders to:
  - Identify top artists for marketing.
  - Analyze artist type distribution.
  - Track popularity trends.
- Scalable for large data volumes.

## 🔮 Future Enhancements

- Integrate real-time APIs for live data.
- Automate reporting with QuickSight/Power BI.
- Optimize S3 partitioning for faster Athena queries.
- Add CI/CD with AWS CodePipeline.

## ✍️ Author
Muhammad Zamin

## 📌 End-to-End AWS Data Engineering Pipeline
Ingestion → Processing → Querying.
