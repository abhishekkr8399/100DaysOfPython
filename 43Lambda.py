#|----------------------------------------------------------------|
#|Description    :    Lambda Program
#|----------------------------------------------------------------|
#|Author         :    ABHISHEK KUMAR, Computer Science Student
#|----------------------------------------------------------------|
#|Organization   :    NMAMIT, Nitte
#|----------------------------------------------------------------|
#|E-Mail         :    abhishekkumar8399@gmail.com
#|----------------------------------------------------------------|

# def double(x):
#     return x*2
def appl(fx,value):
    return 6+fx(value)

double=lambda x:x*2
cube=lambda x:x*x*x
avg=lambda x,y:(x+y)/2

print(double(5))
print(cube(5))
print(avg(5,7))
print(appl(cube,2))