# string = input("Name a city? ")
# print(string)
# float = input("What is a decimal? ")
# print(float)
# boolean = input("Is carti a good rapper? ")
# print(boolean)
# int = input( " What is a whole number? ")
# print(int)


# cats = int(input(" How many cats do you have ?"))

# if cats < 14:
#     print(" You're a loser")
# elif cats == 18:
#     print(" You're a goat")
# elif cats >= 20:
#     print(" You're a bum")
# else :
#     print(" You're a semi-loser")


city = input(" What's your favorite city?").lower()

if city == "birmingham":
    print(" You stink")
elif city == "new york" or city == "los angeles":
    print(" You're alright")
elif len(city) > 12:
    print(" You're a witch who belongs in a ditch")
elif len(city) > 5 and len(city) < 10:
    print(" You're THE goat")
elif city != "gary" and len(city) == 11:
    print(" You're not hood")
else:
    print(" You're the mvp of my life")
