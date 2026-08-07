num=list(map(int,input("Enter numbers:").split()))
sum=0
for i in range(0,len(num)):
    sum=sum+num[i]
print(sum)
average=sum/len(num)
print(average)