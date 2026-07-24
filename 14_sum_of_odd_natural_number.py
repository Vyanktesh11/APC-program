num=int(input("Enter range of natural number:"))
i=1
sum=0
while i<=num:
    if i%2!=0:
        sum=sum+i
    i+=1
print("sum of natural number:",sum)
