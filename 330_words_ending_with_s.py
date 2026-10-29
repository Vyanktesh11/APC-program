import re

text = input("Enter a sentence: ")
print("Words ending with s:", re.findall(r"\\b\\w+s\\b", text, re.IGNORECASE))
