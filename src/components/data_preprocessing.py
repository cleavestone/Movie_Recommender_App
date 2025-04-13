from src.components.data_ingestion import load_data
import pandas as pd
import numpy as np
import ast
import os
from sentence_transformers import SentenceTransformer
from src.utils.load_yaml_file import load_yaml


drop_columns=load_yaml()['columns_to_drop']
output_folder=load_yaml()['preprocessed_data_path']

def preprocess_data(path:str) ->  pd.DataFrame:
    """
    Preprocess the data by removing duplicates, dropping columns, 
    handling missing values , clean genre and popularity
    """
    try:
        data = pd.read_csv(path, low_memory=False)
        # Remove duplicates
        data= data.drop_duplicates()
        # Drop columns
        data = data[drop_columns]

        # Handle missing values by dropping
        data = data.dropna()

        # clean genre column by extracting the names
        data['genres']=data['genres'].apply(lambda x: [i['name'] for i in ast.literal_eval(x)] if isinstance(x,str) else x)

        # clean popularity , convert values to float
        data['popularity']=data['popularity'].astype('float')
        
        os.makedirs(output_folder,exist_ok=True)
        csv_path=os.path.join(output_folder,'preprocessed_data.csv')
        
        data.to_csv(csv_path,index=False)
        return data


    except Exception as e:
        print(f"Error preprocessing data: {e}")







