import yfinance as yf
import pandas_datareader as pdr
import pandas as pd

# Define the tech companies index ticker
tech_index_ticker = '^NDX'  # Nasdaq-100 Index

# Define the economic indicators
indicators = ['GDP', 'CPI', 'UNRATE', 'DFF']

# Define the start and end dates
start_date = '2010-01-01'
end_date = '2024-08-20'

# Pull the tech companies index data
tech_index_data = yf.download(tech_index_ticker, start=start_date, end=end_date)['Adj Close']

# Pull the economic indicators data
gdp_data = pdr.get_data_fred('GDPC1', start_date, end_date)  # GDP growth rate
inflation_data = pdr.get_data_fred('CPIAUCSL', start_date, end_date)  # Inflation rate
unemployment_data = pdr.get_data_fred('UNRATE', start_date, end_date)  # Unemployment rate
interest_data = pdr.get_data_fred('DFF', start_date, end_date)  # Federal Funds Effective Rate

# Calculate the growth rates for GDP and inflation
gdp_growth_rate = gdp_data.pct_change() * 100
inflation_rate = inflation_data.pct_change() * 100

# Create a DataFrame to store the data
data = pd.DataFrame(index=pd.date_range(start_date, end_date))
data['Tech Index'] = tech_index_data
data['GDP Growth Rate'] = gdp_growth_rate
data['Inflation Rate'] = inflation_rate
data['Unemployment Rate'] = unemployment_data
data['Interest Rate'] = interest_data

# Replace NaN values in the tech index with the mean of the last 5 days
data['Tech Index'].fillna(data['Tech Index'].rolling(window=5, min_periods=1).mean(), inplace=True)

# Replace NaN values in GDP growth rate, inflation rate, and unemployment rate with the last existing value
data['GDP Growth Rate'].fillna(method='ffill', inplace=True)
data['Inflation Rate'].fillna(method='ffill', inplace=True)
data['Unemployment Rate'].fillna(method='ffill', inplace=True)

# Print the data
print(data.head())

# Save the data to a CSV file
data.to_csv('economic_data.csv', index=True)