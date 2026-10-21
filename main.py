
# Func defs

def display_products(products):
    i = 1
    for item, price in products.items():
        print(f"{i}. {item}: ${price}")
        i += 1
    print(f"{i}. Quit")

def get_number(prompt, validmin, validmax):
    while True:
        try:
            num = int(input(prompt))
            if validmin <= num <= validmax:
                return num
            else:
                print(f"Invalid input. Please enter a number between {validmin} and {validmax}.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Var init

product_list = {
    "Crisps": "1",
    "Chocolate": "1.5",
    "Water": "1.2",
}

balance = 2

# --- Vending MACHINE ---
#         Entry

# Repeat program until exit selected
while True:
    display_products(product_list)

    # Init values
    user_choice = -1
    item_name = ""
    item_price = -1

    # While user choice is in invalid range, keep prompting for input
    while user_choice < 1 or user_choice > len(product_list) + 1:
        user_choice = get_number("Please select an option: ", 1, len(product_list) + 1)

        # Test exit condition before indexing to prevent out of range error
        if(user_choice == len(product_list) + 1):
            print("Thank you for using the vending machine!")
            quit()

        # Converet dict keys to a list and index it
        item_name = list(product_list.keys())[user_choice - 1]
        # Retrieve the price of the selected item and format it to 2 decimal places
        item_price = float(product_list[item_name])

        # Check price against balance
        if(item_price > balance):
            print(f"Insufficient funds. Your balance is £{balance}. Please select a different option.")
            user_choice = -1  # Reset user_choice to prompt for input again

    # If the user has sufficient funds to escape the while loop, deduct the item price from the balance
    balance -= float(item_price)

    print(f"You selected option {item_name}.\nPrice: £{item_price}.")
    print(f"Your remaining balance is £{balance:.2f}.")