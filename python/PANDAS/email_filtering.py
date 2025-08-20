# Install scikit-learn if needed
# pip install scikit-learn pandas

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

# 1. Sample dataset (you can replace with your own)
data = {
    "message": [
        "Win a free iPhone now!!!",
        "Hi, how are you doing today?",
        "Limited time offer, buy 1 get 1 free",
        "Are we still meeting tomorrow?",
        "Congratulations, you won a lottery prize!"
    ],
    "label": ["spam", "ham", "spam", "ham", "spam"]  # spam = unwanted, ham = normal
}

df = pd.DataFrame(data)

# 2. Split data into training & testing
X_train, X_test, y_train, y_test = train_test_split(
    df["message"], df["label"], test_size=0.3, random_state=42
)

# 3. Convert text to numerical features
vectorizer = CountVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# 4. Train a Naive Bayes classifier
model = MultinomialNB()
model.fit(X_train_vec, y_train)

# 5. Predict on test data
y_pred = model.predict(X_test_vec)

# 6. Evaluate performance
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))
