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

├── App.py                     # Main application script
├── config.yaml                # Configuration file with database URI and other settings
├── requirements.txt           # List of dependencies
├── moviees.jpg                # Image used in the application
├── Artifacts/
│   └── embeddings/
│       └── embeddings.csv     # CSV file containing movie embeddings
├── src/
│   ├── components/
│   │   └── create_lance_db.py # Script to create and manage LanceDB tables
│   ├── pipeline/
│   │   └── pipeline.py        # Main pipeline for data processing and model integration
│   └── utils/
│       └── load_yaml_file.py  # Utility to load YAML configuration files
├── notebooks/                 # Jupyter notebooks for experimentation and analysis
└── .dvc/                      # DVC files for data version control



---

## ⚙️ Setup Instructions

1. **Clone the repo**

```bash
git clone https://github.com/cleavestone/Movie_Recommender_App.git
cd Movie_Recommender_App
