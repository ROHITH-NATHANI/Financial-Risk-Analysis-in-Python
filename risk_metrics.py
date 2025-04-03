import numpy as np
import pandas as pd

def calculate_monthly_returns(data):
    """Calculate monthly percentage returns."""
    return data.resample('M').ffill().pct_change()

def calculate_volatility(stock_returns):
    """Calculate standard deviation (volatility) of stock returns."""
    return stock_returns.std()

def calculate_beta(stock_returns, market_returns):
    """Calculate Beta (Market Risk)."""
    covariance_matrix = np.cov(stock_returns[1:], market_returns[1:])  
    beta = covariance_matrix[0, 1] / covariance_matrix[1, 1]  
    return beta

def calculate_treynor_ratio(stock_returns, risk_free_rate, beta):
    """Calculate Treynor Ratio."""
    excess_return = stock_returns.mean() - risk_free_rate  
    treynor_ratio = excess_return / beta  
    return treynor_ratio

def calculate_var(stock_returns, confidence_level=0.95):
    """Calculate Value at Risk (VaR) at a given confidence level."""
    return np.percentile(stock_returns.dropna(), (1 - confidence_level) * 100)

if __name__ == "__main__":
    print("Risk metrics module loaded successfully.")
