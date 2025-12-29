"""
1. Basic File Read & Write 
● Create a text file and write multiple lines into it 
● Read the contents of the file and display them on the screen 
● Handle the case where the file does not exist using try-except 
"""

try:
    file = open("two.txt","w")
    file.write("Hello World\n")
    file.write("Welcome to the world\n")
    file.write("My name is Manisha Mahato.")
    file.close()

    file = open("two.txt","r")
    print(file.read())
    file.close()
except ValueError:
    print("File not found")