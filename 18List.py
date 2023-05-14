#|----------------------------------------------------------------|
#|Description    :    List Program
#|----------------------------------------------------------------|
#|Author         :    ABHISHEK KUMAR, Computer Science Student
#|----------------------------------------------------------------|
#|Organization   :    NMAMIT, Nitte
#|----------------------------------------------------------------|
#|E-Mail         :    abhishekkumar8399@gmail.com
#|----------------------------------------------------------------|
list=[1,3,5,7,9,"Hello",True]
print(type(list))
print(list)
print(list[0])
if False in list:
    print("Yes")
else:
    print("No")
if "ello" in "Hello":
    print("Yes")

lst=[i*i for i in range(11)]
lst2=[i*i for i in range(11) if i%2==0]
print(lst)
print(lst2)