numbers = input("Enter numbers separated by spaces: ").split()

list = []

for n in numbers:
    list.append(float(n))

if list:
    largest = list[0]
    for num in list:
        if num > largest:
            largest = num
        
    if largest.is_integer():
        print("The largest number is: ", int(largest))
    else:
        print("The largest number is: ", largest)

else:
    print("No valid numbers entered.")

