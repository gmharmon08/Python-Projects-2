# Create a program that asks the user for each grocery item they need to purchase until they type "STOP"
# After each item is added, you should display (aka print) "-insert item here- added"
# Also after each item is added, determine how much the item costs and add it to a total cost that will be used for a receipt
# If the length of the item (letter count) is greater than or equal to 7, the item costs 5 dollars, less than 7 it costs 2 dollars
# By the end, You program should display first display the number of grocery items on your list, the entire list of grocery items, and a receipt total
# Receipt - (make it sort of look like a real receipt when you print)
# Hint - (Make sure your program stores each item into a list, remember list_name.append() to your desired list) -lists can initially be empty-


groceries = []

total = 0

user_input = input(
    "What items do you need to purchasee? (type STOP to end program)")
groceries.append(user_input)

while user_input != "STOP":
    print(f"{user_input} added")
    if len(user_input) >= 7:
        total = 5 + total
    else:
        total = 2 + total

    user_input = input(
        "What items do you need to purchase? (type STOP to end program)")
    if user_input != "STOP":
        groceries.append(user_input)

print(f"{len(groceries)} items total")

for x in groceries:
    print(x)


print(f'your total is: {total}$')
