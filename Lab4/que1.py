'''1. Write a Python script that takes a list of student marks and sorts them in descending 
order (highest to lowest) using either the sorted() function or the .sort() method. '''


marks = [65, 78, 90, 56, 88, 72]
marks.sort(reverse=True)
print("Sorted marks (highest to lowest):", marks)





# Using sorted()
# marks = [65, 78, 90, 56, 88, 72]

# sorted_marks = sorted(marks, reverse=True)
# print("Sorted marks (highest to lowest):", sorted_marks)


'''Taking User Input'''
# Take number of students
# n = int(input("Enter number of students: "))

# marks = []

# # Take marks input
# for i in range(n):
#     m = int(input(f"Enter marks of student {i+1}: "))
#     marks.append(m)

# # Sort marks in descending order
# marks.sort(reverse=True)

# # Display result
# print("Sorted marks (highest to lowest):", marks)


# Using sorted()
# n = int(input("Enter number of students: "))
# marks = []

# for i in range(n):
#     marks.append(int(input(f"Enter marks of student {i+1}: ")))

# sorted_marks = sorted(marks, reverse=True)
# print("Sorted marks (highest to lowest):", sorted_marks)

