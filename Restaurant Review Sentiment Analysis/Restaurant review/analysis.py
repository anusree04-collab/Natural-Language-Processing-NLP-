import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import pickle
import os

print("current folder:",os.getcwd())

print("Loading dataset...")

data = pd.read_csv(r"C:\Users\K anusree\OneDrive\Desktop\Restaurant review\Restaurant_Reviews.tsv", sep="\t", encoding="utf-8", on_bad_lines='skip')

print(data.head())
print("Columns:", data.columns)

X = data["Review"]
y = data["Liked"]

vectorizer = TfidfVectorizer(stop_words="english")
X_vec = vectorizer.fit_transform(X)

model = LogisticRegression(max_iter=1000)
model.fit(X_vec, y)

# Save pickle files
pickle.dump(model, open("model.pkl", "wb"))
pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))

print("model.pkl and vectorizer.pkl created successfully")
