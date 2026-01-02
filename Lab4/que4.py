'''4. Write a Python script that takes a list of six student names and uses the 
random.sample() function to randomly select exactly three "Volunteers" for a 
presentation, ensuring that no student is picked more than once in the selection. '''

import random

students = ["Manisha", "Reeja", "Shristi", "Nikhil", "Divya", "Samira"]
# students = ["Manisha", "Manisha", "Manisha", "Manisha", "Manisha", "Manisha"]
# students = ["Manisha", "Manisha"]
# random.seed(2)
volunteers = random.sample(students, 3)

print("Selected volunteers for the presentation:", volunteers)
