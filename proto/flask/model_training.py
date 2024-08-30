import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score
import joblib

# Load your dataset
df = pd.read_csv('cyberattacks.csv')

# Check column names
print("Columns in the dataset:", df.columns)

# Update column names if necessary
df.rename(columns={'text': 'description', 'label': 'attack_type'}, inplace=True)

# Split the dataset into features and labels
X = df['description']
y = df['attack_type']

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a text processing and logistic regression pipeline
pipeline = Pipeline([
    ('tfidf', TfidfVectorizer()),
    ('clf', LogisticRegression(max_iter=1000)),
])

# Train the model
pipeline.fit(X_train, y_train)

# Test the model
y_pred = pipeline.predict(X_test)
print(f"Accuracy: {accuracy_score(y_test, y_pred)}")

# Save the model to a file
joblib.dump(pipeline, 'cyberattack_classifier.pkl')
