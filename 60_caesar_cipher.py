s = input("Enter text: ")
k = int(input("Enter shift: "))

r = ""

for i in s:
    if i.isalpha():
        if i.isupper():
            r += chr((ord(i) - 65 + k) % 26 + 65)
        else:
            r += chr((ord(i) - 97 + k) % 26 + 97)
    else:
        r += i

print(r)