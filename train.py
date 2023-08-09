import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib

# Load the dataset
print('loading')
train_data = pd.read_csv('dataset/train.csv', header=None, names=['rating', 'title', 'review'])
test_data = pd.read_csv('dataset/test.csv', header=None, names=['rating', 'title', 'review'])

# Prepare the features and labels
print('prepping')
X_train = train_data['review']
y_train = train_data['rating']
X_test = test_data['review']
y_test = test_data['rating']

# Create and fit the vectorizer
print('vectorising')
vectorizer = TfidfVectorizer()
X_train_vectorized = vectorizer.fit_transform(X_train)

# Train the model with increased max_iter
print('train')
max_iter = 1000  # Increase the max_iter value
model = LogisticRegression(max_iter=max_iter)
model.fit(X_train_vectorized, y_train)

# Save the model and vectorizer
print('save')
joblib.dump(model, 'trained_model.joblib')
joblib.dump(vectorizer, 'vectorizer.joblib')
