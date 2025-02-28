import re

s = input("Enter a string: ")
cleaned = re.sub(r'[^a-zA-Z0-9]', '', s).lower() # removes everything that is not a letter or number and makes them lowercase

if cleaned == cleaned[::-1]:  # checking if a string is palindrome
    print("The given string is a palindrome.")
else:
    print("The given string is NOT a palindrome.")