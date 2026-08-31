def is_palindrome(value):
    value = str(value)
    return value == value[::-1]

value = input("Enter a string or number: ")

if is_palindrome(value):
    print("Palindrome")
else:
    print("Not a palindrome")
