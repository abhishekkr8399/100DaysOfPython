#|----------------------------------------------------------------|
#|Description    :    Operation in Tuples Program
#|----------------------------------------------------------------|
#|Author         :    ABHISHEK KUMAR, Computer Science Student
#|----------------------------------------------------------------|
#|Organization   :    NMAMIT, Nitte
#|----------------------------------------------------------------|
#|E-Mail         :    abhishekkumar8399@gmail.com
#|----------------------------------------------------------------|
countries=("Spain", "United States","Italy", "India","England")
temp=list(countries)
temp.append("Russia")
temp.pop(3)
temp[2]="Finland"
countries=tuple(temp)
print(countries)
print(countries.count("Spain"))
tuple=(1,2,3,4,5,6,7,8,9,0,8,6,3,3,3)
print(tuple.index(3))
print(tuple.index(3,8,13))
print(len(tuple))