s = input("Enter a string: ")
a = input("Enter character to replace: ")
b = input("Enter new character: ")

r = ""

for i in s:
    if i == a:
        r += b
    else:
        r += i

print(r)