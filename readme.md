# Fake News Detection

## Overview
This project is a **Fake News Detection System** that uses machine learning to classify news articles as real or fake. The system is deployed using **Streamlit**, allowing users to input text and get a prediction.

## Features
- Input a news article and check if it's real or fake.
- Uses a trained machine learning model with TF-IDF vectorization.
- Simple and interactive UI built with **Streamlit**.
- Supports real-time predictions.

## Files and Directories
- `app.py` - The main script for the Streamlit web application.
- `model.pkl` - The trained machine learning model.
- `vectorizer.pkl` - The saved TF-IDF vectorizer.
- `README.md` - Project documentation.
- `fake_or_real_news.csv` - Dataset

## How It Works
1. The user enters a news article into the text area.
2. The input is transformed using the **TF-IDF vectorizer**.
3. The **ML model** predicts whether the news is real or fake.
4. The result is displayed on the web app.

