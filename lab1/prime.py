n = input("Enter a number upto which print prime number: ")
if n.isdigit():
    num = int(n)
    for number in range(2, num+1):
        is_prime = True

        for i in range(2, number):
            if number % i == 0:
                is_prime = False
                break

        if is_prime:
            print(number, end="\n")

else:
    print("Enter a valid positive number: ")