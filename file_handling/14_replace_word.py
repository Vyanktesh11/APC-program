old_word = input("Word to replace: ")
new_word = input("Replacement word: ")

with open("student.txt", "r") as f:
    text = f.read()

text = text.replace(old_word, new_word)

with open("student.txt", "w") as f:
    f.write(text)

print("File updated.")
