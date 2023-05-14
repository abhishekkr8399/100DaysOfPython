#|----------------------------------------------------------------|
#|Description    :    Static Methods Program
#|----------------------------------------------------------------|
#|Author         :    ABHISHEK KUMAR, Computer Science Student
#|----------------------------------------------------------------|
#|Organization   :    NMAMIT, Nitte
#|----------------------------------------------------------------|
#|E-Mail         :    abhishekkumar8399@gmail.com
#|----------------------------------------------------------------|
class Math:
    def __init__(self,num):
        self.num=num

    def add2num(self,n):
        self.num=self.num+n
            
    @staticmethod  #self is not required
    def add(a,b):
        return a+b
    
# result=Math.add(1,2)
# print(result)
a=Math(5)
print(a.num)
a.add2num(6)
print(a.num)
print(a.add(5,2))
print(Math.add(7,2))