import random
a=input("enter names")
al=a.split(",")
x=len(al)
y=random.randint(0,x-1)
print(al[y],"is going to pay the bill")
