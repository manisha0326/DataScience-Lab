'''
2. File Processing with Exception Handling 
● Reads numbers from a text file (one number per line) 
● Ignores invalid entries using exception handling 
● Calculates and displays the sum and average of valid numbers 
'''

t = 0
c = 0
try:

    file = open("numbers.txt","r")
    for line in file:
        try:
            num = float(line)
            t += num
            c += 1
        except ValueError:
            continue

    file.close()

    if c > 0:
        avg = t/c
        print("Sum : ", t)
        print("Average: ", avg)
    else:
        print("NO valid numbers found.")

except FileNotFoundError:
    print("File not found.")


# total = 0
# count = 0

# try:
#     file = open("numbers.txt", "r")

#     for line in file:
#         try:
#             num = float(line) 
#             total += num
#             count += 1
#         except ValueError:
#             continue

#     file.close()

#     if count > 0:
#         avg = total / count
#         print("Sum =", total)
#         print("Average =", avg)
#     else:
#         print("No valid numbers found.")

# except FileNotFoundError:
#     print("File not found!")
