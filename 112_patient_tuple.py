t1=(
    (121,"batman",52,"B-"),
    (122,"naruto",20,"A"),
    (123,"Goku",50,"A+"),
    (124,"Vegeta",47,"A+")
   )
for i in t1:
    print(i)
    
id=int(input("Enter patient Id:"))
for i in t1:
    if i[0]==id:
        print("Id Found....")
        break
else:
    print("Not Found....")
print("Total Number of patient:",end="")
count=0
for i in t1:
    count+=1
print(count)
print("Blood Group:",end="")
for i in t1:
    print(i[0],i[3],end=" ")
