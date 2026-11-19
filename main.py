
import yfinance as yf
import pandas as pd

# 1. Select TCS stock
ticker = "TCS.NS"

# 2. Download historical data
stock = yf.Ticker(ticker)

data = stock.history(
    period="5y",
    interval="1d",
    auto_adjust=True
)

# 3. Display first five records
print(data.head())

# 4. Display dataset dimensions
print("\nDataset Shape:", data.shape)

# 5. Display column information
print("\nDataset Information:")
print(data.info())

# 6. Save the dataset
data.to_csv("data/TCS_stock_data.csv")

print("\nData collection completed!")

print(data.head())
print(data.shape)
print(data.info())

print("duplicate rows:",data.duplicated().sum())

data= data.dropna();
print("rows after dropping duplicates:",data.shape[0])
