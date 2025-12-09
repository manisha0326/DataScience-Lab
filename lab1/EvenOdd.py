num = input("Enter a number: ")

if num.isdigit():
    n = int(num)

    if n % 2 == 0:
        print(f"{n} is even.")
    else:
        print(f"{n} is odd.")

else:
    print("Please enter a valid integer.")