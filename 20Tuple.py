#|----------------------------------------------------------------|
#|Description    :    Tuple Program
#|----------------------------------------------------------------|
#|Author         :    ABHISHEK KUMAR, Computer Science Student
#|----------------------------------------------------------------|
#|Organization   :    NMAMIT, Nitte
#|----------------------------------------------------------------|
#|E-Mail         :    abhishekkumar8399@gmail.com
#|----------------------------------------------------------------|
#immutable
tup1=(1,2,9,"Green",True)
print(type(tup1),tup1)
tup2=(1,2)
print(type(tup2),tup2)
tup3=(1,)
print(type(tup3),tup3)
tup=(1)
print(type(tup),tup)
if True in tup1:
    print("Yes")
tupn=tup1[1:4]
print(tupn)