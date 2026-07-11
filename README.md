# AI-Based Military Intelligence Dashboard 🛡️

A comprehensive Streamlit application for analyzing the Global Terrorism Database (GTD) and leveraging machine learning models to forecast and predict military intelligence metrics such as threat levels, attack types, and global incident distributions.

## Project Structure

```text
Military_Intelligence_Dashboard/
├── app.py                         # Main Streamlit dashboard entry point
├── train_attack_model.py          # Script to train the ML models
├── data/                          
│   └── globalterrorism.csv        # Primary GTD dataset
├── models/                        # Directory for trained ML models
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
3. **Data Requirements:**
   Ensure the `data/globalterrorism.csv` file exists in the correct path relative to the project root.

## Model Training

Before using the predictive features of the dashboard, you can retrain or generate the initial attack prediction model.

To train the Random Forest model:
```bash
python train_attack_model.py
```
This script will process the GTD dataset, train the model, and export the required `.pkl` files into the `models/` directory.

## Running the Dashboard

To launch the interactive dashboard locally:

```bash
streamlit run app.py
```

This will open a local web server (typically at `http://localhost:8501`) where you can explore the various modules including the Global Threat Map, Attack Predictions, AI Intelligence reports, and Data Explorers.
