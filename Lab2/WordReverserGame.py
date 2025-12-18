
words = input("Enter words separated by space: ").split()

new_list = []

for w in words:
    if len(w) % 2 == 0:   # even length
        new_list.append(w[::-1])
    else:
        new_list.append(w)

print("Processed words:", new_list)
