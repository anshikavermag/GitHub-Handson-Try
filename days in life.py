age=int(input("Enter your age: "))
week=90*52
month=90*12
day=90*365
wl=week-(age*52)
ml=month-(age*12)
dl=day-(age*365)
message=(f"you have {dl} days ,{wl} week ,{ml} months left")
print(message)