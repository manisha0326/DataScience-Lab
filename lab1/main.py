from age import calculate_year, leap_year
from bmi import (
    height_to_meters_feet,
    height_to_meters_cm,
    weight_to_kg_pounds,
    calculate_bmi,
    bmi_category
)

from army import is_army_eligible

age = int(input("Enter your age: "))
birth_year = calculate_year(age)

print(f"Your birth year is: ",birth_year)

if leap_year(birth_year):
    print("your birth year was leap year")
else:
    print("your birth year was not a lep year")



print("\nHeight Input Options:")
print("1. Feet/Inches")
print("2. Centimeters")
choice_h = input("Choose option (1/2): ")

if choice_h == "1":
    feet = int(input("Enter feet: "))
    inches = int(input("Enter inches: "))
    height_m = height_to_meters_feet(feet, inches)
elif choice_h == "2":
    cm = float(input("Enter height in cm: "))
    height_m = height_to_meters_cm(cm)
else:
    print("Invalid choice.")
    exit()

print("\nWeight Input Options:")
print("1. Kilograms")
print("2. Pounds")
choice_w = input("Choose option (1/2): ")

if choice_w == "1":
    weight_kg = float(input("Enter weight in kg: "))
elif choice_w == "2":
    pounds = float(input("Enter weight in pounds: "))
    weight_kg = weight_to_kg_pounds(pounds)
else:
    print("Invalid choice.")
    exit()

bmi = calculate_bmi(weight_kg, height_m)
category = bmi_category(bmi)

print(f"\nYour BMI is: {bmi:.2f}")
print(f"Category: {category}")


eligible = is_army_eligible(age, bmi)

if eligible:
    print("\nYou ARE eligible for army entrance.")
else:
    print("\nYou are NOT eligible for army entrance.")

