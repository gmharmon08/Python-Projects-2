# P1
# Use a function or multiple functions to complete task
# Also after each item is added, determine how much the item costs and add it to a total cost that will be used for a receipt
# If the length of the item (letter count) is greater than 6, the item costs 9 dollars, less than or equal to 6 it costs 4 dollars
# By the end, You program should display first display the number of grocery items on your list, the entire list of grocery items, and a receipt total as well as a receipt ID
# Receipt - (make it sort of look like a real receipt when you print)
# Hint - There is a  built in function called random.randint() and when you set it equal to a variable, it will generate a random number for you within your given range

# Ex:
# import random
# random_number = random.randint(1,2)

import random
grocceries = []

total = 0

receipt_id = random.randint(10000000, 999999900)

user_input = input(
    "What goods are you purchasing? (type STOP to end program): ")

while user_input != "STOP":
    grocceries.append(user_input)
    print(f"{user_input} added")
    if len(user_input) <= 6:
        total = 4 + total
    else:
        total = 9 + total
    user_input = input(
        "What goods are you purchasing? (type STOP to end program): ")

print(f"{len(grocceries)} items total")

for x in grocceries:
    print(x)

print(f'your total is: {total}$')
print(f'Receipt ID: {receipt_id}')
