import streamlit as st
import pickle

# Load the trained model
with open("movie_similarity.pkl", "rb") as f:
    movie_similarity_df = pickle.load(f)

with open("movie_list.pkl", "rb") as f:
    movie_list = pickle.load(f)

# Streamlit App UI
st.title("🎬 Movie Recommendation System")

# User selects a movie
selected_movie = st.selectbox("Choose a movie:", movie_list)

# Recommendation button
if st.button("Get Recommendations"):
    if selected_movie in movie_similarity_df.index:
        similar_movies = movie_similarity_df[selected_movie].sort_values(ascending=False)[1:6].index.tolist()
        st.subheader("Recommended Movies:")
        for movie in similar_movies:
            st.write(f"🎥 {movie}")
    else:
        st.error("Movie not found! Please select a valid movie.")



