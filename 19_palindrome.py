num=int(input("Enter Number:"))
val=num
sum=0
while num>0:
    temp=num%10
    sum=sum*10+temp   
    num=num//10
if sum==val:
    print("palindrome")
else:
    print("not palindrome")
