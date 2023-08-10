# pcost.py
#
# Exercise 1.27
import csv 
import sys

def portfolio_cost(filename):
    cost = 0
    with open(filename, 'rt') as file:
        reader = csv.reader(file)
        next(reader) # Filtering headers
        for row in reader:
            try:
                num = int(row[1])
                value = float(row[2])
                cost += num * value
            except ValueError:
                print('WARNING: Data missing...', row)

    return cost

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print('Total cost:', cost)