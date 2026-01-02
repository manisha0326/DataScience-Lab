'''Given a list of student names and a list of their corresponding scores, use the zip() 
function to pair them together and then apply the reduce() function from the 
functools module to calculate the total sum of all scores.'''

from functools import reduce

students = ["Nikhil", "Bikram", "Divya", "Samira"]

scores = [85, 90, 78, 92]

student_scores = list(zip(students, scores))
print("Student scores:", student_scores)

total_score = reduce(lambda acc, pair: acc + pair[1], student_scores, 0)

print("Total sum of scores:", total_score)

