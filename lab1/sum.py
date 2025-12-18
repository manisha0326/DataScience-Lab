# 1. Write a program that takes two numbers as input from the user, and print their sum. 

try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter another number: "))

    sum = num1 + num2

    if sum.is_integer():
        print(int(sum))
    else:
        print(sum)

except TypeError:
    print("please enter only numbers.")



# without try except
# num1 = input("Enter first number: ")
# num2 = input("Enter another number: ")

# if (num1.replace('.', '', 1).replace('-', '', 1).isdigit() and
# num2.replace('.', '', 1).replace('-', '', 1).isdigit()):

#     num1 = float(num1)
#     num2 = float(num2)

#     sum = num1 + num2
#     if sum.is_integer():
#         print(int(sum))
#     else:
#         print(sum)

# else:
#     print("Please enter only numbers.")