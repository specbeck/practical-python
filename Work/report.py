# report.py
#
# Exercise 2.4
import csv
from pprint import pprint


def read_portfolio(filename):
    portfolio = []

    with open(filename, "rt") as f:
        rows = csv.reader(f)
        headers = next(rows)

        for row in rows:
            holding = dict(zip(headers, row))
            
            holding['shares'] = int(holding['shares'])
            holding['price'] = float(holding['price'])

            portfolio.append(holding)

    return portfolio


def read_prices(filename):
    stocks = {}

    with open(filename, "rt") as f:
        rows = csv.reader(f)
        for row in rows:
            if row == []:
                continue
            stocks[row[0]] = float(row[1])

    return stocks


def make_report(stocks, prices):
    report = []
    for stock in stocks:
        stock_name = stock['name']
        if stock_name in prices.keys():
            change = prices[stock_name] - stock['price']
            tup = (stock_name, stock['shares'], prices[stock_name], change)
            report.append(tup)
    return report


portfolio = read_portfolio("Data/portfoliodate.csv")
prices = read_prices("Data/prices.csv")

report = make_report(portfolio, prices)

total_cost = 0.0
for s in portfolio:
    total_cost += s["shares"] * s["price"]

current_value = 0.0
for s in portfolio:
    current_value += s["shares"] * prices[s["name"]]

print("Current value: ", current_value)
print(f"Total loss/gain: {current_value - total_cost}")

headers = ('Name', 'Shares', 'Price', 'Change')
print('%10s %10s %10s %10s' % headers)
print(('-' * 10 + ' ') * len(headers))
for name, shares, price, change in report:
    price = f'${price:.2f}'
    print(f'{name:>10s} {shares:>10d} {price:>10s} {change:>10.2f}')