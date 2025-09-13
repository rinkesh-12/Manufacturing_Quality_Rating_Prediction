# Manufacturing Quality Rating Prediction

A **Streamlit web application** that predicts the **quality rating of manufactured products** based on process and material parameters.  
This project uses a **Machine Learning model** trained on manufacturing process data to assist engineers in evaluating product quality.

---

## Features

- **Interactive Web App** built with Streamlit  
- **User Input Fields:**
  - Temperature (°C)
  - Pressure (kPa)
  - Temperature × Pressure
  - Material Fusion Metric
  - Material Transformation Metric  
- **Prediction:**  
  - Outputs the **predicted quality rating** as a numeric value.  

---

## Tech Stack

- **Frontend/UI:** [Streamlit](https://streamlit.io/)  
- **Data Handling:** Pandas, NumPy  
- **Modeling:** Scikit-learn (pre-trained model stored as `.pkl`)  
- **Serialization:** Pickle  

---

## Project Structure

├── app.py # Main Streamlit app
├── Manufacturing Quality Rating Prediction.ipynb # Jupyter Notebook (EDA & model training)
├── manufacturing_quality_rating_model.pkl # Trained ML model
├── manufacturing_xgr.csv # Dataset
├── requirements.txt # Dependencies
└── README.md # Documentation

