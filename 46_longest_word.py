s = input("Enter a sentence: ")

words = s.split()

longest = words[0]

for i in words:
    if len(i) > len(longest):
        longest = i

print(longest)