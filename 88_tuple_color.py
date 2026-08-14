t=("Red","Black","White","Blue","Pink")
v=input("Enter color:").capitalize()
count=0
for i in t:
    if i==v:
        print("Found")
        count=1
if count==0:
    print("not found")
    
