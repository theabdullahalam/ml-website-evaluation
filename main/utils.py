import joblib

def get_calculated_rating(review_content):
    model = joblib.load('/home/abdullah/college/sem2/capstone/myproj/websitereview/main/models/trained_model.joblib')
    vectorizer = joblib.load('/home/abdullah/college/sem2/capstone/myproj/websitereview/main/models/vectorizer.joblib')

    X_input_vectorized = vectorizer.transform([review_content])

    predictions = model.predict(X_input_vectorized)

    return predictions[0]