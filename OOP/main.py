# Importing the classes
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
# We want to print the report of the available resources
is_on = True
# Getting input from the user
# While the machine is still on
while is_on:
    my_menu=Menu()
    # Access the coffee maker class 
    coffee_maker=CoffeeMaker()
    # Access the Money Machine class
    money_machine=MoneyMachine()
    # Access the menu class to get the available items on the menu as a concatenated string
    available_menu_items=my_menu.get_items()
    user_input=input(f"What would you like {available_menu_items}")
    # When the user's input is a report, the result should be the report of the resources and the current profit
    if user_input=="report":
        print(coffee_maker.report())
        print(money_machine.report())
    # if the user types the word "off" it automatically turns off the machine
    elif user_input=="off":
        is_on=False
    # This only lets us remain with the items in the menu or an invalid choice
    else:
    #  The menu class has a function that searches the menu for a particular drink by name.
        # It inturn returns a Menu Item object if it exists other wise returns none
        drink=my_menu.find_drink(user_input)
        # Check if the resources are sufficient
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            # make coffee if resources and the money is sufficient
            coffee_maker.make_coffee(drink)
            
        
        
        
            

       
        
       
        

    
        