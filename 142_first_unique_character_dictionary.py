s = input("Enter a string: ")

count = {}

for ch in s:
    count[ch] = count.get(ch, 0) + 1

for ch in s:
    if count[ch] == 1:
        print("First character occurring only once:", ch)
        break
else:
    print("No unique character")
