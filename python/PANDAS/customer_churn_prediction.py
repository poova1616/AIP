import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

# Sample dataset (Continuous + Categorical)
data = {
    "Age": [25, 40, 60, 30, 50],
    "Gender": ["Male", "Female", "Male", "Female", "Male"],
    "MonthlyBill": [5000, 8000, 6000, 7000, 9000],
    "Churn": ["No", "Yes", "No", "Yes", "Yes"]
}

df = pd.DataFrame(data)

# Encode categorical variable (Gender, Churn)
le_gender = LabelEncoder()
df["Gender"] = le_gender.fit_transform(df["Gender"])  # Male=1, Female=0

le_churn = LabelEncoder()
df["Churn"] = le_churn.fit_transform(df["Churn"])    # No=0, Yes=1

# Features & Target
X = df[["Age", "Gender", "MonthlyBill"]]
y = df["Churn"]

# Scale continuous data
scaler = StandardScaler()
X[["Age", "MonthlyBill"]] = scaler.fit_transform(X[["Age", "MonthlyBill"]])

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train Random Forest Classifier
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)

# Evaluation
print("Classification Report:\n", classification_report(y_test, y_pred))
