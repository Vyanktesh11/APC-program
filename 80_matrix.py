a = []
b = []
c = []

print("Enter first matrix")
for i in range(3):
    row = list(map(int, input().split()))
    a.append(row)

print("Enter second matrix")
for i in range(3):
    row = list(map(int, input().split()))
    b.append(row)

for i in range(3):
    row = []
    for j in range(3):
        row.append(a[i][j] + b[i][j])
    c.append(row)

print("Result")
for i in c:
    print(i)