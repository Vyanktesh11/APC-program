import re

text = input("Enter research paper references: ")
dois = re.findall(r"(?i)\\b10\\.\\d{4,9}/[-._;()/:A-Z0-9]+", text)
years = re.findall(r"\\b(?:19|20)\\d{2}\\b", text)
emails = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,}", text)
urls = re.findall(r"https?://[^\\s]+", text)
print("DOI identifiers:", dois)
print("Publication years:", years)
print("Email addresses:", emails)
print("URLs:", urls)
