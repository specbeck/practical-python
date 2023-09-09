#!/usr/bin/env python
# pcost.py
#
# Exercise 1.27
from report import read_portfolio
import sys


def portfolio_cost(filename):
    """Computes the total cost (shares*price) of a portfolio file."""
    portfolio = read_portfolio(filename)
    return sum([s["shares"] * s["price"] for s in portfolio])


def main(args):
    if len(args) != 2:
        sys.exit(f"Usage: {args[0]} portfile")

    filename = args[1]
    print("Total cost:", portfolio_cost(filename))


if __name__ == "__main__":
    main(sys.argv)
