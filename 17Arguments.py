#|----------------------------------------------------------------|
#|Description    :    Arguments Program
#|----------------------------------------------------------------|
#|Author         :    ABHISHEK KUMAR, Computer Science Student
#|----------------------------------------------------------------|
#|Organization   :    NMAMIT, Nitte
#|----------------------------------------------------------------|
#|E-Mail         :    abhishekkumar8399@gmail.com
#|----------------------------------------------------------------|
#Default,Keyword,Variable,Required
def average(a,b=2,c=3,d=4,e=5):
    print((a+b+c+d+e)/5)

average(3)
average(2)
average(2,3)
average(2,3,4)
average(2,3,4,5)
average(2,3,4,5,6)

#Keyword
average(e=100,a=99)

#Required
average(99)

def avg(*num):
    print(type(num))
    sum=0
    for i in num:
        sum=sum+i
    print(sum/len(num))

avg(57,89)
avg(57,89,77,66,55,44,)

def name(**name):
    print(type(name))
    return("Hello,",name["fname"],name["mname"],name["lname"])

print(name(mname="Raja",lname="Ram",fname="Raghupati"))