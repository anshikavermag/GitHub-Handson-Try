y=int(input("enter year: "))
if (y%4==0):
    if y%400==0:
        print("leap")
    
    elif y%100==0:
        print("no leap")
    
#better and complete code

x=int(input("enter year: "))
if x%4==0:
    if x%100==0:
        if x%400==0:
            print("a leap year")
        else:
            print("not a leap year")
    else:
        print("not a leap year")
else:print("not a leap year")
