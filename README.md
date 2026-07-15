<div align="center">
  
  # 🛡️ AI-Based Military Intelligence Dashboard 🌍

  <p align="center">
    <strong>A comprehensive Streamlit application for analyzing the Global Terrorism Database (GTD) and leveraging machine learning models to forecast and predict military intelligence metrics.</strong>
  </p>
  
  <p align="center">
    <img src="https://img.shields.io/badge/Python-3.8+-blue.svg" alt="Python Version" />
    <img src="https://img.shields.io/badge/Streamlit-FF4B4B.svg?style=flat&logo=Streamlit&logoColor=white" alt="Streamlit" />
    <img src="https://img.shields.io/badge/Machine%20Learning-scikit--learn-orange.svg" alt="scikit-learn" />
    <img src="https://img.shields.io/badge/Data%20Viz-Plotly-purple.svg" alt="Plotly" />
  </p>

</div>

---

## 🌟 Overview

The **Military Intelligence Dashboard** is an advanced analytics platform designed to uncover patterns in global terrorism data. By combining interactive visualizations with predictive machine learning models, it provides actionable insights into threat levels, attack types, and geographic incident distributions.

---

## ✨ Key Features

- 🗺️ **Global Threat Map**: Interactive geospatial analysis of historical and predicted incidents.
- 📊 **Country-Level Analysis**: Deep dive into regional metrics and localized threat assessments.
- 🔮 **Attack & Threat Prediction**: Machine learning models forecasting potential attack types and overall threat levels.
- 📈 **Trend Forecasting**: Time-series forecasting for future incident volumes.
- 🤖 **AI Intelligence Report**: Automated generation of intelligence summaries based on data insights.
- 🔍 **Data Explorer**: Comprehensive interface to query and filter the underlying GTD dataset.

---

## 📁 Project Structure

```text
Military_Intelligence_Dashboard/
├── app.py                         # 🚀 Main Streamlit dashboard entry point
├── train_attack_model.py          # 🧠 Script to train the ML models
├── data/                          
│   └── globalterrorism.csv        # 🗄️ Primary GTD dataset
├── models/                        # 💾 Directory for trained ML models
│   ├── attack_prediction_model.pkl
│   ├── feature_encoders.pkl
│   └── target_encoder.pkl
├── pages/                         # 📑 Interactive dashboard modules
│   ├── 1_Home.py
│   ├── 2_Global_Threat_Map.py
│   ├── 3_Country_Analysis.py
│   ├── 4_Attack_Prediction.py
│   ├── 5_Threat_Level_Prediction.py
│   ├── 6_Forecasting.py
│   ├── 7_AI_Intelligence_Report.py
│   ├── 8_Data_Explorer.py
│   └── 9_Settings.py
└── utils/
    └── data_loader.py             # 🛠️ Utility functions (e.g., cached data loader)
```

---

## 🚀 Getting Started

### 1️⃣ Prerequisites
Ensure you have Python installed on your system. 

### 2️⃣ Installation
Install the required dependencies using pip:
```bash
pip install streamlit pandas plotly scikit-learn joblib
```

### 3️⃣ Data Preparation
Make sure the `data/globalterrorism.csv` file exists in the correct path relative to the project root. You can download the GTD dataset and place it in the `data/` directory.

---

## 🧠 Model Training

Before using the predictive features of the dashboard, you need to generate the initial prediction models.

Train the Random Forest models by running:
```bash
python train_attack_model.py
```
> **Note:** This script will process the GTD dataset, train the model, and export the required `.pkl` files into the `models/` directory.

---

## 💻 Running the Dashboard

Launch the interactive dashboard locally with a single command:

```bash
streamlit run app.py
```

> The application will open a local web server (typically at `http://localhost:8501`), allowing you to explore all modules from the Global Threat Map to AI Intelligence reports.

---


