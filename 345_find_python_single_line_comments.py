import re

source = input("Enter Python source code on one line: ")
comments = re.findall(r"(?m)(?<!\\S)#.*$", source)
print("Single-line comments:", comments)
print("Note: Regex alone cannot reliably distinguish # inside quoted strings or handle every multiline/string-literal case.")
