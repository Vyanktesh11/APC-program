e = input("Enter email: ")

if "@" in e and "." in e and e.index("@") < e.rindex("."):
    print("Valid Email")
else:
    print("Invalid Email")