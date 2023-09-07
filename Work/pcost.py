# pcost.py
#
# Exercise 1.27
import csv 
import sys

def portfolio_cost(filename):
    total_cost = 0
    with open(filename, 'rt') as file:
        reader = csv.reader(file)
        headers = next(reader) # Filtering headers
        for rowno, row in enumerate(reader, start=1):
            record = dict(zip(headers, row))
            try:
                nshares = int(record['shares'])
                price = float(record['price'])
                total_cost += nshares * price
            # This catches errors in int() and float() conversions above
            except ValueError:
                print(f'Row {rowno}: Bad row: {row}')

    return total_cost

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print('Total cost:', cost)