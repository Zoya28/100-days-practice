from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
my_menu = Menu()
my_coffee_maker = CoffeeMaker()
my_money_machine = MoneyMachine()
is_on = True
while is_on:
    order = input(f"what would you like? ({my_menu.get_items()}) ")
    if order == "report":
        my_coffee_maker.report()
    elif order == "off":
        is_on = False
    else:  
        drink = my_menu.find_drink(order)
        if my_coffee_maker.is_resource_sufficient(drink) and my_money_machine.make_payment(drink.cost):
            my_coffee_maker.make_coffee(drink)

