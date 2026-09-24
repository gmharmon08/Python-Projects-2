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
