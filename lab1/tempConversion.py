'''9. Write a program that takes a temperature in Celsius, and converts it to Fahrenheit and 
Kelvin, based on the choice of user. '''

temp = input("Enter temperature in Celsius: ")

try:
    celsius = float(temp)

    print("Choose conversion type:")
    print("1. Fahrenheit")
    print("2. Kelvin")
    choice = input("Enter 1 or 2: ")

    if choice == "1":
        fahrenheit = (celsius * 9/5) + 32
        print(f"{celsius}°C is equal to {fahrenheit}°F.")
    elif choice == "2":
        kelvin = celsius + 273.15
        print(f"{celsius}°C is equal to {kelvin} K.")
    else:
        print("Invalid choice. Please enter 1 or 2.")
   
except ValueError:
    print("Please enter a valid number for temperature.")