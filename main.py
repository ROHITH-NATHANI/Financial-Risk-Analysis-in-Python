import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from src.data_fetcher import get_stock_data
from src.risk_metrics import *
from src.report_generator import generate_pdf_report

def plot_stock_returns(stock_returns, var_95):
    """Plot stock return distribution & VaR threshold."""
    plt.figure(figsize=(10,5))
    sns.histplot(stock_returns.dropna(), bins=50, kde=True)
    plt.axvline(var_95, color='r', linestyle='dashed', linewidth=2, label=f'VaR 95%: {var_95:.4f}')
    plt.title("Stock Returns Distribution & Value at Risk (VaR)")
    plt.xlabel("Returns")
    plt.ylabel("Frequency")
    plt.legend()
    plt.show()

def main():
    # Fetch stock & market data
    stock_data = get_stock_data("AAPL", "2020-01-01", "2024-01-01")
    market_data = get_stock_data("^GSPC", "2020-01-01", "2024-01-01")

    # Calculate returns
    stock_returns = calculate_monthly_returns(stock_data)
    market_returns = calculate_monthly_returns(market_data)

    # Compute risk metrics
    std_dev = calculate_volatility(stock_returns)
    beta = calculate_beta(stock_returns.dropna(), market_returns.dropna())
    treynor_ratio = calculate_treynor_ratio(stock_returns, risk_free_rate=0.02, beta=beta)
    var_95 = calculate_var(stock_returns, confidence_level=0.95)

    # Display results
    print(f"Standard Deviation: {std_dev:.4f}")
    print(f"Beta: {beta:.4f}")
    print(f"Treynor Ratio: {treynor_ratio:.4f}")
    print(f"Value at Risk (95% confidence): {var_95:.4f}")

    # Plot returns
    plot_stock_returns(stock_returns, var_95)

    # Generate PDF report
    generate_pdf_report("reports/risk_report.pdf", std_dev, beta, treynor_ratio, var_95)

if __name__ == "__main__":
    main()
