''' Student Marks Manager 
Store student names as keys and marks (list of integers) as values in a dictionary. Compute 
each student’s average and grade (A/B/C/D). Print the top 2 students based on average marks. '''

students = {}
n = int(input("Enter number of students: "))

for i in range(n):
    name = input("\nEnter student name: ")
    marks = []

    sub = int(input("How many subjects? "))
    for j in range(sub):
        mark = int(input("Enter mark: "))
        marks.append(mark)

    students[name] = marks

averages = {}

for name, marks in students.items():
    total = 0
    for x in marks:
        total = total + x

    avg = total / len(marks)
    averages[name] = avg

    if avg >= 80:
        grade = "A"
    elif avg >= 60:
        grade = "B"
    elif avg >= 40:
        grade = "C"
    else:
        grade = "D"

    print("\n", name)
    print("Marks:", marks)
    print("Average:", avg)
    print("Grade:", grade)

first = ""
second = ""
first_avg = 0
second_avg = 0

for name, avg in averages.items():
    if avg > first_avg:
        second_avg = first_avg
        second = first
        first_avg = avg
        first = name
    elif avg > second_avg:
        second_avg = avg
        second = name

print("\nTop 2 Students:")
print("1.", first, "-", first_avg)
print("2.", second, "-", second_avg)