#|----------------------------------------------------------------|
#|Description    :    Inheritance Program
#|----------------------------------------------------------------|
#|Author         :    ABHISHEK KUMAR, Computer Science Student
#|----------------------------------------------------------------|
#|Organization   :    NMAMIT, Nitte
#|----------------------------------------------------------------|
#|E-Mail         :    abhishekkumar8399@gmail.com
#|----------------------------------------------------------------|
class Employee:
    def __init__(self,name,id):
        self.name = name
        self.id = id

    def show(self):
        print(f"The name of employee: {self.id} is {self.name}")

class Programmer(Employee):
    def showLang(self):
        print("Python")

e=Employee("Rohan Das",400)
e.show()
e1=Programmer("Ramesh Das",4010)
e1.show()
e1.showLang()
