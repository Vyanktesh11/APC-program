n=int(input("Enter Number:"))
sum=1
fact=1
for i in range(1,n+1):
    fact=fact*i
    sum=sum+1/fact
print(sum)
    
