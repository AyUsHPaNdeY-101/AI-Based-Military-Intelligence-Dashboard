# AI-Based Military Intelligence Dashboard 🛡️

A comprehensive Streamlit application for analyzing the Global Terrorism Database (GTD) and leveraging machine learning models to forecast and predict military intelligence metrics such as threat levels, attack types, and global incident distributions.

## Project Structure

```text
Military_Intelligence_Dashboard/
├── app.py                         # Main Streamlit dashboard entry point
├── train_attack_model.py          # Script to train the ML models
├── data/                          
│   └── globalterrorism.csv        # Primary GTD dataset (Must be downloaded manually)
├── models/                        # Directory for trained ML models (Generated locally)
│   ├── attack_prediction_model.pkl
│   ├── feature_encoders.pkl
│   └── target_encoder.pkl
├── pages/                         # Interactive dashboard modules
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
    └── data_loader.py             # Utility functions (e.g., cached data loader)
```

## Setup Instructions

1. **Ensure you have Python installed.**
2. **Install the required dependencies:**
   Make sure you have `streamlit`, `pandas`, `plotly`, `scikit-learn`, and `joblib` installed. You can install them using pip:
   ```bash
   pip install streamlit pandas plotly scikit-learn joblib
   ```
3. **Data Requirements (Important):**
   Due to GitHub's file size limits, the `globalterrorism.csv` file (155+ MB) is **not** included in this repository. You must download the Global Terrorism Database dataset manually and place the extracted `globalterrorism.csv` file directly into the `data/` directory before proceeding.

## Model Training

Due to GitHub's file size limits, the pre-trained `attack_prediction_model.pkl` (1.14 GB) is **not** included in this repository. 

Before using the predictive features of the dashboard, you **must** generate the initial attack prediction model locally. Once you have placed the dataset in the `data/` folder, run the following command:

```bash
python train_attack_model.py
```
This script will process the GTD dataset, train the Random Forest model, and export the required `.pkl` files into the `models/` directory.

## Running the Dashboard

**Important:** Because the Global Terrorism Database is a large file, it exceeds Streamlit's default message size limit of 200 MB. To avoid a `MessageSizeError` crashing the app, you must increase the server's maximum message size.

To launch the interactive dashboard locally, use the following command:

```bash
streamlit run app.py --server.maxMessageSize 400
```

> **Note:** Alternatively, you can permanently increase the limit for this project by creating a `.streamlit/config.toml` file in your root directory and adding the following lines:
> ```toml
> [server]
> maxMessageSize = 400
> ```

This will open a local web server (typically at `http://localhost:8501`) where you can explore the various modules including the Global Threat Map, Attack Predictions, AI Intelligence reports, and Data Explorers.
