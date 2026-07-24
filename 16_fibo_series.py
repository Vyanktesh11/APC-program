n=int(input("Enter Number upto you want fibo:"))
n1=-1
n2=1
sum=0
i=0
while sum<=n: 
    sum=n1+n2
    print(sum)
    n1=n2
    n2=sum
    
