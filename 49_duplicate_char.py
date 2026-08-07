s = input("Enter a string: ")

seen = ""

for i in s:
    if i not in seen:
        c = 0
        for j in s:
            if i == j:
                c += 1
        if c > 1:
            print(i)
        seen += i