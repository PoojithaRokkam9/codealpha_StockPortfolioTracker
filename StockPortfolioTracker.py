import yfinance as yf

portfolio = {}

def add_stock(symbol, quantity):
    portfolio[symbol] = portfolio.get(symbol, 0) + quantity

def remove_stock(symbol, quantity):
    if symbol in portfolio:
        portfolio[symbol] -= quantity
        if portfolio[symbol] <= 0:
            del portfolio[symbol]

def get_portfolio_value():
    total_value = 0
    for symbol, quantity in portfolio.items():
        stock = yf.Ticker(symbol)
        price = stock.history(period="1d")['Close'][0]
        total_value += price * quantity
    return total_value

while True:
    print("\n1. Add Stock\n2. Remove Stock\n3. View Portfolio Value\n4. Exit")
    choice = input("Choose an option: ")
    if choice == '1':
        symbol = input("Enter stock symbol: ").upper()
        quantity = int(input("Enter quantity: "))
        add_stock(symbol, quantity)
    elif choice == '2':
        symbol = input("Enter stock symbol: ").upper()
        quantity = int(input("Enter quantity: "))
        remove_stock(symbol, quantity)
    elif choice == '3':
      print(portfolio)
      value = get_portfolio_value()
      print(f"Portfolio Value: ${value:.2f}")
    elif choice == '4':
        break