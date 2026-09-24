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

# P2
# Use a function or multiple functions to complete task
# Write a program that repeatedly asks the user for a number until they type "stop".
# This program will repeatedly add the users numbers together and print " -insert number here- added" each time a new number is entered.
# When the user stops the program, the program prints the total of all the numbers the user added.
# If the user's total is greater than 200, print a response of your choice
# If the user's total is less than or equal to 200, print a different response of your choice

# Answer this question - What is a libary in python?
total = 0


def calculator_question():
    global user_input
    user_input = input("Can you pick a number? (type stop to end program)")


def calculator_repeat():
    global user_input
    global total
    while user_input.lower() != "stop":
        print(f"{user_input} added")
        total = int(user_input) + total
        user_input = input("Can you pick a number? (type stop to end program)")


def calculator_result():
    print("Your total is:")
    print(total)
    if total > 200:
        print("I need a movieeeee")
    elif total <= 200:
        print("Go home dork")


calculator_question()

calculator_repeat()

calculator_result()
