#|----------------------------------------------------------------|
#|Description    :    Function Program
#|----------------------------------------------------------------|
#|Author         :    ABHISHEK KUMAR, Computer Science Student
#|----------------------------------------------------------------|
#|Organization   :    NMAMIT, Nitte
#|----------------------------------------------------------------|
#|E-Mail         :    abhishekkumar8399@gmail.com
#|----------------------------------------------------------------|
def calculatrGMean(a,b):
    GMean=(a*b)/(a+b)
    print(GMean)

def Greater(a,b):
    if a>b:
        print(a)
    elif a<b:
        print(b)
    else:
        print("Equal")
def lesser(a,b):
    pass   #pass means leave it for now

a=10
b=20
Greater(a,b)
calculatrGMean(a,b)
c=9
d=8
Greater(c,d)
calculatrGMean(c,d)