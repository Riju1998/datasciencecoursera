# author: Seema Kumari Patel
# Enhanced implementation of data extraction, analysis, and visualization using pandas & matplotlib

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

# Read the CSV file
df = pd.read_csv("data.csv")

# Display basic info
print("Dataset Info:")
print(df.info())
print("\nFirst few rows:\n", df.head())

# Ensure Month is treated properly
if 'Month' in df.columns:
    df['Month'] = pd.to_datetime(df['Month'], errors='coerce')

# -----------------------------
# 1. Sales Trend Plot
# -----------------------------
plt.figure(figsize=(10, 6))
for col in df.columns[1:]:
    plt.plot(df['Month'], df[col], marker='o', label=col)

plt.title("Monthly Sales Data")
plt.xlabel("Month")
plt.ylabel("Units Sold")
plt.legend()
plt.grid(True)
plt.show()

# -----------------------------
# 2. Moving Average (Trend Smoothing)
# -----------------------------
plt.figure(figsize=(10, 6))
for col in df.columns[1:]:
    df[f"{col}_MA3"] = df[col].rolling(window=3).mean()
    plt.plot(df['Month'], df[f"{col}_MA3"], label=f"{col} (3M Avg)")

plt.title("Moving Average (3-Month)")
plt.xlabel("Month")
plt.ylabel("Smoothed Units Sold")
plt.legend()
plt.grid(True)
plt.show()

# -----------------------------
# 3. Correlation Analysis
# -----------------------------
print("\nCorrelation Matrix:")
print(df.corr(numeric_only=True))

# -----------------------------
# 4. Top-Selling Product
# -----------------------------
totals = df.drop(columns=['Month']).sum()
top_product = totals.idxmax()
print(f"\nTop-Selling Product: {top_product} with {totals[top_product]} units sold.")

# -----------------------------
# 5. Quarterly Aggregation
# -----------------------------
if 'Month' in df.columns:
    df['Quarter'] = df['Month'].dt.to_period("Q")
    quarterly_sales = df.groupby("Quarter").sum(numeric_only=True)
    print("\nQuarterly Sales:\n", quarterly_sales)

    quarterly_sales.plot(kind="bar", figsize=(10, 6))
    plt.title("Quarterly Sales by Product")
    plt.xlabel("Quarter")
    plt.ylabel("Units Sold")
    plt.grid(True)
    plt.show()

# -----------------------------
# 6. Forecast using Linear Regression (basic)
# -----------------------------
if 'Month' in df.columns:
    df['MonthNum'] = np.arange(len(df))  # numerical month index

    forecast_months = 3
    future_x = np.arange(len(df), len(df) + forecast_months).reshape(-1, 1)

    plt.figure(figsize=(10, 6))
    for col in df.columns[1:]:
        X = df[['MonthNum']]
        y = df[col]
        model = LinearRegression()
        model.fit(X, y)

        future_pred = model.predict(future_x)
        plt.plot(df['Month'], df[col], marker='o', label=f"{col} Actual")
        plt.plot(pd.date_range(df['Month'].iloc[-1], periods=forecast_months + 1, freq='M')[1:], 
                 future_pred, linestyle="--", label=f"{col} Forecast")

    plt.title("Sales Forecast (Next 3 Months)")
    plt.xlabel("Month")
    plt.ylabel("Units Sold")
    plt.legend()
    plt.grid(True)
    plt.show()
