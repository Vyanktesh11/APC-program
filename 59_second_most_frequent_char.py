s = input("Enter a string: ")

f = {}

for i in s:
    f[i] = f.get(i, 0) + 1

a = sorted(f.items(), key=lambda x: x[1], reverse=True)

if len(a) > 1:
    print(a[1][0])
else:
    print("Not Found")