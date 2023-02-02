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


def is_resources_left(order_ingredients):
    for items in order_ingredients:
        if order_ingredients[items] >= resources[items]:
            print(f'Sorry there is not enough {items}')
            return False
    return True


def process_coins():
    """RETURN THE TOTAL CALCULATED COINS"""
    print("Please insert coins.")
    total = 0
    total += int(input("How many quarters?: "))*0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickles?: "))*0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total


def is_transaction_success(money_received, drink_cost):
    """RETURN TREE WHEN THE PAYMENT IS ACCEPTED, OR FALSE IF MONEY IS INSUFFICIENT."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} is the change")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    global resources
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}")


profit = 0
machine_on = True

while machine_on:
    choice = input("What would you like? (espresso/latte/cappuccino)")
    if choice == "off":
        machine_on = False
    elif choice == "report":
        print(f'Water: {resources["water"]}ml\nMilk: {resources["milk"]}ml\nCoffee: {resources["coffee"]}g\nMoney: ${profit}')
    elif choice == "espresso" or choice == "latte" or choice == "cappuccino":
        drink = MENU[choice]
        if is_resources_left(order_ingredients=drink["ingredients"]):
            payment = process_coins()
            if is_transaction_success(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
