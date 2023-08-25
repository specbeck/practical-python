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
            holding = {
                headers[0]: row[0],
                headers[1]: int(row[1]),
                headers[2]: float(row[2]),
            }
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


portfolio = read_portfolio("Data/portfolio.csv")
prices = read_prices("Data/prices.csv")

total_cost = 0.0
for s in portfolio:
    total_cost += s["shares"] * s["price"]

current_value = 0.0
for s in portfolio:
    current_value += s["shares"] * prices[s["name"]]

print("Current value: ", current_value)
print(f"Total loss/gain: {current_value - total_cost}")
