'''Simple Path Validator 
Represent a small map as a dictionary like {"A": {"B", "C"}, "B": {"A", "D"}, "C": {"A", "D"}, "D": 
{"B", "C"}}. Ask the user to input a path, e.g., ["A", "C", "D"]. Check if each consecutive step is 
connected and print "Valid path" or "Invalid path".'''

dict = {
    "A": {"B", "C"},
    "B": {"A", "D"},
    "C": {"A", "D"},
    "D": {"B", "C"}
}

path = input("Enter path (separated by space): ").split()

valid = True

for i in range(len(path) - 1):
    current = path[i]
    nxt = path[i + 1]

    if nxt not in dict.get(current, {}):
        valid = False
        break

if valid:
    print("Valid path")
else:
    print("Invalid path")
