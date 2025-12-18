# 2. Write a program that checks if a given string is palindrome. 

text = input("Enter a string: ")

clean_text = text.replace(" ", "").lower()

is_palindrome = True

for i in range(len(clean_text) // 2):
    if clean_text[i] != clean_text[-(i + 1)]:
        is_palindrome = False
        break 
if is_palindrome:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")



# text = input("Enter a string: ")
# if text == text[::-1]:
#     print("palindrome")
# else:
#     print("not palindrome")