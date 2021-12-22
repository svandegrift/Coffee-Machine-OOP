from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
is_on = True

while is_on:
    user_choice = input(f"What would you like? ({menu.get_items()}): ")
    if user_choice == 'report':
        coffee_maker.report()
        money_machine.report()
    elif user_choice == 'off':
        is_on = False
        break
    elif user_choice in menu.get_items():
        drink = menu.find_drink(user_choice)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
