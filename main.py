from os import system
from time import sleep
import json

def clear_screen():
    sleep(1.5)
    system('cls')

def get_ailse(ailses):
    smallest_queue_ailse = 1
    for ailse in range(len(list(ailses.keys())), 0, -1):
        if ailses[str(ailse)] <= ailses[str(smallest_queue_ailse)]: smallest_queue_ailse = ailse

    return smallest_queue_ailse

def update_ailses(ailses, orders):
    for order in orders:
        if orders[order]["Done"]: ailses[orders[order]["Ailse"]] = -1
    return ailses

def save_orders(orders):
    with open("orders.json", "w") as f:
        f.write(json.dumps(orders,indent=4))

def save_ailses(ailses):
    with open("ailses.json", "w") as f:
        f.write(json.dumps(ailses,indent=4))

def load_ailses():
    with open("ailses.json", "r") as f:
        ailses = json.load(f)

    return ailses

def load_orders():
    with open("orders.json", "r") as f:
        orders = json.load(f)

    return orders

def print_orders(orders):
    print("Order Number \t\t Done \t\t Ailse")
    for order in orders:
         print(f"{order}\t\t\t {orders[order]['Done']} \t\t {orders[order]['Ailse']}")

def prompt(message):
    print(message)
    sleep(1.5)

def print_menu():
    print("Menu")
    print("1) Get Ailse")
    print("2) Change Order Status")
    print("3) Exit")

def get_integer_input(message, valid_options = []):
    while True:
        try:
            selected_option = int(input(message))
            if len(valid_options) == 0: return selected_option
            if selected_option in valid_options: return selected_option

        except:
            prompt("Must be a number!")
        
        prompt("Enter a valid option!")

orders = load_orders()
ailses = load_ailses()

while True:
    update_ailses(ailses, orders)
    clear_screen()
    print_orders(orders)
    print_menu()
    option = get_integer_input(">> ", [1,2,3])

    if option == 1:
        order_number = get_integer_input("Order Number: ")
        ailse = get_ailse(ailses)
        ailses[str(ailse)] += 1
        orders[order_number] = {"Done": False, "Ailse": ailse}
        print(f"Ailse: {ailse}")

    elif option == 2:
        order_number = get_integer_input("Order Number: ")
        if orders[order_number]["Done"] == False: orders[order_number]["Done"] = True
        else: orders[order_number]["Done"] = False
        print(f"Done: {orders[order_number]['Done']}")

    elif option == 3:
        break
         
    save_orders(orders)
    save_ailses(ailses)
