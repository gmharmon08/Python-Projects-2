# Write a program that counts to 20 and prints each number as it counts.
# If the number is even, also print even. If the number is odd, also print odd.
# Once you've counted to 20, you should ask the user how many odd numbers there were. If they guess correct, print correct. If they guess incorrect, print any message you want.
# Hint - (Make sure your program counts the number of even numbers and number of odd numbers)
# When your program is finished. Print "this is an example of a -insert name here- loop"


for x in range(21):
    print(x)
    if x == 2:
        print("even")
    elif x == 3:
        print("odd")
    elif x == 4:
        print("even")
    elif x == 5:
        print("odd")
    elif x == 6:
        print("even")
    elif x == 7:
        print("odd")
    elif x == 8:
        print("even")
    elif x == 9:
        print("odd")
    elif x == 10:
        print("even")
    elif x == 11:
        print("odd")
    elif x == 12:
        print("even")
    elif x == 13:
        print("odd")
    elif x == 14:
        print("even")
    elif x == 15:
        print("odd")
    elif x == 16:
        print("even")
    elif x == 17:
        print("odd")
    elif x == 18:
        print("even")
    elif x == 19:
        print("odd")
    elif x == 20:
        print("even")
number = input("How many odd numbers were there?")
print(number)
if number == "10":
    print("good job")
else:
    print("You can't count")
print("This is an example of a for loop")
