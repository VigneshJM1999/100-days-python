QUARTERS = 0.25
DIMES = 0.10
NICKELS = 0.05
PENNIES = 0.01

sales = 0

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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def report():
    print("=== Report ===")
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${sales}\n")


def make_payment(price):
    total_payment = 0
    total_payment += int(input("How many quarters? ")) * QUARTERS
    total_payment +=int(input("How many dimes? ")) * DIMES
    total_payment += int(input("How many nickels? ")) * NICKELS
    total_payment += int(input("How many pennies? ")) * PENNIES

    print(f"You inserted a total of ${total_payment}")
    change = round(total_payment - price, 2)

    if change >= 0:
        if change > 0:
            print(f"Your change is ${change}.")
        return True
    else:
        print("There is not enough money. Refunding the money.")
        return False

def check_resources(choice):
    order_ingredients = MENU[choice]["ingredients"]
    for item in order_ingredients:
        if resources.get(item, 0) < order_ingredients[item]:
            print(f"Apologies! There is not enough {item}.")
            return False
    return True

def prepare_order(choice):
    global sales
    if check_resources(choice):
        if make_payment(MENU[choice]["cost"]):
            for item in MENU[choice]["ingredients"]:
                resources[item] -= MENU[choice]["ingredients"][item]
            print(f"The transaction is successful! Here, please enjoy your {choice} ☕!")
            sales += MENU[choice]["cost"]



is_machine_on = True
while is_machine_on:
    order = input('What would you like to order? (espresso/latte/cappuccino): ').lower()
    if order == 'off':
        is_machine_on = False
    elif order == 'report':
        report()
    elif order in MENU:
        prepare_order(order)
    else:
        print("Please select a valid item in menu.")
