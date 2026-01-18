''' Unique Words Collector 
Take a paragraph input from the user. Split it into words, remove duplicates, sort them 
alphabetically, and count the total number of unique words.'''

paragraph = input("Enter paragraph: ")
words = paragraph.split()

freq = {}
for w in words:
    if w in freq:
        freq[w] += 1
    else:
        freq[w] = 1

unique_words = list(freq.keys())

for i in range(len(unique_words)):
    for j in range(i + 1, len(unique_words)):
        if unique_words[i].lower() > unique_words[j].lower():
            
            unique_words[i], unique_words[j] = unique_words[j], unique_words[i]

print("\nUnique words:", unique_words)
print("Total unique words:", len(unique_words))
print("Word frequency:", freq)





# paragraph = input("Enter paragraph: ")
# words = paragraph.split()

# freq = {}
# for w in words:
#     if w in freq:
#         freq[w] += 1
#     else:
#         freq[w] = 1

# unique_words = list(freq.keys())

# for i in range(len(unique_words)):
#     for j in range(i + 1, len(unique_words)):
#         if unique_words[i].lower() > unique_words[j].lower():
            
#             unique_words[i], unique_words[j] = unique_words[j], unique_words[i]

# print("\nUnique words:", unique_words)
# print("Total unique words:", len(unique_words))
# print("Word frequency:", freq)





# paragraph = input("Enter paragraph: ")

# words = paragraph.split()

# word_freq = {}
# for w in words:
#     if w in word_freq:
#         word_freq[w] += 1
#     else:
#         word_freq[w] = 1

# # unique_words = sorted(word_freq.keys())
# unique_words = sorted(words)


# print("\nUnique words:", unique_words)
# print("Total unique words:", len(unique_words))
# print("Word frequency:", word_freq)
