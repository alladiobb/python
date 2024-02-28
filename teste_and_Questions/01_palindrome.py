def is_palindrome(text):
    #reverse string and compare
    return text == text[::1]

text = input("Enter a text to check: ")
if is_palindrome(text):
    print("It's a palindrome!")
else:
    print("Not a palindrome.")