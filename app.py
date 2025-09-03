import joblib
import pandas as pd

# Load saved model
model = joblib.load("linear_model.pkl")

# Example input (replace with user input later)
peak_viewers = 200000
avg_viewers = 50000
airtime_hours = 250

# Feature engineering (must match training script)
viewers_per_hour = avg_viewers * airtime_hours
efficiency = (avg_viewers * airtime_hours) / (airtime_hours + 1e-6)

# Put into DataFrame (same order as training)
X_new = pd.DataFrame([[peak_viewers, avg_viewers, airtime_hours, viewers_per_hour, efficiency]],
                     columns=["Peak Viewers", "Average Viewers", "Airtime Hours", "Viewers_per_Hour", "Efficiency"])

# Predict
prediction = model.predict(X_new)[0]
print(f"Predicted Hours Watched: {prediction:,.0f}")
