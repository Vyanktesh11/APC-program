marry=input("Enter Your married or unmarried:").lower()
age=int(input("Enter Age:"))
gender=input("Enter your gender:").lower()
if marry=="married":
    print("driver is insured")

elif gender=="male" and age>30:
        print("driver is insured")
elif gender=="female" and age>25:
        print("driver is insured")
else:
    print("driver is not insured")
