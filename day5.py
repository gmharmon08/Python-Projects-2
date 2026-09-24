# P1
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

# P2
# Write a program that counts to 20 and prints each number as it counts.
# If the number is even, also print even. If the number is odd, also print odd.
# Once you've counted to 20, you should ask the user how many odd numbers there were. If they guess correct, print correct. If they guess incorrect, print any message you want.
# Hint - (Make sure your program counts the number of even numbers and number of odd numbers)
# When your program is finished. Print "this is an example of a -insert name here- loop"


# for x in range(21):
#     print(x)
#     if x == 2:
#         print("even")
#     elif x == 3:
#         print("odd")
#     elif x == 4:
#         print("even")
#     elif x == 5:
#         print("odd")
#     elif x == 6:
#         print("even")
#     elif x == 7:
#         print("odd")
#     elif x == 8:
#         print("even")
#     elif x == 9:
#         print("odd")
#     elif x == 10:
#         print("even")
#     elif x == 11:
#         print("odd")
#     elif x == 12:
#         print("even")
#     elif x == 13:
#         print("odd")
#     elif x == 14:
#         print("even")
#     elif x == 15:
#         print("odd")
#     elif x == 16:
#         print("even")
#     elif x == 17:
#         print("odd")
#     elif x == 18:
#         print("even")
#     elif x == 19:
#         print("odd")
#     elif x == 20:
#         print("even")
# number = input("How many odd numbers were there?")
# print(number)
# if number == "10":
#     print("good job")
# else:
#     print("You can't count")
# print("This is an example of a for loop")
