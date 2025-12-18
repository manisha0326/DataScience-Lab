# Map representation
graph = {
    "A": {"B", "C"},
    "B": {"A", "D"},
    "C": {"A", "D"},
    "D": {"B", "C"}
}

# User input (example: A C D)
path = input("Enter path (separated by space): ").split()

valid = True

# Check consecutive connections
for i in range(len(path) - 1):
    current = path[i]
    nxt = path[i + 1]

    # Check if next node exists in the connection set
    if nxt not in graph.get(current, {}):
        valid = False
        break

# Output result
if valid:
    print("Valid path")
else:
    print("Invalid path")
