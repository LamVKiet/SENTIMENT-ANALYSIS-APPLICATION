import streamlit as st
import pickle
import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
import re
import time

# Load models and other necessary files
MODEL_PATH = 'models/svm_model.pkl'
VECTORIZER_PATH = 'models/tfidf_vectorizer.pkl'
LABEL_ENCODER_PATH = 'models/label_encoder.pkl'

with open(MODEL_PATH, 'rb') as file:
    svm_model = pickle.load(file)
with open(VECTORIZER_PATH, 'rb') as file:
    vectorizer = pickle.load(file)
with open(LABEL_ENCODER_PATH, 'rb') as file:
    label_encoder = pickle.load(file)

# Initialize Streamlit app
st.title('Sentiment Analysis')

# Text input for review
review = st.text_area("Enter your review here...")

# Analyze button
if st.button('Analyze'):
    if review:
        # Process the input review
        review_tfidf = vectorizer.transform([review])
        predicted_label = svm_model.predict(review_tfidf)
        predicted_label_name = label_encoder.inverse_transform(predicted_label)[0]

        # Display the result
        if predicted_label_name == 'Positive':
            st.success('Sentiment: Positive')
            st.image('static/pos.png', width=200)
        else:
            st.error('Sentiment: Negative')
            st.image('static/neg.png', width=200)
