import re

text = input("Enter filenames or text: ")
print("File extensions:", re.findall(r"\\.([A-Za-z0-9]+)\\b", text))
