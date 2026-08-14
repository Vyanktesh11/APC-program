t=(10,20,30,30,20)
print(t)
for i in range(0,len(t)):
    count=0
    for j in range(0,len(t)):
        if t[i]==t[j]:
            count+=1
    print(f"count of {t[i]} = {count}")

        
    
