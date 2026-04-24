import streamlit as st
import pandas as pd
import pickle

# Load model and encoders (we'll save them from model.py)
with open("model.pkl", "rb") as f:
    model, encoders = pickle.load(f)

st.title("🧠 Smart Daily Activity Recommender")

st.write("Enter your current state to get a smart activity suggestion")

# Inputs
mood = st.selectbox("Mood", ["happy", "stressed", "tired"])
energy = st.selectbox("Energy Level", ["low", "medium", "high"])
time = st.selectbox("Time of Day", ["morning", "afternoon", "evening", "night"])
day = st.selectbox("Day Type", ["weekday", "weekend"])
previous = st.selectbox("Previous Activity", ["study", "exercise", "relax", "socialize", "sleep"])

# Predict function
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

# Button
if st.button("🔍 Recommend Activity"):
    result = predict_activity(mood, energy, time, day, previous)
    st.success(f"✅ Recommended Activity: {result}")