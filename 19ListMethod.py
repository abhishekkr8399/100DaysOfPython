#|----------------------------------------------------------------|
#|Description    :    List Methods Program
#|----------------------------------------------------------------|
#|Author         :    ABHISHEK KUMAR, Computer Science Student
#|----------------------------------------------------------------|
#|Organization   :    NMAMIT, Nitte
#|----------------------------------------------------------------|
#|E-Mail         :    abhishekkumar8399@gmail.com
#|----------------------------------------------------------------|
list=[11,2,33,4,5,6,6,6,6]
list.append(7)
print(list)
# list.sort(reverse=True)
# print(list)
# list.reverse()
# print(list)
# print(list.index(6))
# print(list.count(6))
m=list.copy()
m[0]=0
print(list)
m=list
m[0]=0
print(list)
list.insert(1,899)
print(list)
k=[900,1000,1100]
list.extend(k)
print(list)
p=list+m
print(p)