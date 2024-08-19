import pandas as pd
import yfinance as yf
from requests_cache import CachedSession

# Create a cached session
session = CachedSession('yfinance.cache')
session.headers['User-agent'] = 'my-program/1.0'

# Get the S&P 500 tickers
sp500_tickers = pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')[0]['Symbol'].values.tolist()

# Set the start and end dates for the historical data
start_date = '2010-01-01'
end_date = '2023-02-26'  # or use 'today' for the current date

# Create an Excel writer
with pd.ExcelWriter('sp500_historical_data.xlsx') as writer:
    # Loop through each ticker and download the historical data
    total_tickers = len(sp500_tickers)
    for i, ticker in enumerate(sp500_tickers):
        try:
            ticker_obj = yf.Ticker(ticker, session=session)
            hist = ticker_obj.history(start=start_date, end=end_date)
            
            # Convert the datetime index to timezone unaware
            hist.index = hist.index.tz_localize(None)
            
            # Write the historical data to a separate tab in the Excel file
            hist.to_excel(writer, sheet_name=ticker, index=True)
            
            progress = (i + 1) / total_tickers * 100
            print(f"Data saved for {ticker} ({progress:.2f}% complete)")
        except Exception as e:
            print(f"Error downloading data for {ticker}: {e}")