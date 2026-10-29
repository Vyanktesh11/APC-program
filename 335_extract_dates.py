import re

text = input("Enter a paragraph: ")
print("Dates:", re.findall(r"\\b\\d{2}-\\d{2}-\\d{4}\\b", text))
