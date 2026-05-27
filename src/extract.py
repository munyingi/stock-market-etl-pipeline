import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta
import os

symbols = ['AAPL', 'GOOGL', 'TSLA', 'MSFT']
end_date = datetime.now()
start_date = end_date - timedelta(days=365)

print("=" * 60)
print("📊 STOCK DATA EXTRACTION")
print("=" * 60)
print(f"\nFetching data from {start_date.date()} to {end_date.date()}\n")

os.makedirs('data/raw', exist_ok=True)

for symbol in symbols:
    try:
        print(f"Fetching {symbol}...", end=" ")
        data = yf.download(symbol, start=start_date, end=end_date, progress=False)
        data.reset_index(inplace=True)
        data.columns = [col.lower() for col in data.columns]
        data['symbol'] = symbol
        data = data.dropna()
        data.to_csv(f'data/raw/{symbol.lower()}.csv', index=False)
        print(f"OK ({len(data)} records)")
    except Exception as e:
        print(f"ERROR: {e}")

print("\n✅ EXTRACTION COMPLETE!\n")
