#|----------------------------------------------------------------|
#|Description    :    Operator Overloading Program
#|----------------------------------------------------------------|
#|Author         :    ABHISHEK KUMAR, Computer Science Student
#|----------------------------------------------------------------|
#|Organization   :    NMAMIT, Nitte
#|----------------------------------------------------------------|
#|E-Mail         :    abhishekkumar8399@gmail.com
#|----------------------------------------------------------------|
class Vector:
    def __init__(self,i,j,k):
        self.i = i
        self.j = j
        self.k = k

    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"
    def __add__(self,x):
        return Vector(self.i+x.i,self.j+x.j,self.k+x.k)

v=Vector(3,5,6) 
print(v)
v2=Vector(7,5,4) 
print(v2)

print(v+v2)
print(type(v+v2))