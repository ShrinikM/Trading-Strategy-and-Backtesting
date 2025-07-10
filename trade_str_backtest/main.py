import yfinance as yf

ticker = yf.Ticker("AAPL")
hist = ticker.history(period="6mo")  # past 6 months
print(hist.tail())

info = ticker.info
print(info["longName"])
print(info["sector"])
print(info["marketCap"])
print(info["dividendYield"])
print()

# print(ticker.earnings)       # Yearly earnings
# print(ticker.quarterly_earnings)

# print(ticker.financials)     # Income statement
# print(ticker.balance_sheet)
# print(ticker.cashflow)
print(ticker.dividends)
print(ticker.splits)