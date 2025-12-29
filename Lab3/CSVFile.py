'''
3. CSV File Handling 
● Read data from a CSV file containing student records (roll number, name, marks) 
● Display all student records 
● Handle file-related and data conversion errors using try-except
'''

import csv

try:
    with open("students.csv", "r") as file:
        reader = csv.reader(file)
        header = next(reader) 

        print("Roll\tName\tMarks")
    
        for row in reader:
            try:
                roll = int(row[0])
                name = row[1]
                marks = int(row[2])

                print(f"{roll}\t{name}\t{marks}")

            except ValueError:
                print("Invalid data found, skipped:", row)

except FileNotFoundError:
    print("CSV file not found!")
except Exception as e:
    print("Error:", e)
