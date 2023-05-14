#|----------------------------------------------------------------|
#|Description    :    Class Methods As Constructors Program
#|----------------------------------------------------------------|
#|Author         :    ABHISHEK KUMAR, Computer Science Student
#|----------------------------------------------------------------|
#|Organization   :    NMAMIT, Nitte
#|----------------------------------------------------------------|
#|E-Mail         :    abhishekkumar8399@gmail.com
#|----------------------------------------------------------------|
class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    @classmethod
    def fromStr(cls,string):
        return cls(string.split("-")[0],int(string.split("-")[1]))

string="Larry-12000"
e=Employee.fromStr(string)
print(e.name)
print(e.salary)