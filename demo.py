def is_palindrome(s):
    s = s.replace(" ", "").lower()
    
    return s == s[::-1]


word=input("Enter a word or phrase to check if it's palindrome: ")
if is_palindrome(word):
    print(f"'{word}' is a plindrome!")
else:
    print(f"'{word}' is not a palindrome.")
