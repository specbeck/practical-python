# pcost.py
#
# Exercise 1.27
cost  = 0

with open('Data/portfolio.csv', 'rt') as file:
    headers = next(file)
    for line in file:
        stock = line.split(',')
        cost += int(stock[1]) * float(stock[2])

print('Total cost', cost)