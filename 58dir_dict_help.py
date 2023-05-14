#|----------------------------------------------------------------|
#|Description    :    dir() _dict_ help() Program
#|----------------------------------------------------------------|
#|Author         :    ABHISHEK KUMAR, Computer Science Student
#|----------------------------------------------------------------|
#|Organization   :    NMAMIT, Nitte
#|----------------------------------------------------------------|
#|E-Mail         :    abhishekkumar8399@gmail.com
#|----------------------------------------------------------------|
x=[1,2,3]
print(dir(x))
print(x.__add__)

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

p=Person("John",30)
print(p.__dict__) 


print(help(Person))