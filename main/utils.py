import os
import joblib

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

def get_calculated_rating(review_content):

    model_filename = os.path.join(BASE_DIR, "main/models/trained_model.joblib")
    vectorizer_filename = os.path.join(BASE_DIR, "main/models/vectorizer.joblib")

    model = joblib.load(model_filename)
    vectorizer = joblib.load(vectorizer_filename)

    X_input_vectorized = vectorizer.transform([review_content])

    predictions = model.predict(X_input_vectorized)

    return predictions[0]