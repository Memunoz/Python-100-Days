import os


def clear():
    os.system("clear")


MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    },
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}

money = {"penny": 0.01, "nickel": 0.05, "dime": 0.10, "quarter": 0.25}


def menu_choice():
    while True:
        try:
            choice1 = input("What would you like? (espresso/latte/cappuccino): ")
            if (
                choice1 == "espresso"
                or choice1 == "latte"
                or choice1 == "cappuccino"
                or choice1 == "report"
                or choice1 == "off"
                or choice1 == "menu"
            ):
                return choice1
            else:
                print("Plz select between (espresso/latte/cappuccino): ")
        except ValueError:
            print("Plz select between (espresso/latte/cappuccino): ")


def cobrar(pedido):
    print(f"total ${MENU[pedido]['cost']}")
    print("Insert coins:")
    while True:
        try:
            penny = (
                float(input("How many pennies you want to insert? ")) * money["penny"]
            )
            nickel = (
                float(input("How many nickels you want to insert? ")) * money["nickel"]
            )
            dime = float(input("How many dimes you want to insert? ")) * money["dime"]
            quarter = (
                float(input("How many quarters you want to insert? "))
                * money["quarter"]
            )
            dinero = penny + nickel + dime + quarter
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    if dinero < MENU[pedido]["cost"]:
        print("Sorry, that's not enough money. Money refunded.\n")
        work()
    else:
        vuelto = round(dinero - MENU[pedido]["cost"], 2)
        print(f"Your change is: ${vuelto}")
        resources["money"] += MENU[pedido]["cost"]
        resources["coffee"] -= MENU[pedido]["ingredients"]["coffee"]
        resources["milk"] -= MENU[pedido]["ingredients"]["milk"]
        resources["water"] -= MENU[pedido]["ingredients"]["water"]
        print(f"Here is your {pedido}. Enjoy!")
        work()


def stock_check(flavor):
    missing_ingredients = []
    if resources["coffee"] < MENU[flavor]["ingredients"]["coffee"]:
        missing_ingredients.append("coffee")
    if resources["milk"] < MENU[flavor]["ingredients"]["milk"]:
        missing_ingredients.append("milk")
    if resources["water"] < MENU[flavor]["ingredients"]["water"]:
        missing_ingredients.append("water")

    if missing_ingredients:
        print(
            f"Sorry, we don't have enough of the following ingredients: {', '.join(missing_ingredients)}."
        )
        work()
    else:
        return True


def work():
    while True:
        print()
        choice2 = menu_choice()
        clear()
        if choice2 == "report":
            print(resources)
        elif choice2 == "off":
            print("Goodbye")
            exit()
        elif choice2 == "menu":
            for item, details in MENU.items():
                print(f"Flavor: {item}")
                print(f"Ingredients: {details['ingredients']}")
                print(f"Cost: ${details['cost']}")
                print()
        else:
            if stock_check(choice2):
                cobrar(choice2)


work()
