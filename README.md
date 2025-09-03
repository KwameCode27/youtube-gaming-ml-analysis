# 🎮 YouTube Gaming Channel Predictor

This project analyzes **Top YouTube Gaming Channels** and uses **Machine Learning** to:
- Predict **Hours Watched** based on channel stats.
- Cluster channels into groups (e.g., efficient, high-view, long-hour).
- Provide an **interactive web app** (built with Streamlit) to make predictions.

---


---

## ⚙️ Installation

1. Clone this repo or download the files.  
2. (Optional but recommended) Create a virtual environment:

```bash
python -m venv venv
.\venv\Scripts\activate    # Windows
source venv/bin/activate   # Linux/Mac


pip install -r requirements.txt


📊 Training the Model

Run the ML script to:

Load dataset

Engineer features

Train Linear Regression & Random Forest

Save best models

Perform clustering & visualization


python train_model.py


🌐 Running the Web App

To launch the prediction app:
streamlit run app.py

python -m streamlit run app.py

🖼 Features

ML Models: Linear Regression & Random Forest

Predictions: Estimate Hours Watched from user input stats

Clustering: Group channels by efficiency & viewership

Web App: Simple, interactive Streamlit interface

📌 Requirements

See requirements.txt. Main libraries:

pandas

numpy

matplotlib

scikit-learn

joblib

streamlit

🚀 Future Improvements

Add model selection dropdown in the app

Deploy online (Streamlit Cloud / Heroku / Render)

Extend to other platforms (Twitch, Kick, etc.)



