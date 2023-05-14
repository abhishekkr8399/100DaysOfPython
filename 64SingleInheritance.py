#|----------------------------------------------------------------|
#|Description    :    Single Inhritance Program
#|----------------------------------------------------------------|
#|Author         :    ABHISHEK KUMAR, Computer Science Student
#|----------------------------------------------------------------|
#|Organization   :    NMAMIT, Nitte
#|----------------------------------------------------------------|
#|E-Mail         :    abhishekkumar8399@gmail.com
#|----------------------------------------------------------------|
class Animal:
    def __init__(self,name,species):
        self.name = name
        self.species = species

    def sound(self):
        print("sound")

class Dog(Animal):
    def __init__(self,name,breed):
        Animal.__init__(self,name,species="Dog")
        self.breed =breed

    def sound(self):
        print("Bark!")

d=Dog("Doggy","Doggerman")
d.sound()

a=Animal("Animal","Animal")
a.sound()