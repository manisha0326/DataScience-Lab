'''2. Use a list comprehension to create a new list containing only the even numbers between 
1 and 20, demonstrating a more concise and readable alternative to traditional loops.'''

even_numbers = [i for i in range(1, 21) if i % 2 == 0]
print("Even numbers between 1 and 20:", even_numbers)



# Traditional loop
# even = []
# for i in range(1, 11):
#     if i % 2 == 0:
#         even.append(i)

# # List comprehension
# even = [i for i in range(1, 11) if i % 2 == 0]

# print(even)

