import yfinance as yf
stock=yf.Ticker("AAPL")
print(stock.history(period="1d"))
