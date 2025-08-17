import boto3
import pandas as pd
from botocore.config import Config

# Optional: retry and timeout config
my_config = Config(
    retries={'max_attempts': 10},
    connect_timeout=30,
    read_timeout=60
)

bucket_name = "finance-tracker-bucket-nithin"
file_key = "expenses.csv"

# Initialize S3 client
s3 = boto3.client("s3", config=my_config)

# Read object directly into pandas
try:
    obj = s3.get_object(Bucket=bucket_name, Key=file_key)
    df = pd.read_csv(obj['Body'])
    print("✅ File read into pandas successfully!")
    print(df.head())
except Exception as e:
    print(f"❌ Error reading file from S3: {e}")
