# Make a virtual coffee Machine
from CoffeeMachineData import resources, MENU
profit = 0
should_continue = True


def is_resource_sufficient(order_ingredients):
    """Returns true when order can be made, False if ingredients are insufficient"""
    is_enough = True
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            is_enough = False
    return is_enough


def process_coin():
    """Return total calculated from coins inserted"""
    print("Please insert coin")
    total = int(input("How many quarters"))
    total += int(input("How many dime")) * 0.1
    total += int(input("How many nickel")) * 0.05
    total += int(input("How many penny")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    """Return true if payment is accepted ,or false if money is insufficient"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}🥧. Enjoy!☺")


while should_continue:
    choice = input("What would you like?(expresso/latte/cappuccino): ")
    if choice == 'off':
        should_continue = False
    elif choice == 'report':
        print(f"water: {resources['water']}ml")
        print(f"milk: {resources['milk']}ml")
        print(f"coffee: {resources['coffee']}g")
        print(f"Money: {profit}$")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink['ingredients']):
            payment = process_coin()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
