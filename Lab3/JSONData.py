'''
4. Writing and Reading JSON Data 
● Stores student details (ID, name, and marks) in a JSON file 
● Reads the JSON file and displays the student information 
● Handles exceptions related to file access and JSON decoding
'''

import json

students = [
    {"id": 1, "name": "Ram", "marks": 85},
    {"id": 2, "name": "Sita", "marks": 92},
    {"id": 3, "name": "John", "marks": 78}
]

try:
    with open("students.json", "w") as file:
        json.dump(students, file)
        print("Data written to JSON file successfully.")
except IOError:
    print("Error writing to file!")

try:
    with open("students.json", "r") as file:
        data = json.load(file)

        print("\nStudent Information:")
        for s in data:
            print(f"ID: {s['id']}, Name: {s['name']}, Marks: {s['marks']}")

except FileNotFoundError:
    print("JSON file not found!")
except json.JSONDecodeError:
    print("Error decoding JSON data!")
except Exception as e:
    print("Error:", e)
