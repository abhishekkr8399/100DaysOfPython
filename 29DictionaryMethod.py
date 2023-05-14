#|----------------------------------------------------------------|
#|Description    :    Dictionary Method Program
#|----------------------------------------------------------------|
#|Author         :    ABHISHEK KUMAR, Computer Science Student
#|----------------------------------------------------------------|
#|Organization   :    NMAMIT, Nitte
#|----------------------------------------------------------------|
#|E-Mail         :    abhishekkumar8399@gmail.com
#|----------------------------------------------------------------|
#ordered
ep1={122:45,123:89,867:69,670:69}
ep2={222:67,566:90}
ep1.update(ep2)
print(ep1)
ep1.pop(122)
print(ep1)
ep1.popitem()  #remove last item
print(ep1)
ep1.clear()
print(ep1)
empt={}
print(empt)