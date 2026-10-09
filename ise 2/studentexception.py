class studentexception(Exception):
    pass
try:
    marks=int(input("Enter marks:"))
    if marks<0 or marks>100:
        raise studentexception("marks is out of bound (1-100)")
    else:
        print("marks are valid")
except studentexception as e:
    print(e)