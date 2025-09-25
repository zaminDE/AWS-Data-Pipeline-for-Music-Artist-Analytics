import json
import boto3
import requests
import csv
import io
from datetime import datetime

s3 = boto3.client('s3')
bucket_name = "data-lake-zamin"
staging_prefix = "staging/"

def lambda_handler(event, context):
    try:
        # 🎯 Example: MusicBrainz API (Beatles ka artist data)
        url = "https://musicbrainz.org/ws/2/artist?query=beatles&fmt=json"
        headers = {
            "User-Agent": "zamin-music-pipeline/1.0 (zamin@example.com)"  # MusicBrainz requires this
        }
        
        response = requests.get(url, headers=headers, timeout=30)
        
        if response.status_code != 200:
            raise Exception(f"API call failed with status {response.status_code}")
        
        data = response.json()
        
        # 📊 Extract artists list
        artists = data.get("artists", [])
        
        if not artists:
            raise Exception("❌ No artist data found in API response")
        
        # 📝 Convert to CSV using csv module
        # Pick some keys (columns) you want to store
        fields = ["id", "name", "type", "score"]  
        
        output = io.StringIO()
        writer = csv.DictWriter(output, fieldnames=fields)
        writer.writeheader()
        
        for artist in artists:
            row = {field: artist.get(field, "") for field in fields}
            writer.writerow(row)
        
        csv_data = output.getvalue()
        
        # 📂 Unique partitioned filename
        timestamp = datetime.utcnow().strftime("%Y%m%d%H%M%S")
        year = datetime.utcnow().strftime("%Y")
        month = datetime.utcnow().strftime("%m")
        
        file_name = f"{staging_prefix}year={year}/month={month}/artists_{timestamp}.csv"
        
        # 💾 Upload CSV to S3
        s3.put_object(
            Bucket=bucket_name,
            Key=file_name,
            Body=csv_data,
            ContentType="text/csv"
        )
        
        return {
            "statusCode": 200,
            "body": f"✅ CSV saved to {file_name}"
        }
    
    except Exception as e:
        return {
            "statusCode": 500,
            "body": f"❌ Error: {str(e)}"
        }
