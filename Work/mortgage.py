# mortgage.py
#
# Exercise 1.7
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
extra_payment = 1000
extra_payment_start_month = 61
extra_payment_end_month = 108
month = 0

while principal > 0:
    month += 1
    principal = principal * (1+rate/12) - payment 
    total_paid = total_paid + payment 

    if principal < 0: # check for extra payment and reject that
        total_paid = total_paid + principal
        principal = 0

    if month >= extra_payment_start_month and month <= extra_payment_end_month:
        principal -= extra_payment
        total_paid += extra_payment

    print(f'{month} : {total_paid:.2f} : {principal:.2f}')


print('Total paid', round(total_paid, 1))
print('Months', month)