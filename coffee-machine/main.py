MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
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
    }
}
profit = 0.0
resources = {
    "water": 50,
    "milk": 200,
    "coffee": 100,
}


def print_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${profit}")


def check_resources(customer_request):
    print(f"customer requesting: {customer_request}")
    enough_resources = True
    for r in customer_request["ingredients"]:
        if resources[r] - customer_request["ingredients"][r] < 0:
            print(f"Sorry, there is not enough {r}.")
            enough_resources = False
    return enough_resources


def process_coins(cost_of_item):
    enough_money = False
    print("Please insert coins.")
    quarters = float(input("How many quarters?: "))
    dimes = float(input("How many dimes?: "))
    nickels = float(input("How many nickels?: "))
    pennies = float(input("How many pennies?: "))
    quarters *= 0.25
    dimes *= 0.10
    nickels *= 0.05
    pennies *= 0.01
    total = quarters + dimes + nickels + pennies
    if cost_of_item > total:
        print("Sorry that's not enough money. Money refunded.")
    else:
        change = total - cost_of_item
        print(f"Here is {round(change, 2)} in change.")
        global profit
        profit += cost_of_item
        enough_money = True
        return enough_money


def subtract_resources(customer_request):
    for r in customer_request["ingredients"]:
        resources[r] -= customer_request["ingredients"][r]
    print_report()


menu_choice = input("What would you like? (espresso/latte/cappuccino): ")

if menu_choice == "off":
    exit(0)
elif menu_choice == "report":
    print_report()
elif menu_choice in MENU:
    if check_resources(MENU[menu_choice]):
        if process_coins(MENU[menu_choice]["cost"]):
            print(f"Here is your {menu_choice}. Enjoy!")
            subtract_resources(MENU[menu_choice])

