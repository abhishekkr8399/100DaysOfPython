#|----------------------------------------------------------------|
#|Description    :    Super Keyword Program
#|----------------------------------------------------------------|
#|Author         :    ABHISHEK KUMAR, Computer Science Student
#|----------------------------------------------------------------|
#|Organization   :    NMAMIT, Nitte
#|----------------------------------------------------------------|
#|E-Mail         :    abhishekkumar8399@gmail.com
#|----------------------------------------------------------------|

# class Parent:
#     def parent_method(self):
#         print("This is Parent method.")
# class child(Parent):
#     def child_method(self):
#         print("This is Child method.")
#         super().parent_method()
# child_obj=child()
# child_obj.child_method()

class Employee:
    def __init__(self,name,id):
        self.name = name
        self.id = id

class Programmer(Employee):
    def __init__(self,name,id,lang):
        super().__init__(name,id)
        self.lang = lang

ep1=Employee("Rohan",420)
ep2=Programmer("Sohan",454,"Python")
print(ep1.id)
print(ep2.lang)
