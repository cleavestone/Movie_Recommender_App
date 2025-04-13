from src.components.data_ingestion import load_data
from src.components.data_preprocessing import preprocess_data
from src.components.feature_engineering import generate_embeddings
from src.components.create_lance_db import create_db

def main():
    """
    Main function to run the pipeline.
    """
    # Load data from S3
    #data = load_data('beansbucket12', 'lancedb34/movies_metadata.csv')
    
    # Preprocess the data
    #preprocessed_data = preprocess_data(r'Artifacts/raw_data/raw.csv')
    
    # Generate embeddings
    #embeddings = generate_embeddings(r'Artifacts/preprocessed_data/preprocessed_data.csv')
    
    # Create LanceDB
    create_db(r'Artifacts/embeddings/embeddings.csv')


if __name__ == "__main__":
    main()