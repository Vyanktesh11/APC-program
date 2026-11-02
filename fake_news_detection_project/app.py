import csv
import os
from pathlib import Path

from flask import Flask, render_template, request
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

BASE_DIR = Path(__file__).resolve().parent
DATASET_PATH = BASE_DIR / "news_dataset.csv"
app = Flask(__name__)

def load_news():
    records = []
    with open(DATASET_PATH, "r", encoding="utf-8", newline="") as file:
        for row in csv.DictReader(file):
            if row.get("news") and row.get("label"):
                records.append({
                    "id": row.get("id", ""),
                    "news": row["news"].strip(),
                    "label": row["label"].strip().upper(),
                    "category": row.get("category", "General").strip(),
                    "source_note": row.get("source_note", "").strip()
                })
    return records

NEWS_RECORDS = load_news()
VECTORIZER = TfidfVectorizer(stop_words="english", ngram_range=(1, 2))
DATASET_MATRIX = VECTORIZER.fit_transform([item["news"] for item in NEWS_RECORDS])

def classify_news(user_text):
    query_vector = VECTORIZER.transform([user_text])
    scores = cosine_similarity(query_vector, DATASET_MATRIX).flatten()
    best_index = int(scores.argmax())
    best_score = float(scores[best_index])
    best_match = NEWS_RECORDS[best_index]

    # A low similarity score is not enough evidence to label a claim as real or fake.
    threshold = 0.18
    if not user_text.strip() or best_score < threshold:
        return {
            "status": "unknown",
            "label": "UNKNOWN",
            "similarity": round(best_score * 100, 1),
            "match": best_match,
            "message": "No sufficiently similar record was found in the 20-item sample dataset."
        }

    return {
        "status": "matched",
        "label": best_match["label"],
        "similarity": round(best_score * 100, 1),
        "match": best_match,
        "message": "This result is based only on similarity to a stored sample record, not live fact-checking."
    }

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    searched_text = ""
    if request.method == "POST":
        searched_text = request.form.get("news", "").strip()
        if searched_text:
            result = classify_news(searched_text)
    return render_template(
        "index.html",
        result=result,
        searched_text=searched_text,
        total_records=len(NEWS_RECORDS)
    )

@app.route("/dataset")
def dataset():
    return render_template("dataset.html", records=NEWS_RECORDS)

if __name__ == "__main__":
    app.run(debug=True)
