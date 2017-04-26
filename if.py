print("write your age ")
age=input()
print ("your age is "+age+ " yrs old")
if int(age) == 18 :
    print("you are adult now")
elif int(age) <= 13 and int(age) >= 17 :
    print("you are a teenager")

elif int(age) > 12 :
    print("you r still a kid bro")
else :
    print("end")
