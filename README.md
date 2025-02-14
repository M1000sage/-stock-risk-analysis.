# Stock Risk Analysis

A Python-based open-source project for fetching historical stock data and performing risk analysis. The project uses Yahoo Finance (`yfinance`) to retrieve stock data and calculates key risk metrics like volatility, Value at Risk (VaR), Conditional VaR (CVaR), and the Sharpe Ratio.

## Features
- Fetch full historical stock data from Yahoo Finance
- Perform risk analysis with key financial metrics
- Generate stock price and return distribution plots
- Supports NSE (India) and global stock markets

## Installation

```bash
pip install -r requirements.txt
```

## Usage
Run the script and enter a stock ticker when prompted:

```bash
python stock_risk_analysis.py
```

Or use it as a module in Python:

```python
from stock_risk_analysis import get_stock_data, risk_analysis, plot_stock, plot_returns

# Get stock data for Apple (AAPL)
data = get_stock_data("AAPL")
if data is not None:
    risks = risk_analysis(data)
    print(risks)
    plot_stock(data, "AAPL")
    plot_returns(data, "AAPL")
```

## Risk Metrics Explained
- **Volatility**: Measures annualized risk based on daily returns.
- **Value at Risk (VaR 95%)**: Estimates the worst expected loss at a 95% confidence level.
- **Conditional Value at Risk (CVaR 95%)**: The average loss beyond the VaR threshold.
- **Sharpe Ratio**: Risk-adjusted return metric.

## Example Output
```
Risk Analysis for Entire Market Period:
Volatility: 0.2514
VaR_95: -0.0345
CVaR_95: -0.0456
Sharpe Ratio: 1.1234
```

## Dependencies
- `yfinance`
- `pandas`
- `numpy`
- `matplotlib`
- `seaborn`

Install dependencies using:

```bash
pip install -r requirements.txt
```

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing
Contributions are welcome! Feel free to submit a pull request.

## Support
If you encounter any issues, create an issue on GitHub or reach out via email.

## Acknowledgments
- Built using Yahoo Finance API (`yfinance`).

