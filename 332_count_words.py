import re

sentence = input("Enter a sentence: ")
print("Word count:", len(re.findall(r"\\b\\w+\\b", sentence)))
