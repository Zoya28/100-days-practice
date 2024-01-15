icon = '''
             __  __                                  _     _            
   ___ ___  / _|/ _| ___  ___   _ __ ___   __ _  ___| |__ (_)_ __   ___ 
  / __/ _ \| |_| |_ / _ \/ _ \ | '_ ` _ \ / _` |/ __| '_ \| | '_ \ / _ \
 | (_| (_) |  _|  _|  __/  __/ | | | | | | (_| | (__| | | | | | | |  __/
  \___\___/|_| |_|  \___|\___| |_| |_| |_|\__,_|\___|_| |_|_|_| |_|\___|
                                                                        
'''

menu = {
    "iced coffee": {
        "Ingredients": {
            "water": 50,
            "milk": 100,
            "coffee": 18,
        },
        "cost": 3.5,
    },
    "latte": {
        "Ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "Ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    },
}

resources = {
    "water": 5000,
    "milk": 5000,
    "coffee": 500,
}
def resources_is_sufficient(order_resources):
    '''check whether resources are sufficient or not'''
    for item in resources:
        if resources[item] < order_resources[item]:
            print(f"sorry, there is not enough {item}.🙏")
            return False
    return True

def process_coins():
    '''calculates the total money inserted by customer'''
    print("\nplease insert coins!")
    total = int(input("how many quarter : ")) * 0.25 
    total += int(input("how many Dimes : ")) *  0.10 
    total += int(input("how many nickles : ")) *  0.05 
    total += int(input("how many Pennies : ")) * 0.01 
    return total

def transaction_successful(money_recieved, drink_cost):
    if money_recieved < drink_cost:
        print("Sorry that's not enough money. Money refunded.🙏")
        return False
    else:
        global profit
        profit += drink["cost"]
        change = round(money_recieved - drink_cost, 2)
        print(f"Here is {change}$ in change.")
        return True
def make_coffee(coffee_name):
    for item in drink["Ingredients"]:
        resources[item] -= drink["Ingredients"][item] 
    print(f"Here is your {coffee_name} ☕")

profit = 0
is_on = True
while is_on:
    choice = input("what would you like?(iced coffee/latte/cappuccino) ")
    if choice == "off":
        is_on = False
        # TODO1 print report
    elif choice == "report":
        print(f"water: {resources['water']}ml")
        print(f"milk: {resources['milk']}ml")
        print(f"coffee: {resources['coffee']}g")
        print(f"money: ${profit}")
    else:
        # TODO2 Check resources sufficient? 
        drink = menu[choice]
        if resources_is_sufficient(drink["Ingredients"]):
            # TODO3 Process coins.
            payment = process_coins()
            # TODO4 Check transaction successful?
            if transaction_successful(payment, drink["cost"]):
                # TODO5 Make coffee
                make_coffee(choice)