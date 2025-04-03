import yfinance as yf
import pandas as pd

def get_stock_data(stock_symbol, start_date, end_date):
    """Fetch stock data from Yahoo Finance."""
    stock = yf.download(stock_symbol, start=start_date, end=end_date)
    return stock['Adj Close']  # Get adjusted closing prices

def save_stock_data(stock_symbol, start_date, end_date, filename):
    """Fetch and save stock data to CSV."""
    stock_data = get_stock_data(stock_symbol, start_date, end_date)
    stock_data.to_csv(filename)
    print(f"Stock data saved to {filename}")

if __name__ == "__main__":
    save_stock_data("AAPL", "2020-01-01", "2024-01-01", "data/aapl_stock.csv")
