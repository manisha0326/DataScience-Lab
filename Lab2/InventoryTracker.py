''' Inventory Tracker 
Imagine a small store inventory like {"apple": 10, "banana": 5, "milk": 2}. Program should allow 
adding new items, selling items (subtract quantity), and print items that are low in stock (<3). '''

inventory = {"apple": 10, "banana": 5, "milk": 2}

def add_item(name, qty):
    if name in inventory:
        inventory[name] += qty
    else:
        inventory[name] = qty
    print(f"{qty} {name}(s) added.")

def sell_item(name, qty):
    if name not in inventory:
        print("Item not found!")
    elif inventory[name] < qty:
        print("Not enough stock!")
    else:
        inventory[name] -= qty
        print(f"Sold {qty} {name}(s).")

def low_stock():
    print("\nLow stock items (<3):")
    for item, qty in inventory.items():
        if qty < 3:
            print(f"{item}: {qty}")

while True:
    print("\nInventory Menu:")
    print("1. Add Item")
    print("2. Sell Item")
    print("3. Show Low Stock Items")
    print("4. Show All Inventory")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        name = input("Enter item name: ")
        qty = int(input("Enter quantity to add: "))
        add_item(name, qty)
    elif choice == "2":
        name = input("Enter item name: ")
        qty = int(input("Enter quantity to sell: "))
        sell_item(name, qty)
    elif choice == "3":
        low_stock()
    elif choice == "4":
        print("\nCurrent Inventory:")
        for item, qty in inventory.items():
            print(f"{item}: {qty}")
    elif choice == "5":
        print("Exiting program.")
        break
    else:
        print("Invalid choice! Please try again.")

