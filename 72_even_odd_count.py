num=[1,2,3,4,5,6,7,8,9]
counts=0
counto=0
for i in range(0,len(num)):
    if num[i]%2==0:
        counts+=1
    else:
        counto+=1
print("even=",counts)
print("odd=",counto)