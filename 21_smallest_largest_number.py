n=int(input("Enter Number of elements you want:"))
i=0
list=[]
print("Enter Elements:")
for i in range(0,n):
    value=int(input())
    list.append(value)
min=list[0]
max=list[0]
for i in range(0,n):
    if list[i]<min:
        min=list[i]
    elif list[i]>max:
        max=list[i]
    else:
        pass
print("min:",min)
print("max:",max)
