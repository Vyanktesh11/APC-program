year=int(input("Enter Year:"))
if year%4==0 and year%400==0:
    print("leaf year")
else:
    print("not a leaf year")
