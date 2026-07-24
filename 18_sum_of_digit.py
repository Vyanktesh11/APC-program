num=int(input("Enter Number:"))
sum=0
val=num
while num>0:
    temp=num%10
    sum=sum+temp
    num=num//10
print("sum of digit:",sum)
    
    
