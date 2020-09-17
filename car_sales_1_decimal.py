# Car Sales
# Takes a car's input value and adds tax, title, dealer prep and destination fees

car = int(input("Please enter the price of the car: $"))
tax = car * .0675
title = 15
prep = 100
dest = 275
total = car + tax + title + prep + dest

print("Your new car's total is: $", total)

