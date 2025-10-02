# 📊 Sales Data Analysis & Forecasting

**Description:** This Python script provides a comprehensive pipeline for extracting, analyzing, and visualizing sales data using `pandas`, `matplotlib`, and `scikit-learn`. It includes trend analysis, smoothing, correlation insights, quarterly aggregation, and basic forecasting.

---

## 🧰 Requirements

Ensure the following Python libraries are installed:

```bash
pip install pandas matplotlib numpy scikit-learn
```

---

## 📁 Input

- **data.csv**: A CSV file containing monthly sales data.
  - Must include a `Month` column (e.g., "2023-01") and one or more product columns with unit sales.

---

## 🚀 Features

### 1. **Data Overview**
- Displays dataset structure and the first few rows.
- Converts `Month` to datetime format for time-based operations.

### 2. **Sales Trend Plot**
- Line plot showing monthly sales trends for each product.
- Helps visualize seasonality and performance over time.

### 3. **Moving Average Smoothing**
- Applies a 3-month moving average to smooth out short-term fluctuations.
- Useful for identifying long-term trends.

### 4. **Correlation Analysis**
- Prints a correlation matrix to show relationships between product sales.
- Helps detect patterns or dependencies.

### 5. **Top-Selling Product**
- Calculates total units sold per product.
- Identifies the highest-selling product across the dataset.

### 6. **Quarterly Aggregation**
- Groups data by fiscal quarters.
- Visualizes quarterly sales using bar charts.

### 7. **Sales Forecasting**
- Uses linear regression to predict sales for the next 3 months.
- Forecasts are plotted alongside actual data for comparison.

---

## 📈 Output

- Multiple plots displayed using `matplotlib`:
  - Monthly sales trends
  - Smoothed trends (3-month moving average)
  - Quarterly sales bar chart
  - Forecasted sales for each product

- Console outputs:
  - Dataset info
  - Correlation matrix
  - Top-selling product
  - Quarterly sales summary

---

## 🧠 Notes

- Ensure the `Month` column is in a recognizable date format.
- The forecasting model is basic and assumes linear trends—consider more advanced models for better accuracy.
- Missing or malformed dates will be coerced to `NaT` and may affect analysis.
