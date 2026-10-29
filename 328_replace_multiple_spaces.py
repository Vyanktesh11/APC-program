import re

text = input("Enter a string: ")
print(re.sub(r" {2,}", " ", text))
