s = input("Enter a sentence: ")

count = 1

for i in s:
    if i == " ":
        count += 1

print("Word Count:", count)