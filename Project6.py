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
