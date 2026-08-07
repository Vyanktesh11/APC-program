s = input("Enter a string: ")

m = ""
mc = 0

for i in s:
    c = 0
    for j in s:
        if i == j:
            c += 1
    if c > mc:
        mc = c
        m = i

print(m)