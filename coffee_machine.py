# A Dictionary with the menu and available resources
MENU2 = {"expresso": {"Ingredients":
                      {"water": 50, "coffee": 18},
                      "cost": 1.5},
         "latte": {"Ingredients":
                   {"water": 200, "milk": 150, "coffee": 24},
                   "cost": 2.5},
         "cappucinno": {"Ingredients":
                        {"water": 250, "milk": 100, "coffee": 24},
                        "cost": 3.0}}
AV_RESOURCES = {"water": 300,
                "milk": 200,
                "coffee": 100}

# A function that takes in the input,does the resource cheker,prints the report and checks the coins before subtracting from the resources
machine_on=True
# Resource checker
def enough_resources(ingredients):
    for item in ingredients:
        if ingredients[item]>=AV_RESOURCES[item]:
            print(f"Sorry, there is not enough {item}")
        else:
            pass
# Resource update
def resource_remaining(ingredients):
    for items in ingredients:
        NEW_RESOURCES=AV_RESOURCES[items]-ingredients[items]
        print(NEW_RESOURCES)
while machine_on:
    user_input = input("What would you like? (expresso/latte/cappucinno or report)")
    def coffee_maker(user_input):
        # Checking available resources
        enough_resources(MENU2[user_input]["Ingredients"])
        # Coin checker
        print("Please Insert Coins")
        penny=float(input("How many Pennies :"))
        Nickel=float(input("How many Nickels :"))
        Dime=float(input("How many Dimes: "))
        Quater=float(input("How many Quaters: "))
        Total_cash=(penny*0.01)+(Nickel*0.05)+(Dime*0.1)+(Quater*0.25)
        #
        if Total_cash>=float(MENU2[user_input]['cost']):
            change=Total_cash-float(MENU2[user_input]['cost'])
            print(f"Here's your {user_input} ..... enjoy !")
            print(f"Here is {round(change,2)} in change")
        else:
            print("Sorry, there's not enough money, Money refunded")
    # Report..
    if user_input ==  "report":
        print(f"Report before purchasing is {AV_RESOURCES}")
    elif user_input=="off":
        
        machine_on=False
    else:
        coffee_maker(user_input)
    
        
        
            
  
   

