def total(m1,m2,m3):
    Total=m1+m2+m3
    return Total
def percentage(total,all):
    p=(total/all)*100
    return p
def grade(p):
    if p>75 and p<80:
        print("B")
    elif p>80 and p<95:
        print("A")
    elif p>95:
        print("A+")
    else:
        print("C")