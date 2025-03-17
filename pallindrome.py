import string

def is_palindrome(s):
    # Remove spaces, punctuation, and convert to lowercase
    s = ''.join(e for e in s if e.isalnum()).lower()
    return s == s[::-1]

input_string = input("Enter a string to check if it's a palindrome: ")
if is_palindrome(input_string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
