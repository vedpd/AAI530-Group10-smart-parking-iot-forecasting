# Smart Parking IoT – Occupancy & Demand Forecasting

This project is part of the **Applied Artificial Intelligence (AAI)** program at the **University of San Diego (USD)**.
An Applied AI project demonstrating a Smart Parking IoT architecture with sensor data ingestion, time-series forecasting, deep learning (LSTM), and Tableau-based analytics for urban parking optimization.

**Course:** AAI-530 </br>
**Group:** 10 </br>
**Project Status:** Completed

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

## 📊 Smart Parking IoT – Occupancy & Demand Analytics Dashboard

### 🔗 Live Dashboard
- **[🌐 Open Interactive Tableau Dashboard](https://public.tableau.com/app/profile/dhrub.satyam/viz/SmartParking_Group10_AAI530/Dashboard1)**

---

## 🚀 Overview

The **Smart Parking IoT – Occupancy & Demand Analytics Dashboard** is an end-to-end analytics interface designed to monitor parking utilization, evaluate forecasting performance, and support data-driven operational decisions.

Built using IoT sensor telemetry and machine learning outputs, the dashboard provides a unified view of:

- Real-world parking occupancy behavior  
- Forecasted vs actual demand patterns  
- Model performance benchmarking  
- Temporal demand insights for operational planning  

This dashboard serves as a decision-support layer for smart city and intelligent transportation systems.

---

## 🧠 Analytics Objectives

The dashboard focuses on three core analytical goals:

1. **Occupancy Monitoring**
   - Track real-time and historical occupancy trends.
   - Identify usage patterns across time.

2. **Demand Forecast Validation**
   - Compare machine learning forecasts with actual occupancy.
   - Assess predictive reliability for planning and resource allocation.

3. **Model Performance Evaluation**
   - Benchmark forecasting models using standardized error metrics.
   - Support data-driven model selection.

---

## 📈 Dashboard Visualizations

### 1️⃣ Occupancy Trend
- **Visualization Type:** Time-series line chart  
- **Purpose:** Displays average occupancy rate over time to identify demand cycles, anomalies, and seasonality.

---

### 2️⃣ LSTM Forecast: Predicted vs Actual Occupancy Rate
- **Visualization Type:** Dual-line comparison chart  
- **Purpose:** Compares LSTM model predictions against observed occupancy to evaluate forecasting quality and trend alignment.

---

### 3️⃣ Occupancy Heatmap (Day × Hour)
- **Visualization Type:** Heatmap  
- **Purpose:** Highlights peak usage windows by hour of day and day of week, enabling operational optimization and staffing decisions.

---

### 4️⃣ Model Comparison: Forecast Error by Model (MAPE)
- **Visualization Type:** Bar chart  
- **Models Evaluated:**
  - Gradient Boosting  
  - Linear Regression  
  - LSTM  
  - Neural Network  
  - Random Forest  

- **Purpose:** Benchmarks forecasting models using Mean Absolute Percentage Error (MAPE) to identify the most reliable approach.

---

### 5️⃣ Current Occupancy Status (KPI Indicator)
- **Visualization Type:** KPI summary card  
- **Purpose:** Provides an at-a-glance operational metric showing current occupancy level for quick situational awareness.

---

## 🏗️ Architecture Context

IoT Sensors → Data Pipeline → Feature Engineering → ML Forecasting → Tableau Analytics Layer

The dashboard represents the **final analytics and decision layer** of the Smart Parking IoT system, translating raw telemetry and model outputs into actionable insights.

---

## 💡 Key Insights Enabled

- Identification of peak occupancy periods
- Forecast accuracy validation through visual comparison
- Model benchmarking for continuous improvement
- Real-time operational monitoring
- Data-driven capacity planning

---

## 🔬 Technology Stack

- **Data Source:** IoT Parking Sensor Data  
- **Modeling:** LSTM, Gradient Boosting, Random Forest, Neural Networks, Linear Regression  
- **Analytics & Visualization:** Tableau Public  
- **Programming:** Python (Data Processing & ML Pipeline)

---

## 📌 Business Impact

This dashboard demonstrates how IoT telemetry combined with machine learning can support:

- Smart city parking optimization  
- Reduced congestion through demand forecasting  
- Improved resource allocation  
- Proactive operational decision-making  

It reflects a production-style analytics workflow where predictive modeling and interactive visualization work together to drive actionable intelligence.

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


