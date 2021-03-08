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

possible_commands = ["off", "report", "espresso", "latte", "cappuccino"]
is_machine_work = True
money = 0.0


def report_machine():
    water = resources['water']
    milk = resources['milk']
    coffee = resources['coffee']
    return f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: ${round(money, 2)}"


def check_resources(drink_name):
    ingredients = MENU[drink_name]['ingredients']
    for ingredient in ingredients:
        if resources[ingredient] < ingredients[ingredient]:
            return False, ingredient
    return True, ""


def sum_coins(num_of_quarters, num_of_dimes, num_of_nickles, num_of_pennies):
    return round(0.25 * num_of_quarters + 0.1 * num_of_dimes + 0.05 * num_of_nickles + 0.01 * num_of_pennies, 2)


while is_machine_work:
    command = ""
    while command not in possible_commands:
        command = input("   What would you like? (espresso/latte/cappuccino): ").lower()
    if command == "off":
        is_machine_work = False
    elif command == "report":
        print(report_machine())
    else:
        is_enough, what_to_low = check_resources(command)
        if is_enough:
            print("Please insert coins.")
            quarters = int(input("how many quarters?: "))
            dimes = int(input("how many dimes?: "))
            nickles = int(input("how many nickles?: "))
            pennies = int(input("how many pennies?: "))
            payment = sum_coins(quarters, dimes, nickles, pennies)
            cost = MENU[command]['cost']
            if payment > cost:
                change = round(payment - cost, 2)
                print(f"Here is ${change} in change.")
                resources['water'] -= MENU[command]['ingredients']['water']
                if 'milk' in MENU[command]['ingredients']:
                    resources['milk'] -= MENU[command]['ingredients']['milk']
                resources['coffee'] -= MENU[command]['ingredients']['coffee']
                money += cost
                print(f"Here is your {command} ☕. Enjoy!")
            else:
                print("Sorry that's not enough money. Money refunded.")
        else:
            print(f"Sorry, there is not enough {what_to_low}.")
