# 🎵 AWS Music Data Pipeline (Minimal)

This repository demonstrates a minimal AWS Data Pipeline for ingesting music data into Amazon S3 using AWS Lambda, with an architecture diagram explaining the complete flow.

## 📌 Architecture Overview

The pipeline is designed as follows:

- **API (Music Data Source)** → Provides raw music data (JSON/CSV).
- **Amazon EventBridge** → Schedules/triggers the Lambda function.
- **AWS Lambda** → Fetches data from the API and stores it into S3.
- **Amazon S3 (Staging Layer)** → Stores raw ingested data.
- **AWS Glue Crawler (Staging)** → Discovers schema from staging data.
- **AWS Glue ETL Job (PySpark)** → Cleans, transforms, and deduplicates data.
- **Amazon S3 (Data Warehouse Layer)** → Stores curated/analytics-ready data.
- **AWS Glue Crawler (Curated)** → Updates schema in Glue Catalog.
- **Amazon Athena** → Queries curated data using SQL.

## ⚡ Lambda Function

The `lambda_function.py` script is responsible for data ingestion. Currently, it saves sample JSON data into S3. It can be extended to pull data from external APIs such as Spotify or music websites.

    Key="staging/music_data.json",
    Body=json.dumps(data)
)
