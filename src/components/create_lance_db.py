import pandas as pd
import lancedb
from src.utils.load_yaml_file import load_yaml
import os
import ast

uri=load_yaml()['uri']

def create_db(path):
    """
    Creates a lance database from the embeddings and metadata
    """
    os.makedirs(uri, exist_ok=True)
    df = pd.read_csv(path)
    df['vector']=df['vector'].apply(ast.literal_eval)
    db = lancedb.connect(uri)

    if "movies" in db.table_names():
        db.drop_table("movies")

    table1 = db.create_table("movies",df)


    

