#|----------------------------------------------------------------|
#|Description    :    OOPs Program
#|----------------------------------------------------------------|
#|Author         :    ABHISHEK KUMAR, Computer Science Student
#|----------------------------------------------------------------|
#|Organization   :    NMAMIT, Nitte
#|----------------------------------------------------------------|
#|E-Mail         :    abhishekkumar8399@gmail.com
#|----------------------------------------------------------------|
class Person:
    def __init__(self,name,occupation):
        print("Hey I am a Person")
        self.name=name
        self.occupation=occupation
    def info(self):
        print(f"{self.name} is a {self.occupation}")

a=Person("Abhi","Developer")
b=Person("Divya","HR")
a.info()
b.info()
# a.name="Mahesh"
# a.occupation="Accountant"
# #print(a.name,a.occupation)
# b.name="Nathu"
# b.occupation="HR"