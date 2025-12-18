# 4. Write a python program that prints the Fibonacci series up to n terms. 

num = input("Enter the number of terms: ")

if num.isdigit():
    n = int(num)

    a = 0
    b = 1

    print(f"Fibonacci series up to {num} terms:")

    for i in range(n):
        print(a, end=" ")
        temp = a
        a = b
        b = temp + b

else:
    print("Please enter a valid positive integer.")