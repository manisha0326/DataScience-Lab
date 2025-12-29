'''
5. Menu-Driven File Operations 
● Write data to a file 
● Read data from a file 
● Append data to a file 
● Handle invalid user input and file errors using exception handling
'''

filename = "data.txt"

while True:
    print("\n--- File Menu ---")
    print("1. Write to file")
    print("2. Read from file")
    print("3. Append to file")
    print("4. Exit")

    try:
        choice = int(input("Enter your choice (1-4): "))

        if choice == 1:
            try:
                text = input("Enter data to write: ")
                with open(filename, "w") as f:
                    f.write(text + "\n")
                print("Data written successfully.")
            except IOError:
                print("Error writing to file!")

        elif choice == 2:
            try:
                with open(filename, "r") as f:
                    print("\nFile Contents:")
                    print(f.read())
            except FileNotFoundError:
                print("File not found!")

        elif choice == 3:
            try:
                text = input("Enter data to append: ")
                with open(filename, "a") as f:
                    f.write(text + "\n")
                print("Data appended successfully.")
            except IOError:
                print("Error appending to file!")

        elif choice == 4:
            print("Exiting program.")
            break

        else:
            print("Invalid choice! Please enter 1–4.")

    except ValueError:
        print("Invalid input! Please enter a number.")
