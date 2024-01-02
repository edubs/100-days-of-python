from coffee_maker import CoffeeMaker
from menu import Menu
from money_machine import MoneyMachine

my_menu = Menu()
my_coffee_maker = CoffeeMaker()
my_money_machine = MoneyMachine()


def print_report():
    print(my_coffee_maker.report())
    print(my_money_machine.report())


while True:
    customer_choice = input(f"What would you like? ({my_menu.get_items()}):")
    if customer_choice == "off":
        exit(0)
    elif customer_choice == "report":
        print_report()
    else:
        beverage_object = my_menu.find_drink(customer_choice)

        if my_coffee_maker.is_resource_sufficient(beverage_object) and my_money_machine.make_payment(
                beverage_object.cost):
            print(f"enough resources to make the drink are available")
            my_coffee_maker.make_coffee(beverage_object)
            print_report()
