#|----------------------------------------------------------------|
#|Description    :    Hybrid and Hierarchical Inhritance Program
#|----------------------------------------------------------------|
#|Author         :    ABHISHEK KUMAR, Computer Science Student
#|----------------------------------------------------------------|
#|Organization   :    NMAMIT, Nitte
#|----------------------------------------------------------------|
#|E-Mail         :    abhishekkumar8399@gmail.com
#|----------------------------------------------------------------|
class BaseClass:
    pass

class Derived1(BaseClass):
    pass

class Derived2(BaseClass):
    pass

class Derived3(Derived1,Derived2):
    pass

#Hierarchical Inhritance

class Base:
    pass

class D1(Base):
    pass

class D2(Base):
    pass

class D3(D1):
    pass