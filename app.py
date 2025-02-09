import streamlit as st
import joblib
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

# Load the trained model and TF-IDF vectorizer
model = joblib.load("model.pkl")
tfidf_vectorizer = joblib.load("vectorizer.pkl")

# Streamlit UI
st.title("Fake News Detection System")
st.write("Enter a news article below to check if it's fake or real.")

# Input field for news text
news_text = st.text_area("Enter the news article text:")

# Prediction
if st.button("Detect"):
    if news_text.strip():
        # Transform the input text using the vectorizer

        input_data_tfidf = tfidf_vectorizer.transform([news_text])
        prediction = model.predict(input_data_tfidf)
        
        if prediction[0] == 0:
            st.error("This news article is likely FAKE.")
        else:
            st.success("This news article appears to be REAL.")
    else:
        st.warning("Please enter some text to analyze.")
