numbers = [10, 20, 10, 30, 20, 10, 40, 30]

d = {}

for num in numbers:
    d[num] = d.get(num, 0) + 1

print(d)
