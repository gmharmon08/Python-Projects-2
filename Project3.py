# Write a program that repeatedly asks the user for a number until they type "stop".
# This program will repeatedly add the users numbers together and print " -insert number here- added" each time a new number is entered.
# When the user stops the program, the program prints the total of all the numbers the user added.
# If the user's total is greater than or equal to 150, print a response of your choice
# If the user's total is less than 150, print a different response of your choice
# When your program is finished. Print "this is an example of a -insert name here- loop"

total = 0
user_input = input("Can you pick a number? (type stop to end program)")

while user_input.lower() != "stop":
    print(f"{user_input} added")
    total = int(user_input) + total
    user_input = input("Can you pick a number? (type stop to end program)")

print("Your total is:")
print(total)
if total >= 150:
    print("Suns out Buns out")
elif total < 150:
    print("Get your money up")
