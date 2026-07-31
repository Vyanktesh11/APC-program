import math
n=int(input("Enter Number:"))
sqrt=int(math.sqrt(n))
count=0
for i in range(1,sqrt+1):
    if sqrt%i==0:
        count=count+1
        
if count==2:
    print("Prime Number")
else:
    print("Not prime Number")
        
