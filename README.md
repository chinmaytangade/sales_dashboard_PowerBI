# 🧭 Simple Sales Dashboard (Power BI)

### 👨‍💻 Author: Chinmay Tangade.  
---

## 🎯 Objective
Create an interactive dashboard that visualizes **sales performance by product, region, and month** using the Superstore Sales dataset.  
This project demonstrates how data visualization can help business users identify key trends and profitable regions.

---

## 🛠 Tools & Technologies
- **Power BI** → Dashboard design & visualization  
- **Python + Pandas** → *(Optional)* data cleaning and preprocessing  
- **Dataset:** `Superstore_Sales.csv`

---

## 📊 Dashboard Features
1. 📈 **Line Chart** → Sales trend over months  
2. 📊 **Bar Chart** → Sales by region  
3. 🍩 **Donut Chart** → Sales by category  
4. 🎚 **Slicer/Filter** → Region or category selection  
5. 🎨 **Color Highlights** → Emphasize top-performing areas  

---

## 🧹 Data Cleaning (Python Example)
```python
import pandas as pd

df = pd.read_csv("Superstore_Sales.csv")
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Month-Year'] = df['Order Date'].dt.to_period('M')
df.to_csv("Superstore_Sales_Cleaned.csv", index=False)
