s = input("Enter a string: ").replace(" ", "").lower() #handles spaces and ignores cases

if s == s[::-1]: #formula for palindrome
    print("The given string is a palindrome.")
else:
    print("The given string is NOT a palindrome.")
