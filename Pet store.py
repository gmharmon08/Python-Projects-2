# number = (int("42"))
# print(type(number))

# create a program that asks the user for two numbers and adds the numbers together (make sure you print this nuumber FOR THE USER TO SEE)
# if the sum of the numbers are greater than 50, tell the user they suck
# if the numbers are less than or equal to 50, tell the user they're allright


# no1 = int(input("pick a number? "))
# print(no1)

# no2 = int(input("pick another number? "))
# print(no2)

# product = no1 * no2 + 2

# print("your product is")
# print(product)

# if product > 50:
#     print("You suck")
# elif product <= 50:
#     print("You're alright")


# create a program that asks the user what type of pet they would like to purchase (their choices are a dog, cat, turtle, or parrot)
# prints the name of whatever pet they purchased as well as its cost (the cost is up to you)
# then ask the user if they would also like to buy pet food (for the sake of this project, all petfood costs the same price "again the price is up to you")
# print the cost of the pet food and the total cost of the transaction (pet pricee + pet food price). Make sure to include printed messages similar to "Total Transaction cost:" so the output is easy to understand

pet = input("Purchase dog, cat, turtle, or parrot?")
print(pet)

if pet == "dog":
    print("$12 please")

if pet == "cat":
    print("$13 please")

if pet == "turtle":
    print("$20 please")

if pet == "parrot":
    print("$19 please")

food = input("Buy pet food as well?")
print(food)

if food == "yes":
    print("$6 please")

if pet == "parrot" and food == "yes":
    print("Your total is $25")

elif pet == "cat" and food == "yes":
    print("Your total is $19")

elif pet == "dog" and food == "yes":
    print("Your total is $18")

elif pet == "turtle" and food == "yes":
    print("Your total is $26")

else:
    print("have a nice day")