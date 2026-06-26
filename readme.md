# 🤖 IIoT Machine Failure Prediction System

An Industrial Internet of Things (IIoT) machine learning project that predicts machine failures based on sensor data. The system analyzes temperature, pressure, vibration, and humidity to classify machine health and recommend maintenance actions.

---

## 📌 Project Overview

This project demonstrates predictive maintenance using machine learning. A Random Forest Classifier is trained on simulated IIoT sensor data to detect potential machine failures and classify machine conditions as Normal, Warning, or Critical.

The application also evaluates model performance using common machine learning metrics and visualizes vibration trends for monitoring purposes.

---

## ✨ Features

- Machine Failure Prediction
- Predictive Maintenance Recommendations
- Random Forest Classification
- Performance Evaluation
- Model Serialization using Joblib
- Sensor Data Analysis
- Machine Vibration Visualization
- Intelligent Condition Monitoring

---

## 🛠 Technologies Used

- Python
- Pandas
- Scikit-learn
- Matplotlib
- Joblib

---

## 📊 Dataset Features

The model uses the following input features:

- Temperature
- Pressure
- Vibration
- Humidity

Target Variable:

- Machine Failure (0 = Normal, 1 = Failure)

---

## 🤖 Machine Learning Workflow

1. Load IIoT sensor dataset
2. Split training and testing data
3. Train Random Forest Classifier
4. Save trained model
5. Predict machine condition
6. Evaluate model performance
7. Visualize sensor trends

---

## 📈 Evaluation Metrics

- Accuracy
- Precision
- Recall
- F1 Score


---

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/AbdulSami-033/iiot-machine-failure-prediction.git
```

Install dependencies:
```bash
pip install pandas matplotlib scikit-learn joblib
```

Run model training:
```bash
python train_model.py
```

Run prediction:
```bash
python predict_machine.py
```


🎯Learning Outcomes
Machine Learning Classification
Predictive Maintenance
Data Preprocessing
Model Evaluation
Data Visualization
Industrial IoT Concepts
💡 Future Improvements
Real-time IoT sensor integration
Streamlit dashboard
Live monitoring dashboard
MQTT integration
Email alerts
Cloud deployment
Deep Learning models
Time-series forecasting

👨‍💻 Author
GitHub:
```bash
https://github.com/AbdulSami-033
```

⭐ If you found this project useful, consider giving it a star.
