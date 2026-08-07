list=[10,20,30,44,3,67]
min=list[0]
max=list[0]
for i in range(0,len(list)):
    if list[i]<min:
        min=list[i]
    elif list[i]>max:
        max=list[i]
    else:
        pass
print(min)
print(max)
