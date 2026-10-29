import re

text = input("Enter text (use \\n for a newline if needed): ")
text = text.replace(r"\\n", "\\n").replace(r"\\t", "\\t")
matches = re.findall(r"[ \\t\\n]", text)
print("Whitespace characters:", matches)
print("Count:", len(matches))
