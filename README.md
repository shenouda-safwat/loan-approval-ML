# 🎬 Netflix Stock Price Prediction Using Linear Regression

---

## 📈 Project Overview

This project predicts the **closing stock price** of Netflix using **Linear Regression** based on historical stock data.  
It includes **data preprocessing**, **technical feature engineering**, **time-series modeling**, and comprehensive evaluation using multiple **regression metrics**.  
The model provides accurate predictions and can serve as the base for more complex forecasting systems.

---

## 🗂️ Dataset

The dataset contains daily historical stock data for Netflix:

### **Price & Technical Features**
- `Open`  
- `High`  
- `Low`  
- `Volume`  
- `MA50` – 50-day Moving Average  
- `MA200` – 200-day Moving Average  

### **Target Variable**
- `Close`: Closing stock price (regression target)

📦 Dataset File: `archive.zip`

---

## 🔍 Data Preprocessing

- Handled missing values (if any)  
- Created moving averages: **MA50**, **MA200**  
- Scaled features if necessary  
- Applied **time-series split** (no shuffling):  
  - **Training set**: 80%  
  - **Test set**: 20%

---

## 📊 Feature Selection

```python
features = ['Open', 'High', 'Low', 'Volume', 'MA50', 'MA200']
