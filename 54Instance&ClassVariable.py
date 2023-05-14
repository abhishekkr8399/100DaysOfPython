#|----------------------------------------------------------------|
#|Description    :    Instance V/S class Variable Program
#|----------------------------------------------------------------|
#|Author         :    ABHISHEK KUMAR, Computer Science Student
#|----------------------------------------------------------------|
#|Organization   :    NMAMIT, Nitte
#|----------------------------------------------------------------|
#|E-Mail         :    abhishekkumar8399@gmail.com
#|----------------------------------------------------------------|
#Instance Variable has more priority than Class variables 
class Emp:
    comp="Apple Computer"#class Variable
    noOfEmployees=0
    def __init__(self,name):
        self.name = name   #instance Variable
        self.raise_amount=0.02  #instance Variable
        Emp.noOfEmployees+=1
    def showDetails(self):
        print(f"The name of Employee is {self.name} and the raise amount in {self.noOfEmployees} sized {self.comp} is {self.raise_amount}")
emp1=Emp("Abhishek")
emp1.raise_amount=0.5
emp1.comp="Apple India"
emp1.showDetails()
# Emp.showDetails(emp1)
emp1=Emp("Kumar")
emp1.showDetails()
Emp.comp="Google"
print(Emp.comp)