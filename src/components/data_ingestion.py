import boto3
import pandas as pd
from io import StringIO
from src.utils.load_yaml_file import load_yaml
import logging
import os

folder_path=load_yaml()["raw_data_path"]


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def load_data(bucket: str, key: str):
    """
    Load data from an S3 bucket into a pandas DataFrame 
    """
    try:
        s3 = boto3.client('s3')
        logging.info("Downloading from S3 bucket")
        response = s3.get_object(Bucket=bucket, Key=key)
        csv_content = response['Body'].read().decode('utf-8')

        df = pd.read_csv(StringIO(csv_content), low_memory=False)
    
        # create directory if it does not exist
        os.makedirs(folder_path, exist_ok=True)
        csv_path = os.path.join(folder_path, 'raw.csv')

        # Save file
        df.to_csv(csv_path, index=False)
        return df
    except Exception as e:
        print(f"Error loading data: {e}")
        

    
    

