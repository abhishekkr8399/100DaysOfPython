#|----------------------------------------------------------------|
#|Description    :    Multiple Inhritance Program
#|----------------------------------------------------------------|
#|Author         :    ABHISHEK KUMAR, Computer Science Student
#|----------------------------------------------------------------|
#|Organization   :    NMAMIT, Nitte
#|----------------------------------------------------------------|
#|E-Mail         :    abhishekkumar8399@gmail.com
#|----------------------------------------------------------------|
#one child many parent
class Employee:
    def __init__(self,name):
        self.name = name
    def show(self):
        print(f"The name is {self.name}")

class Dancer:
    def __init__(self,dance):
        self.dance = dance
    def show(self):
        print(f"The dance is {self.dande}")    
    
class ED(Employee,Dancer):
    def __init__(self,dance,name):
        self.dance = dance
        self.name = name


o=ED("Kathak","raju")
print(o.name)
print(o.dance)
print(o.show())
print(ED.mro())