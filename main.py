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
profit = 0.0


def report_machine():
    water = resources['water']
    milk = resources['milk']
    coffee = resources['coffee']
    return f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: ${round(profit, 2)}"


def check_resources(drink_name):
    ingredients = MENU[drink_name]['ingredients']
    for ingredient in ingredients:
        if resources[ingredient] < ingredients[ingredient]:
            print(f"Sorry, there is not enough {ingredient}.")
            return False
    return True


def check_money(coins, drink_name):
    if coins >= MENU[drink_name]['cost']:
        return True
    print("Sorry that's not enough money. Money refunded.")
    return False


def sum_coins(num_of_quarters, num_of_dimes, num_of_nickles, num_of_pennies):
    return round(0.25 * num_of_quarters + 0.1 * num_of_dimes + 0.05 * num_of_nickles + 0.01 * num_of_pennies, 2)


def calc_change(coins, drink_name):
    return round(coins - MENU[drink_name]['cost'], 2)


while is_machine_work:
    choice = ""
    while choice not in possible_commands:
        choice = input("   What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "off":
        is_machine_work = False
    elif choice == "report":
        print(report_machine())
    else:
        if check_resources(choice):
            print("Please insert coins.")
            quarters = int(input("how many quarters?: "))
            dimes = int(input("how many dimes?: "))
            nickles = int(input("how many nickles?: "))
            pennies = int(input("how many pennies?: "))
            payment = sum_coins(quarters, dimes, nickles, pennies)
            if check_money(payment, choice):
                print(f"Here is ${calc_change(payment, choice)} in change.")
                resources['water'] -= MENU[choice]['ingredients']['water']
                if 'milk' in MENU[choice]['ingredients']:
                    resources['milk'] -= MENU[choice]['ingredients']['milk']
                resources['coffee'] -= MENU[choice]['ingredients']['coffee']
                profit += MENU[choice]['cost']
                print(f"Here is your {choice} ☕. Enjoy!")
