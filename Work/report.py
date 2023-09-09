# report.py
#
# Exercise 2.4
import csv
from pprint import pprint


def read_portfolio(filename):
    """
    Read a stock portfolio file into a list of dictionaries with keys
    name, shares, and price.
    """
    portfolio = []

    with open(filename, "rt") as f:
        rows = csv.reader(f)
        headers = next(rows)

        for row in rows:
            holding = dict(zip(headers, row))

            holding["shares"] = int(holding["shares"])
            holding["price"] = float(holding["price"])

            portfolio.append(holding)

    return portfolio


def read_prices(filename):
    """
    Read a CSV file of price data into a dict mapping names to prices.
    """
    stocks = {}

    with open(filename, "rt") as f:
        rows = csv.reader(f)
        for row in rows:
            if row == []:
                continue
            stocks[row[0]] = float(row[1])

    return stocks


def get_cost(portfolio):
    """ Get the total cost of a portfolio."""
    total_cost = 0.0
    for s in portfolio:
        total_cost += s["shares"] * s["price"]
    return total_cost


def get_current_value(portfolio, prices):
    """ Get the current value of stocks in a portfolio based on prices."""
    current_value = 0.0
    for s in portfolio:
        current_value += s["shares"] * prices[s["name"]]
    return current_value


def make_report(stocks, prices):
    """
    Make a list of (name, shares, price, change) tuples given a portfolio list
    and prices dictionary.
    """
    report = []
    for stock in stocks:
        stock_name = stock["name"]
        if stock_name in prices.keys():
            change = prices[stock_name] - stock["price"]
            tup = (stock_name, stock["shares"], prices[stock_name], change)
            report.append(tup)
    return report


def print_report(report):
    """
    Print a nicely formated table from a list of (name, shares, price, change) tuples.
    """
    headers = ("Name", "Shares", "Price", "Change")
    print("%10s %10s %10s %10s" % headers)
    print(("-" * 10 + " ") * len(headers))
    for name, shares, price, change in report:
        price = f"${price:.2f}"
        print(f"{name:>10s} {shares:>10d} {price:>10s} {change:>10.2f}")


def portfolio_report(portfolio_filename, prices_filename):
    """
    Make a stock report given portfolio and price data files.
    """
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)
    report = make_report(portfolio, prices)

    current_value = get_current_value(portfolio, prices)
    total_cost = get_cost(portfolio)

    print("Current value:", current_value)
    print(f"Total loss/gain: {current_value - total_cost}")

    print_report(report)

portfolio_report('Data/portfolio.csv', 'Data/prices.csv')
