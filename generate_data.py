import pandas as pd
import random

# Possible values
moods = ["happy", "stressed", "tired"]
energy_levels = ["low", "medium", "high"]
times = ["morning", "afternoon", "evening", "night"]
days = ["weekday", "weekend"]
activities = ["study", "exercise", "relax", "socialize", "sleep"]

data = []

# Generate 150 rows
for _ in range(150):
    mood = random.choice(moods)
    energy = random.choice(energy_levels)
    time = random.choice(times)
    day = random.choice(days)
    prev = random.choice(activities)

    # Strong logical rules (important for accuracy)
    if time == "morning":
        if energy == "high":
            rec = "exercise"
        elif energy == "medium":
            rec = "study"
        else:
            rec = "relax"

    elif time == "afternoon":
        if mood == "stressed":
            rec = "relax"
        else:
            rec = "study"

    elif time == "evening":
        if day == "weekend":
            rec = "socialize"
        else:
            rec = "relax"

    elif time == "night":
        rec = "sleep"

    data.append([mood, energy, time, day, prev, rec])

# Create DataFrame
df = pd.DataFrame(data, columns=[
    "mood", "energy", "time", "day", "previous_activity", "recommendation"
])

# Save to CSV
df.to_csv("activities.csv", index=False)

print("✅ Dataset generated successfully with 150 rows!")