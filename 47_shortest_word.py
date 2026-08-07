s = input("Enter a sentence: ")

words = s.split()

shortest = words[0]

for i in words:
    if len(i) < len(shortest):
        shortest = i

print(shortest)