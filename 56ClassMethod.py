#|----------------------------------------------------------------|
#|Description    :    Class Method Program
#|----------------------------------------------------------------|
#|Author         :    ABHISHEK KUMAR, Computer Science Student
#|----------------------------------------------------------------|
#|Organization   :    NMAMIT, Nitte
#|----------------------------------------------------------------|
#|E-Mail         :    abhishekkumar8399@gmail.com
#|----------------------------------------------------------------|
class Empolyee:
    company="Apple"
    def show(self):
        print(f"The name is {self.name} and company is {self.company}")
    @classmethod        #change class Variable
    def changeCompany(cls,newcompany):
        cls.company = newcompany

e1=Empolyee()
e1.name="Carry"
e1.show()
e1.changeCompany("Tesla")
e1.show()
print(Empolyee.company)