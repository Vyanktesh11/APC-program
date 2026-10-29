import re

password = input("Enter a password: ")
pattern = r"(?=.*[A-Z])(?=.*[a-z])(?=.*\\d)(?=.*[^A-Za-z0-9]).{8,}"
print("Strong password" if re.fullmatch(pattern, password) else "Password does not meet requirements")
