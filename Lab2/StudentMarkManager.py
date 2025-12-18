# Function to calculate grade based on average
def get_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 75:
        return "B"
    elif avg >= 60:
        return "C"
    else:
        return "D"


# Dictionary to store students and their marks
students = {}

# Input format: Ram-80-85-90,Sita-95-92-94,Hari-70-65-75
user_input = input("Enter students and marks (comma-separated, e.g., Ram-80-85-90,Sita-95-92-94): ")

entries = user_input.split(",")  # split students

for entry in entries:
    parts = entry.split("-")
    if len(parts) < 2:
        print(f"Ignored invalid entry: {entry}")
        continue

    name = parts[0]
    marks = []

    for m in parts[1:]:
        if m.isdigit():
            marks.append(int(m))
        else:
            print(f"Ignored invalid mark: {m} for student {name}")

    if marks:
        students[name] = marks
    else:
        print(f"No valid marks for student {name}!")

# ---- Processing ----
results = []

for name, marks in students.items():
    avg = sum(marks) / len(marks)
    grade = get_grade(avg)
    results.append((name, avg, grade))

# Sort students by average marks (descending)
results.sort(key=lambda x: x[1], reverse=True)

# ---- Output ----
print("\n--- Student Results ---")
for name, avg, grade in results:
    print(f"{name}: Average = {avg:.2f}, Grade = {grade}")

# Print top 2 students
print("\nTop 2 Students:")
for r in results[:2]:
    print(f"{r[0]} (Average: {r[1]:.2f})")
