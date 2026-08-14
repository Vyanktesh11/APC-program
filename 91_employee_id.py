emp_id=(111,112,113,114,115)
id=int(input("Enter Id:"))
for i in range(0,len(emp_id)):
    if emp_id[i]==id:
        print("Index="+str(i))
