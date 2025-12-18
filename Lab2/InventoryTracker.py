inventory = {"apple": 10, "banana": 5, "milk": 2}

while True:
    print("\n--- Inventory Menu ---")
    print("1. Add new item")
    print("2. Sell item")
    print("3. Show low stock items (<3)")
    print("4. Show full inventory")
    print("5. Exit")

    choice = input("Enter your choice: ")

    # ---------------- ADD NEW ITEM ----------------
    if choice == "1":
        item = input("Enter item name: ").lower()
        qty = input("Enter quantity: ")

        if qty.isdigit():
            qty = int(qty)
            if item in inventory:
                inventory[item] += qty
            else:
                inventory[item] = qty
            print(f"{item} added/updated successfully!")
        else:
            print("Invalid quantity!")

    # ---------------- SELL ITEM ----------------
    elif choice == "2":
        item = input("Enter item to sell: ").lower()

        if item not in inventory:
            print("Item not found!")
            continue

        qty = input("Enter quantity to sell: ")

        if qty.isdigit():
            qty = int(qty)
            if qty <= inventory[item]:
                inventory[item] -= qty
                print(f"Sold {qty} {item}.")
            else:
                print("Not enough stock!")
        else:
            print("Invalid quantity!")

    # ---------------- LOW STOCK ----------------
    elif choice == "3":
        print("\nLow Stock Items (<3):")
        low = [item for item, qty in inventory.items() if qty < 3]

        if low:
            for i in low:
                print(f"- {i} ({inventory[i]})")
        else:
            print("No low stock items!")

    # ---------------- SHOW INVENTORY ----------------
    elif choice == "4":
        print("\nCurrent Inventory:")
        for item, qty in inventory.items():
            print(f"{item}: {qty}")

    # ---------------- EXIT ----------------
    elif choice == "5":
        print("Exiting program.")
        break

    else:
        print("Invalid choice! Try again.")
