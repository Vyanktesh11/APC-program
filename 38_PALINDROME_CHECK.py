s = input("Enter a string: ")

r = ""
for i in s:
    r = i + r

if s == r:
    print("Palindrome")
else:
    print("Not Palindrome")