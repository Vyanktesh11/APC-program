s = input("Enter a sentence: ")
w = input("Enter word: ")

words = s.split()

count = 0

for i in words:
    if i == w:
        count += 1

print("Occurrences:", count)