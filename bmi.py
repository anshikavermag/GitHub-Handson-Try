h=float(input("enter height in m: "))
w=int(input("enter weight in kg: "))
bmi=w/h**2
if bmi<18.5:
    print("underweight")
elif bmi<25 and bmi>18.5:
    print("normal")
elif bmi<30 and bmi>25:
    print("overweight")
elif bmi>30 and bmi<35:
    print("obese")
elif bmi>35:
    print("clinically obese")



