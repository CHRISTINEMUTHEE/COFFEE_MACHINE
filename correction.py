
#A full code on an automated coffee machine.

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
# Revenue made
Revenue=2.5
# A function to check for resources
def enough_resources(drink_ingredient):
    #" This checks whether the user input is enought to supply drink"
    for item in drink_ingredient:
        if drink_ingredient[item]>=AV_RESOURCES[item]:
            print(f"Sorry there is not enough {item}.")
            return False
        return True
# Function to process the coins,compile total and give change while updating the profit
def process_coins(drink_cost):
    penny=float(input("How many Pennies :"))
    Nickel=float(input("How many Nickels :"))
    Dime=float(input("How many Dimes: "))
    Quater=float(input("How many Quaters: "))
    # Total
    Total_cash=(penny*0.01)+(Nickel*0.05)+(Dime*0.1)+(Quater*0.25)
    # Adding to the revenue
    global Revenue
    Revenue += drink_cost
    # Change processing
    if Total_cash>=drink_cost:
        change=Total_cash-drink_cost
        # Return change
        print(f"Here is {round(change,2)} in change")
        return True
    else:
        print("Sorry, there's not enough money, Money refunded")
        return False
# Function to make coffee
def make_coffee(drink_ingredients,user_input): 
    for item in drink_ingredients:
        AV_RESOURCES[item]-=drink_ingredients[item]
    print(f"Here's your {user_input} enjoy !")
        
            
# Asking a user whether they_d like coffee as long as its on
is_on=True

while is_on:
    user_input=input("What would you like? (espresso/latte/cappuccino): ")
    if user_input=="off":
        is_on=False
        # Printing a report of the resources in the machine
    elif user_input=="report":
        print(f"Water:{AV_RESOURCES['water']}ml")
        print(f"Milk: {AV_RESOURCES['milk']}ml"),
        print(f"Coffee:{AV_RESOURCES['coffee']}g"),
        print(f"Money:{Revenue} $")
    else:
        drink=MENU2[user_input]
        # Checking for enough resources
        if enough_resources(drink["Ingredients"]):
            # Proceeding to process coins
            print("Please insert the coins: ")
            if process_coins(drink["cost"]):
                # Making coffee
                make_coffee(drink["Ingredients"],user_input)
        
        
        
        