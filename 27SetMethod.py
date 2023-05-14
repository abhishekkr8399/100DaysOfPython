#|----------------------------------------------------------------|
#|Description    :    Set Methods Program
#|----------------------------------------------------------------|
#|Author         :    ABHISHEK KUMAR, Computer Science Student
#|----------------------------------------------------------------|
#|Organization   :    NMAMIT, Nitte
#|----------------------------------------------------------------|
#|E-Mail         :    abhishekkumar8399@gmail.com
#|----------------------------------------------------------------|
s1={1,2,5,6}
s2={3,6,7}
print(s1.union(s2))
print(s1.intersection(s2))
print(s1.difference(s2))
print(s1.symmetric_difference(s2))  #leave common
print(s1.isdisjoint(s2))  
print(s1.issubset(s2))  
print(s1.issuperset(s2))  
s2.add(9)
s1.update(s2)
print(s1)
s1.remove(9)  #will show error if item is not found but discard will not
print(s1)
s1.pop()
print(s1)
#del s1 will delete s1
#clear() will remove all items
if 6 in s1:
    print("Present")
else:
    print("Absent")