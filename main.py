from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


cashier = MoneyMachine()
barista = CoffeeMaker()
menu = Menu()

turned_on = True

while turned_on:
    choice = ""
    while not choice:
        choice = input(f"What would you like? ({menu.get_items()}): >")
        if choice != "report" and choice != "off":
            choice = menu.find_drink(choice)
        elif choice == "report":
            barista.report()
            cashier.report()
            choice = ""
            continue
        elif choice == "off":
            turned_on = False
            break
        else:
            pass
        if barista.is_resource_sufficient(choice) and cashier.make_payment(choice.cost):
            barista.make_coffee(choice)
