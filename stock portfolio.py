# Initialize an empty portfolio dictionary
portfolio = {}

def add_stock(symbol, shares):
    if symbol in portfolio:
        portfolio[symbol] += shares  # Increment shares if stock already exists
    else:
        portfolio[symbol] = shares  # Add new stock to portfolio
    print(f"{shares} shares of {symbol} added to the portfolio.")

def remove_stock(symbol, shares):
    if symbol in portfolio:
        if portfolio[symbol] >= shares:
            portfolio[symbol] -= shares
            if portfolio[symbol] == 0:
                del portfolio[symbol]  # Remove stock if no shares left
            print(f"{shares} shares of {symbol} removed from the portfolio.")
        else:
            print(f"Error: Insufficient shares of {symbol} in the portfolio.")
    else:
        print(f"Error: {symbol} is not in the portfolio.")

def display_portfolio():
    print("Current Portfolio:")
    for symbol, shares in portfolio.items():
        print(f"{symbol}: {shares} shares")

# Example usage
add_stock('AAPL', 10)
add_stock('GOOGL', 5)
add_stock('AAPL', 5)  # Add more shares of existing stock
display_portfolio()

remove_stock('AAPL', 8)  # Remove some shares
remove_stock('GOOGL', 5)  # Remove all shares of a stock
display_portfolio()