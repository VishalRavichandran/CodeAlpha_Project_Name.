import yfinance as yf

portfolio = {}

def add_stock(ticker, quantity):
    portfolio[ticker] = quantity
    print(f"Added {quantity} shares of {ticker} to the portfolio.")

def track_performance():
    print("Current Portfolio:")
    for ticker, quantity in portfolio.items():
        stock = yf.Ticker(ticker)
        current_price = stock.history(period="1d")['Close'].iloc[0]
        print(f"{ticker}: {quantity} shares, Current Price: ${current_price:.2f}")

add_stock('AAPL', 10)
add_stock('MSFT', 5)
track_performance()
