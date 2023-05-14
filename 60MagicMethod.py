#|----------------------------------------------------------------|
#|Description    :    Magic Method Program
#|----------------------------------------------------------------|
#|Author         :    ABHISHEK KUMAR, Computer Science Student
#|----------------------------------------------------------------|
#|Organization   :    NMAMIT, Nitte
#|----------------------------------------------------------------|
#|E-Mail         :    abhishekkumar8399@gmail.com
#|----------------------------------------------------------------|
class Emp:
    def __init__(self,name):
        self.name = name

    def __len__(self):
        i=0
        for c in self.name:
            i+=1
        return i
    
    def __str__(self):
        return(f"The name of Employee is {self.name} str")
    def __repr__(self):
        return(f"The name of Employee is {self.name} repr")
    def __call__(self):
        print("Hello")
    
e=Emp("Larry")
print(str(e))
print(repr(e))
# print(e.name)
# print(len(e))
e()