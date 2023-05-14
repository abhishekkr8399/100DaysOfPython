#|----------------------------------------------------------------|
#|Description    :    IF-ELSE Program
#|----------------------------------------------------------------|
#|Author         :    ABHISHEK KUMAR, Computer Science Student
#|----------------------------------------------------------------|
#|Organization   :    NMAMIT, Nitte
#|----------------------------------------------------------------|
#|E-Mail         :    abhishekkumar8399@gmail.com
#|----------------------------------------------------------------|
num=int(input("Please Enter a number:"))
print("Number: ",num)
if num>0:
    print("Positive")
    if num>100:
        print("Greater than 100")
    else:
        print("Smaller than 100")
elif num<0:
    print("Negative")
    if num<-100:
        print("Smaller than -100")
    else:
        print("Greater than -100")
else:
    print("Zero")