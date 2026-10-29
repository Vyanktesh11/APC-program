import re

sentence = input("Enter a sentence: ")
print("Words beginning with A or a:", re.findall(r"\\b[Aa]\\w*\\b", sentence))
