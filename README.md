# Smart Parking IoT – Occupancy & Demand Forecasting

This project is part of the **Applied Artificial Intelligence (AAI)** program at the **University of San Diego (USD)**.
An Applied AI project demonstrating a Smart Parking IoT architecture with sensor data ingestion, time-series forecasting, deep learning (LSTM), and Tableau-based analytics for urban parking optimization.

**Course:** AAI-530 </br>
**Group:** 10 </br>
**Project Status:** In Progress  

---

## 📌 Project Overview

Urban parking congestion leads to increased traffic, fuel consumption, and user frustration. This project presents a **Smart Parking IoT System** that leverages real-world sensor data to analyze, visualize, and forecast parking occupancy patterns.

Using historical parking sensor data, the system predicts **future parking availability (1–24 hours ahead)** and estimates the **probability of finding a parking spot**, enabling data-driven decision-making for smart city applications.

The solution integrates **IoT architecture**, **time-series forecasting**, **deep learning**, and **interactive dashboards**, making it both technically robust and easy to communicate.

---

## 🎯 Project Objectives

- Analyze real-world IoT parking sensor data
- Forecast short-term parking occupancy using time-series models
- Compare traditional statistical models with deep learning approaches
- Build an end-to-end IoT analytics pipeline
- Visualize real-time status and future availability through dashboards

---
## 👥 Contributors

- **Ved Prakash Dwivedi**  
- **Dhrub Satyam**

---

## 🎓 Faculty Advisor

- **Prof. Anamika Singh**  
  University of San Diego – Applied Artificial Intelligence Program

---

## 🧠 Methods Used

- Internet of Things (IoT)
- Time-Series Analysis
- Machine Learning
- Deep Learning (LSTM)
- Data Analytics & Visualization
- Cloud-Based Data Processing

---

## 🛠️ Technologies

- Python  
- Pandas, NumPy  
- Scikit-learn  
- TensorFlow / Keras  
- Time-Series Databases  
- MQTT Protocol  
- Tableau  
- Git & GitHub  

---

## 📊 Dataset Description

**Main Dataset:** `data\raw\smart_parking_full.csv`  
**Source:** San Francisco Open Data (via Kaggle)  
**Data Type:** Time-series parking occupancy data  

**Key Characteristics:**
- Sensor-based parking space occupancy
- Minute-level and hourly observations
- Clean, structured CSV format with semicolon delimiter
- Real-world IoT data from urban infrastructure
- **508,034 records** with comprehensive sensor readings

**Key Features Include:**
- `timestamp` - Date and time of observation
- `segmentid` - Parking segment identifier
- `capacity` - Total parking spaces in segment
- `occupied` - Currently occupied spaces
- `observed1-10` - Multiple sensor readings
- `diff1-10` - Sensor difference values

**Important Notes:**
- The main dataset file (`smart_parking_full.csv`) is **not** included in `.gitignore` and should be committed to the repository
- Ensure the dataset is placed in `data\raw\` directory before running notebooks
- Dataset uses semicolon (`;`) as delimiter, not comma

---

## 🤖 Machine Learning Tasks

### 1. Time-Series Forecasting (Required)

**Goal:**  
Predict parking occupancy for the next **1–24 hours**

**Models Used:**
- ARIMA (baseline statistical model)
- Linear Regression (baseline comparison)
- LSTM Neural Network (deep learning model)

---

### 2. Deep Learning Task (Required)

**LSTM Model Outputs:**
- Predicted occupancy rate
- Probability of finding a parking spot in the next hour

The LSTM model captures temporal dependencies and recurring patterns such as daily and weekly parking trends.

---

## 📈 Dashboard & Visualization (Tableau)

The Tableau dashboard provides:

- ✅ Current parking occupancy status (live-style metric)
- ✅ Historical utilization trends
- ✅ Predicted parking availability
- ✅ Heatmaps by location and time
- ✅ KPI-style summaries for decision-makers

---

## 🏗️ System Architecture

The system follows a layered IoT architecture:

1. **Sensors & Edge Layer**
   - Parking sensors (IR / Ultrasonic)
   - Edge devices (Raspberry Pi / ESP32)

2. **Network Layer**
   - MQTT protocol
   - Wi-Fi / 4G / LTE communication

3. **Cloud Processing Layer**
   - Time-series data storage
   - ML & LSTM forecasting models
   - Analytics and alert generation

4. **Dashboard Layer**
   - Tableau-based visualization
   - User access via web interface

---

## ⚙️ Installation & Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/smart-parking-iot-forecasting.git
   cd smart-parking-iot-forecasting
   ```

2. Ensure the main dataset is present:
   - The main dataset `data\raw\smart_parking_full.csv` should be included in the repository
   - If missing, download from the project source and place in the specified directory

3. Install required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the notebooks in order:
   - `01_data_overview.ipynb` - Data exploration and understanding
   - `02_cleaning_and_eda.ipynb` - Data cleaning and exploratory analysis
   - `03_time_series_forecasting.ipynb` - Time series analysis and forecasting
   - `04_ml_baseline_models.ipynb` - Machine learning baseline models

---

## 📁 Project Structure

```
smart-parking-iot-forecasting/
├── data/
│   ├── raw/
│   │   └── smart_parking_full.csv     # Main dataset (committed to repo)
│   ├── processed/                    # Processed data (gitignored)
│   └── external/                     # External data (gitignored)
├── notebooks/
│   ├── 01_data_overview.ipynb
│   ├── 02_cleaning_and_eda.ipynb
│   ├── 03_time_series_forecasting.ipynb
│   └── 04_ml_baseline_models.ipynb
├── models/                           # Trained models (gitignored)
├── src/                              # Source code
├── requirements.txt
├── .gitignore                        # Git ignore rules
└── README.md
```

---
## 🚀 Interactive Dashboard

### 📊 **Smart Parking Analytics Dashboard**
A comprehensive, interactive dashboard showcasing parking occupancy insights and model performance.

### **🔗 Quick Access:**
- **[🌐 Open Dashboard](dashboard/fixed_dashboard.html)** - Click to view live dashboard

### **📈 Features:**
- **8 Interactive Charts** including:
  - 📊 Record Types Distribution
  - 🤖 Model Sources Distribution  
  - 📈 Occupancy Rate Time Series
  - 🏆 Model Performance Comparison
  - 📊 Error Distribution Analysis
  - 🔥 Hourly Occupancy Heatmap
  - 🎯 Top Performing Segments
  - 📉 Occupancy Rate Distribution

### **📊 Dataset Overview:**
- **719,882 Records** across 841 parking segments
- **Real-time analytics** with responsive design
- **Modern UI** with gradient styling and animations

### **🛠️ Technical Stack:**
- **Plotly.js** for interactive visualizations
- **Responsive CSS Grid** layout
- **Real-time data** processing and rendering
---
## 🚫 Git Ignore Policy

The `.gitignore` file is configured to:

**Ignore:**
- Processed data files (`data/processed/`)
- External datasets (`data/external/`)
- Trained models (`models/`)
- Jupyter checkpoints (`*.ipynb_checkpoints`)
- Python cache files (`__pycache__/`)
- Virtual environments (`venv/`, `env/`)
- IDE files (`.vscode/`, `.idea/`)
- OS files (`.DS_Store`, `Thumbs.db`)

**Explicitly Include:**
- `data/raw/smart_parking_full.csv` - The main dataset is **NOT ignored** and should be committed

This ensures the main dataset is always available while keeping generated files and temporary artifacts out of version control.
