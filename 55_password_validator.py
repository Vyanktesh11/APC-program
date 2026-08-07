p = input("Enter password: ")

u = l = d = s = 0

for i in p:
    if i.isupper():
        u = 1
    elif i.islower():
        l = 1
    elif i.isdigit():
        d = 1
    else:
        s = 1

if len(p) >= 8 and u and l and d and s:
    print("Valid Password")
else:
    print("Invalid Password")