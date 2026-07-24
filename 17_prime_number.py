num=int(input("Enter Number:"))
i=1
count=0
while i<=num:
    if num%i==0:
        count=count+1
    i=i+1
if count==2:
    print("prime number")
else:
    print("not prime number")
