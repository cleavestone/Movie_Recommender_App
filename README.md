# 🎬 Movie Recommender App

A semantic movie recommendation system powered by **LanceDB**, **Sentence Transformers**, and **Streamlit**. This app suggests movies based on the similarity of user queries to movie descriptions using vector embeddings.

---

## 🚀 Features

- ✅ Loads movie metadata from an S3 bucket
- ✅ Preprocesses and cleans the dataset
- ✅ Generates sentence embeddings using Sentence Transformers
- ✅ Stores vector embeddings in a LanceDB vector database
- ✅ Retrieves top-k similar movies via semantic search
- ✅ Clean and interactive UI using Streamlit

---
## 🧰 Tech Stack

- **Python 3.10+**
- **Streamlit** – For the interactive web interface
- **LanceDB** – Used for vector similarity search
- **SentenceTransformers** – To generate sentence-level embeddings for movie descriptions
- **pandas**, **numpy** – For data manipulation and preprocessing
- **DVC + S3** – For data versioning and managing large files remotely

## 🏗️ Project Structure
```
Movie_Recommender_App/
├── App.py                        # Streamlit main application
├── config.yaml                   # Configuration file (e.g., LanceDB URI)
├── moviees.jpg                   # Banner image
├── requirements.txt              # List of dependencies
│
├── Artifacts/
│   └── embeddings/
│       └── embeddings.csv        # Precomputed embeddings + metadata
│
└── src/
    ├── components/
    │   ├── create_lance_db.py        # Creates and populates LanceDB
    │   ├── data_ingestion.py         # Loads data from S3
    │   ├── data_preprocessing.py     # Cleans and preprocesses data
    │   └── feature_engineering.py    # Generates sentence embeddings
    │
    ├── pipeline/
    │   └── pipeline.py               # Main pipeline runner
    │
    └── utils/
        └── load_yaml_file.py        # Helper to load config

