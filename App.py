import streamlit as st
import pandas as pd
import lancedb
from sentence_transformers import SentenceTransformer
from src.utils.load_yaml_file import load_yaml

uri=load_yaml()['uri']

# Load the model and database
@st.cache_resource
def load_model():
    return SentenceTransformer('paraphrase-MiniLM-L6-v2')


@st.cache_resource
def load_database():
    return lancedb.connect(uri).open_table("movies")


def retriever(query, table, model, k=5):
    """
    Retrieve movie recommendations based on semantic search.

    Args:
        query (str): User's search query.
        table (lancedb.table): LanceDB table with movies.
        model (SentenceTransformer): Embedding model.
        k (int, optional): Number of recommendations. Defaults to 5.

    Returns:
        list: List of recommended movies.
    """
    # Encode the query
    query_embedding = model.encode([query])[0]

    # Perform similarity search
    docs = table.search(query_embedding).limit(k).to_list()

    return docs

def main():
    # App Title and Description
    st.title("🎥 Movie Magic")
    
    # Sidebar for Branding and Navigation
    st.sidebar.title("🎬 Movie Magic")
    st.sidebar.image("moviees.jpg", caption="Your Movie Partner", use_container_width=True)
    st.sidebar.markdown("---")
    st.sidebar.markdown("**Powered by:**")
    st.sidebar.markdown("- Streamlit")
    st.sidebar.markdown("- LanceDB")
    st.sidebar.markdown("- SentenceTransformers")

    # Load model and database
    model = load_model()
    table = load_database()

    # Initialize session state variables
    if 'query' not in st.session_state:
        st.session_state.query = None

    # Option 2: Genre Selection
    st.header("Browse by Genre")
    col1, col2, col3, col4 = st.columns(4) 

    genres = {
        "🎭 Comedy": "I want to watch a comedy movie",
        "💥 Action": "I want an action-packed movie",
        "💘 Romance": "Show me romantic movies",
        "👻 Horror": "Looking for a scary horror movie",
        "🎨 Animated": "Recommend animated movies",
        "🎬 Sci-Fi": "I want a science fiction movie",
        "🕵️‍♂️ Mystery": "Show me a mystery movie",
        "🌎 Adventure": "I want an adventure movie" 
    }

    for idx, (label, genre_query) in enumerate(genres.items()):
        with [col1, col2, col3, col4][idx % 4]:
            if st.button(label):
                st.session_state.query = genre_query
                # Clear the text area input when a genre button is clicked
                if 'user_input' in st.session_state:
                    del st.session_state.user_input
                st.rerun()

    # User Input Section
    st.header("Tell Us What You're Looking For")

    if 'user_input' not in st.session_state:
        st.session_state.user_input = ""

    user_input = st.text_area(
        "Describe your ideal movie:", 
        placeholder="e.g., I want an animated action movie like Spider-Man: Into the Spider-Verse", 
        key="user_input"
    )

    # Get the final query (either typed or selected genre)
    if user_input:
        final_query = user_input
    elif st.session_state.query:
        final_query = st.session_state.query
    else:
        final_query = None

    # Number of recommendations slider
    st.header("How Many Recommendations?")
    k = st.slider("Select the number of recommendations:", min_value=1, max_value=10, value=5, step=1)

    # Search button
    if st.button("🎥 Find My Movie Match!"):
        if final_query:
            try:
                # Get recommendations
                recommendations = retriever(final_query, table, model, k)

                # Display recommendations with better formatting
                st.header("Here are your recommendations:")
                for idx, movie in enumerate(recommendations, 1):
                    with st.expander(f"{idx}. {movie['original_title']}"):
                        st.write(f"**Popularity:** {movie.get('popularity', 'N/A')}")
                        st.write(f"**Overview:** {movie.get('overview', 'No overview available.')}")
            except Exception as e:
                st.error(f"An error occurred: {e}")
        else:
            st.warning("Please enter a movie description or select a genre.")

if __name__ == "__main__":
    main()
