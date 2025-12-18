''' Word Reverser Game 
Ask the user for a list of words. Reverse each word only if its length is even. Print the new list of 
words after processing.'''

words = input("Enter words separated by space: ").split()

new_list = []

for w in words:
    if len(w) % 2 == 0:
        new_list.append(w[::-1])
    else:
        new_list.append(w)

print("Processed words:", new_list)
