# Book Data and Market Data using Yahoo Finance API

This repository contains two Python scripts that download and save data from the Yahoo Finance API:

1. `book_data_sp500_yfinance.py`: Downloads and saves book data (fundamental data) (financials, balance sheet, cashflow, etc.) for all S&P 500 companies. The data is saved in different "ticker".xlsx files.
2. `market_data_sp500_yfinance.py`: Downloads and saves historical market data for all S&P 500 companies (prices, volumes). The data is saved in one .xlsx.

## Requirements

* Python 3.x
* `pandas` library
* `yfinance` library
* `requests_cache` library

## Yahoo Finance API

This project uses the Yahoo Finance API to fetch data. Please note that:

* The Yahoo Finance API is used under the terms of the [Yahoo Terms of Service](https://policies.yahoo.com/us/en/yahoo/terms/index.htm) and [Yahoo Developer API Terms of Use](https://legal.yahoo.com/us/en/yahoo/terms/product-atos/apiforydn/index.html).
* The API is subject to rate limits, and excessive usage may result in IP blocking.
* The API may change or be discontinued at any time, which could affect the functionality of this project.


## Usage

1. Run `book_data_sp500_yfinance.py` to download and save book data for all S&P 500 companies. This will create separate Excel files for each company.
2. Run `market_data_sp500_yfinance.py` to download and save historical market data for all S&P 500 companies. This will create a single Excel file with separate tabs for each company.

## Note

* Make sure to install the required libraries using `pip install pandas yfinance requests-cache`.
* The scripts use a cached session to avoid hitting the Yahoo Finance API rate limits. The cache is stored in a file named `yfinance.cache`.
* The scripts may take some time to complete, depending on the number of companies and the amount of data being downloaded.
