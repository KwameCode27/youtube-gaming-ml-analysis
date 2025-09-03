import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt
import seaborn as sns

# ----------------------------
# 1. Load Model
# ----------------------------
lin_reg = joblib.load("models/linear_model.pkl")
rf_reg = joblib.load("models/random_forest_model.pkl")

# ----------------------------
# 2. Streamlit UI
# ----------------------------
st.set_page_config(page_title="YouTube Gaming Predictor", page_icon="🎮", layout="wide")

st.title("🎮 YouTube Gaming Channel Dashboard & Predictor")

# Sidebar menu
menu = st.sidebar.radio("📌 Navigation", ["Predict Hours Watched", "Cluster Dashboard", "Dataset Preview"])

# ----------------------------
# 3. Prediction Section
# ----------------------------
if menu == "Predict Hours Watched":
    st.header("📊 Predict Hours Watched")

    # User inputs
    peak_viewers = st.number_input("Peak Viewers", min_value=0, step=1000, format="%d")
    avg_viewers = st.number_input("Average Viewers", min_value=0, step=1000, format="%d")
    airtime_hours = st.number_input("Airtime Hours", min_value=0, step=1, format="%d")

    model_choice = st.selectbox("Choose Model", ["Linear Regression", "Random Forest"])

    if st.button("Predict"):
        viewers_per_hour = avg_viewers * airtime_hours
        efficiency = (avg_viewers * airtime_hours) / (airtime_hours + 1e-6)

        X_new = pd.DataFrame([[peak_viewers, avg_viewers, airtime_hours, viewers_per_hour, efficiency]],
                             columns=["Peak Viewers", "Average Viewers", "Airtime Hours", "Viewers_per_Hour", "Efficiency"])

        if model_choice == "Linear Regression":
            prediction = lin_reg.predict(X_new)[0]
        else:
            prediction = rf_reg.predict(X_new)[0]

        st.success(f"📈 Predicted Hours Watched: **{prediction:,.0f}**")

# ----------------------------
# 4. Clustering Dashboard
# ----------------------------
elif menu == "Cluster Dashboard":
    st.header("📊 Channel Clustering")

    # Load dataset
    df = pd.read_csv("data/train.csv")

    # Feature engineering
    df["Viewers_per_Hour"] = df["Average Viewers"] * df["Airtime Hours"]
    df["Efficiency"] = df["Hours Watched"] / df["Airtime Hours"]
    df["Cluster"] = pd.qcut(df["Efficiency"], q=3, labels=["Low", "Medium", "High"])

    st.write("### Cluster Summary")
    cluster_summary = df.groupby("Cluster")[["Average Viewers", "Airtime Hours", "Efficiency"]].mean()
    st.dataframe(cluster_summary)

    # Scatter Plot
    st.write("### Cluster Visualization")
    fig, ax = plt.subplots(figsize=(8,6))
    sns.scatterplot(data=df, x="Average Viewers", y="Efficiency", hue="Cluster", palette="viridis", s=80)
    plt.xlabel("Average Viewers")
    plt.ylabel("Efficiency")
    plt.title("YouTube Gaming Channels Clustering")
    st.pyplot(fig)

# ----------------------------
# 5. Dataset Preview
# ----------------------------
else:
    st.header("📂 Dataset Preview")
    df = pd.read_csv("data/train.csv")
    st.write("Here are the first 10 rows of the dataset:")
    st.dataframe(df.head(10))


