# 🎮 YouTube Gaming Channel Analysis & Machine Learning  

This project analyzes the performance of **top YouTube Gaming channels** using real-world streaming data. It combines **data analysis, machine learning, and interactive visualizations** to uncover insights about streaming efficiency and predict audience engagement.  

---

## 📊 Features  

- **Data Cleaning & Feature Engineering**  
  - Added new metrics such as:  
    - *Viewers per Hour* = Average Viewers × Airtime Hours  
    - *Efficiency* = Hours Watched ÷ Airtime Hours  

- **Machine Learning Models**  
  - Built and compared **Linear Regression** and **Random Forest Regressor**  
  - Predicts a channel’s **Hours Watched**  
  - Model evaluation with **R², MAE, RMSE**  

- **Clustering (Unsupervised Learning)**  
  - Used **KMeans** to group channels into 3 performance clusters:  
    - High-efficiency creators  
    - Long-hour grinders  
    - Balanced performers  

- **Interactive Web App (Streamlit)**  
  - Upload channel stats or use dataset  
  - Predict expected **Hours Watched**  
  - Visualize channel clusters and compare strategies  

---

## 🛠️ Tech Stack  

- **Python** (pandas, numpy, matplotlib, scikit-learn, joblib)  
- **Machine Learning** (Regression + Clustering)  
- **Streamlit** for interactive web app  

---

## 🚀 Setup & Installation  

### 1️⃣ Clone the repo  
```bash
git clone https://github.com/your-username/youtube-gaming-ml-analysis.git
cd youtube-gaming-ml-analysis
```

2️⃣ Install dependencies

Make sure you have Python 3.10+ installed. Then run:
```bash
pip install -r requirements.txt
```

3️⃣ Run the analysis script
```bash
python app.py
```

4️⃣ Run the Streamlit app
```bash
streamlit run app.py
```

📌 Example Use Cases

Streamers → Benchmark performance against competitors

Brands/Advertisers → Identify efficient channels for sponsorships

Researchers → Study gaming content engagement trends

📂 Project Structure
```bash
youtube-gaming-ml-analysis/
│── app.py                # Main script & Streamlit app
│── model.pkl             # Saved Random Forest model
│── scaler.pkl            # Saved feature scaler
│── youtube_channels.csv  # Dataset (rename for simplicity)
│── requirements.txt      # Dependencies
│── README.md             # Project documentation
```