# AAI530-Group10-smart-parking-iot-forecasting
An Applied AI project demonstrating a Smart Parking IoT architecture with sensor data ingestion, time-series forecasting, deep learning (LSTM), and Tableau-based analytics for urban parking optimization.

# Smart Parking IoT – Occupancy & Demand Forecasting

This project is part of the **Applied Artificial Intelligence (AAI)** program at the **University of San Diego (USD)**.

**Course:** AAI-XXX  
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

**Dataset:** SFpark / Smart Parking Dataset  
**Source:** San Francisco Open Data (via Kaggle)  
**Data Type:** Time-series parking occupancy data  

**Key Characteristics:**
- Sensor-based parking space occupancy
- Minute-level and hourly observations
- Clean, structured CSV format
- Real-world IoT data from urban infrastructure

**Key Features Include:**
- Parking space ID
- Timestamp
- Occupancy status (occupied / available)
- Location metadata

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
2. Install required Python packages:
 ```bash
   pip install -r requirements.txt
