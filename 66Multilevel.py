#|----------------------------------------------------------------|
#|Description    :    Multilevel Inhritance Program
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
    def show(self):
        print(f"Name: {self.name}species: {self.species}")

class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self,name, species="Dog")
        self.breed = breed
    def show(self):
        Animal.show(self)
        print(f"Breed: {self.breed}")

class DB(Dog):
    def __init__(self, name,color):
        Dog.__init__(self,name,breed="Doberman")
        self.color = color
    def show(self):
        Dog.show(self)
        print(f"Color: {self.color}")

o=DB("tommy","Black")
o.show()