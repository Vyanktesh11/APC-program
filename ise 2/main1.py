import calculate as c
m1=int(input("enter your m1 marks: "))
m2=int(input("enter your m2 marks: "))
m3=int(input("enter your m3 marks: "))
all=90
total=c.total(m1,m2,m3)
print("total:",c.total(m1,m2,m3))
print("percentage:",c.percentage(total,all))
p=c.percentage(total,all)
print("grade",c.grade(p))