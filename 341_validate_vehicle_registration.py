import re

number = input("Enter a vehicle registration number (e.g. MH12AB1234): ").upper().replace(" ", "")
pattern = r"[A-Z]{2}\\d{2}[A-Z]{1,2}\\d{4}"
print("Valid format" if re.fullmatch(pattern, number) else "Invalid format")
