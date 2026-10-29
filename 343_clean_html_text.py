import re
import html

text = input("Enter HTML/text: ")
text = re.sub(r"<[^>]+>", " ", text)
text = html.unescape(text)
text = re.sub(r"[^\\w\\s.,!?'-]", "", text)
text = re.sub(r"\\s+", " ", text).strip()
print(text)
