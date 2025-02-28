# -Movie-Recommendation-System-Beginner-Level-
This project is a Movie Recommendation System that suggests similar movies based on user input. It leverages Natural Language Processing (NLP) and Machine Learning to analyze movie features and determine their similarity.

How It Works:
Feature Extraction: The system converts movie descriptions into numerical vectors using TF-IDF (Term Frequency-Inverse Document Frequency).
Similarity Calculation: It applies Cosine Similarity to measure the closeness between movie vectors.
Recommendation Generation: Based on the input movie, it finds the top 5 most similar movies.

Tech Stack Used:
Python (Flask, Streamlit, Pandas, Scikit-learn)
Machine Learning (TF-IDF, Cosine Similarity)
Web Frameworks (Flask for API, Streamlit for UI)
Users can enter a movie name, and the system will return personalized recommendations instantly.


