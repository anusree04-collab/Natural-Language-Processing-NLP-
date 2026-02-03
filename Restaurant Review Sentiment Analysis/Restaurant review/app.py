import streamlit as st
import pickle

# Load model and vectorizer
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

st.title("Restaurant Review Sentiment Analyzer")

review = st.text_area("Enter your review")

if st.button("Analyze Sentiment"):
    review_vector = vectorizer.transform([review])
    prediction = model.predict(review_vector)

    if prediction[0] == 1:
        st.success("Positive Review")
    else:
        st.error("Negative Review")
        



