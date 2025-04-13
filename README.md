# 🎬 Movie Recommender App

A semantic movie recommendation system powered by **LanceDB**, **Sentence Transformers**, and **Streamlit**. This app suggests movies based on the similarity of user queries to movie descriptions using vector embeddings.

---

## 🚀 Features

- 🔍 Semantic search with vector embeddings
- 💬 Natural language query support
- 🧠 Precomputed embeddings using Sentence Transformers
- 💾 Vector database with LanceDB
- 🖼️ Clean and interactive Streamlit UI

---

## 🏗️ Project Structure

```plaintext
Movie_Recommender_App/
│
├── App.py                        # Main Streamlit app
├── config.yaml                   # Configuration for LanceDB URI
├── requirements.txt              # Project dependencies
├── moviees.jpg                   # Banner image for the app
│
├── Artifacts/
│   └── embeddings/
│       └── embeddings.csv        # Precomputed movie embeddings + metadata
│
└── src/
    ├── components/
    │   └── create_lance_db.py    # Function to create and populate LanceDB
    │
    ├── pipeline/
    │   └── pipeline.py           # Retriever logic using LanceDB and Sentence Transformers
    │
    └── utils/
        └── load_yaml_file.py     # Helper to load config file



---

## ⚙️ Setup Instructions

1. **Clone the repo**

```bash
git clone https://github.com/cleavestone/Movie_Recommender_App.git
cd Movie_Recommender_App
