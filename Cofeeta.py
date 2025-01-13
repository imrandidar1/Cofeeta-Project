import os

print("Welcome to Cofeeta!")
menu = {
    1: ("Espresso", 200),
    2: ("Latte", 250),
    3: ("Cappuccino", 300),
    4: ("Mocha", 275),
    5: ("Tea", 100)
}

customers_file = "customers.txt"
customers = {}

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def load_customers():
    global customers
    if os.path.exists(customers_file):
        try:
            with open(customers_file, "r") as file:
                for line in file:
                    customer_id, name = line.strip().split(',', 1)
                    customers[customer_id] = name
        except Exception as e:
            print(f"Error loading customers: {e}")
            customers = {}
    else:
        print(f"No customer file found. Starting fresh.")

def save_customers():
    with open(customers_file, "w") as file:
        for customer_id, name in customers.items():
            file.write(f"{customer_id},{name}\n")

def show_menu():
    print("Here is the menu:")
    for num, (item, price) in menu.items():
        print(f"{num}. {item}: {price} Taka")

def place_order():
    show_menu()
    items = input("Enter the item numbers you want, separated by commas: ").split(',')
    try:
        items = [int(item.strip()) for item in items if int(item.strip()) in menu]
    except ValueError:
        print("Invalid input. Please enter numbers corresponding to the menu items.")
        return

    if items:
        total = sum(menu[item][1] for item in items)
        customer_id = input("Enter your 3-digit customer ID for a discount (or press Enter to skip): ").strip()
        if customer_id in customers and customer_id.isdigit() and len(customer_id) == 3:
            total *= 0.95  # Apply 5% discount
            print(f"5% discount applied for {customers[customer_id]}.")
        print(f"Final total: {total:.2f} Taka")
    else:
        print("No valid items ordered.")
    input("Press Enter to return to the main menu.")
    clear_screen()

def view_customers():
    if customers:
        for customer_id, name in customers.items():
            print(f"ID: {customer_id}, Name: {name}")
    else:
        print("No customers available.")

def search_customer():
    customer_id = input("Enter the customer ID to search: ").strip()
    if customer_id in customers:
        print(f"Customer Found: ID: {customer_id}, Name: {customers[customer_id]}")
    else:
        print("Customer not found.")

def add_customer():
    while True:
        customer_id = input("Enter new customer ID (3-digit number): ").strip()
        if customer_id.isdigit() and len(customer_id) == 3:
            if customer_id in customers:
                print("Customer ID already exists. Try another.")
            else:
                break
        else:
            print("Invalid ID. Please enter a 3-digit number.")
    name = input("Enter customer name: ").strip()
    customers[customer_id] = name
    save_customers()
    print("Customer added.")

def delete_customer():
    customer_id = input("Enter customer ID to delete: ").strip()
    if customer_id in customers:
        del customers[customer_id]
        save_customers()
        print("Customer deleted.")
    else:
        print("Customer ID not found.")

def edit_customer():
    customer_id = input("Enter the customer ID to edit: ").strip()
    if customer_id in customers:
        new_name = input(f"Enter the new name for customer {customer_id} (current: {customers[customer_id]}): ").strip()
        if new_name:
            customers[customer_id] = new_name
            save_customers()
            print("Customer details updated.")
        else:
            print("No changes made.")
    else:
        print("Customer ID not found.")

def manage_customers():
    while True:
        print("Customer Management Menu:")
        print("1. Add a customer")
        print("2. View all customers")
        print("3. Search for a customer")
        print("4. Edit a customer")
        print("5. Delete a customer")
        print("6. Return to main menu")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            clear_screen()
            add_customer()
            input("Press Enter to return to the customer management menu.")
            clear_screen()
        elif choice == "2":
            clear_screen()
            view_customers()
            input("Press Enter to return to the customer management menu.")
            clear_screen()
        elif choice == "3":
            clear_screen()
            search_customer()
            input("Press Enter to return to the customer management menu.")
            clear_screen()
        elif choice == "4":
            clear_screen()
            edit_customer()
            input("Press Enter to return to the customer management menu.")
            clear_screen()
        elif choice == "5":
            clear_screen()
            delete_customer()
            input("Press Enter to return to the customer management menu.")
            clear_screen()
        elif choice == "6":
            clear_screen()
            break
        else:
            print("Invalid choice. Please try again.")
            clear_screen()

# Load customer data at startup
load_customers()

if not customers:
    print("Customer file loaded but contains no data.")

while True:
    print("Main Menu:")
    print("1. Place an order")
    print("2. Manage customers")
    print("3. Exit")
    choice = input("Enter your choice: ").strip()
    clear_screen()

    if choice == "1":
        place_order()
    elif choice == "2":
        manage_customers()
    elif choice == "3":
        print("Thank you! Please come again.")
        break
    else:
        print("Invalid choice. Please try again.")
