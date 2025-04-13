import pandas as pd
import numpy as np
import ast
from src.components.data_preprocessing import preprocess_data
from sentence_transformers import SentenceTransformer
from src.utils.load_yaml_file import load_yaml
import os
import logging

embeddings_folder=load_yaml()['embeddings_folder']

# configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
def calculate_weighted_rate(vote_average, vote_count, min_vote_count=10):
    """
    Calculate the weighted rating of a movie based on its vote average and count.
    used in IMDB website to calculate the rating of a movie
    """
    return (vote_count / (vote_count + min_vote_count)) * vote_average + (min_vote_count / (vote_count + min_vote_count)) * 5.0


def create_features(path:str) -> pd.DataFrame:
    """
    Create a new column called vector by combining genre, overview and title
    """
    try:
        data = pd.read_csv(path, low_memory=False)
        min_vote_count = data['vote_count'].quantile(0.95)
        data['weighted_rate'] = data.apply(lambda row: calculate_weighted_rate(row['vote_average'],
                                            row['vote_count'], min_vote_count), axis=1)
        #Combine multiple columns into a single column named 'combined_info'.
        # This column will be used to generate embeddings later.
        # Each entry in 'combined_info' includes:The movie title, The movie overview The genres (joined as a comma-separated string)
        # and The weighted rating (calculated previously)
        # This ensures that all relevant textual and numerical information about a movie
        #
        data['combined_info'] = data.apply(lambda row: f"""Title: {row['original_title']}
                                            Overview: {row['overview']} 
                                            Genres: {', '.join(row['genres'])}
                                            Rating: {row['weighted_rate']}""", axis=1).astype(str)
        logging.info('combined_info column successfully created')
        return data
        
    except Exception as e:
        print(f"Error creating features: {e}")

    


def generate_embeddings(path:str) -> pd.DataFrame:
    """
    Generate embeddings for the combined info column using sentence transformers.
    """
    data= create_features(path)
    try:
        # Load a pre-trained Sentence-Transformer model (lighter, faster)
        model = SentenceTransformer('paraphrase-MiniLM-L6-v2')
        logging.info('model successfully downloaded ')
       
        logging.info('generating embeddings for combine_info column')
        # Generate embeddings for a batch of sentences
        embeddings = model.encode(data['combined_info'].tolist(), show_progress_bar=False)
        logging.info("Embeddings completed")

        # Convert the embeddings to a DataFrame
        data['vector']=embeddings.tolist()
        logging.info('saved embdeddings to data frame')

        # Convert the 'embeddings' column from string representation of lists to actual lists of numbers
        data['vector'] = data['vector'].apply(lambda x: ast.literal_eval(x) if isinstance(x, str) else x)
        os.makedirs(embeddings_folder,exist_ok=True)
        csv_path=os.path.join(embeddings_folder,'embeddings.csv')
        data.to_csv(csv_path,index=False)
        return data
    
    except Exception as e:
        print(f"Error generating embeddings: {e}")




