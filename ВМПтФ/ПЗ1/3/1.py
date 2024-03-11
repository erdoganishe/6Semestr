import datetime

s = input("Insert your year")

age = datetime.datetime.now().year - int(s)

print("Your age is " + str(age-1) + " or " + str(age) + " years")