import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load dataset
data = pd.read_csv("activities.csv")

# Encode categorical data
le = LabelEncoder()
encoders = {}

for column in data.columns:
    le = LabelEncoder()
    data[column] = le.fit_transform(data[column])
    encoders[column] = le

# Split data
X = data.drop("recommendation", axis=1)
y = data["recommendation"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier(n_estimators=200, max_depth=5)
model.fit(X_train, y_train)

# Test accuracy
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))

# 🔮 Try prediction
import pandas as pd

def predict_activity(mood, energy, time, day, previous):
    input_dict = {
        "mood": encoders['mood'].transform([mood])[0],
        "energy": encoders['energy'].transform([energy])[0],
        "time": encoders['time'].transform([time])[0],
        "day": encoders['day'].transform([day])[0],
        "previous_activity": encoders['previous_activity'].transform([previous])[0]
    }

    input_df = pd.DataFrame([input_dict])

    prediction = model.predict(input_df)
    return encoders['recommendation'].inverse_transform(prediction)[0]

# Example test
result = predict_activity("happy", "high", "morning", "weekday", "sleep")
print("Recommended Activity:", result)

import pickle

with open("model.pkl", "wb") as f:
    pickle.dump((model, encoders), f)