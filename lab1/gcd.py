def GCD(a, b):
    while b != 0:

        temp = a
        a = b
        b = temp%b
    return a

n1 = input("Enter first number: ")
n2 = input("Enter second number: ")

if n1.isdigit() and n2.isdigit():
    num1 = int(n1)
    num2 = int(n2)

    result = GCD(num1, num2)
    print(f"The GCD of {num1} and {num2} is {result}.")

else:
    print("Please enter valid positive integers.")