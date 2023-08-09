import joblib

# Load the model and vectorizer
model = joblib.load('trained_model.joblib')
vectorizer = joblib.load('vectorizer.joblib')

# Prepare the input data
input_reviews = ["This product is amazing!", "This sucks. It is terrible."]

# Vectorize the input reviews
X_input_vectorized = vectorizer.transform(input_reviews)

# Make predictions
predictions = model.predict(X_input_vectorized)

# Print the predictions
for review, prediction in zip(input_reviews, predictions):
    print(f"Review: {review}\nPrediction: {prediction}\n")
