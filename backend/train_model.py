import pandas as pd
import pickle
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from features import extract_features

DATA_PATH = "../data/clean_urls.csv"
MODEL_PATH = "../models/url_risk_model.pkl"

print("📥 Loading clean dataset...")
df = pd.read_csv(DATA_PATH)

# Feature extraction
print("🔍 Extracting features...")
X = df["url"].apply(lambda x: extract_features(x)).tolist()
y = df["label"]

# Train-test split (for sanity check)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
print("🧠 Training model...")
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print(f"✅ Model trained successfully")
print(f"📊 Accuracy: {round(accuracy * 100, 2)}%")

# Save model
with open(MODEL_PATH, "wb") as f:
    pickle.dump(model, f)

print("💾 Model saved as url_risk_model.pkl")
