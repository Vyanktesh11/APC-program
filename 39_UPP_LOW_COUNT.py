s = input("Enter a string: ")

u = l = 0

for i in s:
    if i.isupper():
        u += 1
    elif i.islower():
        l += 1

print("Uppercase:", u)
print("Lowercase:", l)