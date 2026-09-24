# create a program that asks the user for two numbers and adds the numbers together (make sure you print this nuumber FOR THE USER TO SEE)
# if the sum of the numbers are greater than 50, tell the user they suck
# if the numbers are less than or equal to 50, tell the user they're allright


no1 = int(input("pick a number? "))
print(no1)

no2 = int(input("pick another number? "))
print(no2)

product = no1 * no2 + 2

print("your product is")
print(product)

if product > 50:
    print("You suck")
elif product <= 50:
    print("You're alright")
