#|----------------------------------------------------------------|
#|Description    :    Map Filter Reduce Program
#|----------------------------------------------------------------|
#|Author         :    ABHISHEK KUMAR, Computer Science Student
#|----------------------------------------------------------------|
#|Organization   :    NMAMIT, Nitte
#|----------------------------------------------------------------|
#|E-Mail         :    abhishekkumar8399@gmail.com
#|----------------------------------------------------------------|

# #MAP
# def cube(x):
#     return x*x*x
# print(cube(2))
# l=[1,2,3,4,5,3,6,75,9]
# # newl=[]
# # for i in l:
# #     newl.append(cube(i))
# newl=list(map(cube,l))
# print(newl)

# #FILTER
# def filter_func(a):
#     return a>4
# newl2=list(filter(filter_func,l))
# print(newl2)

#REDUCE
from functools import reduce
num=[1,2,3,4,10]
sum=reduce(lambda x,y:x+y,num)
print(sum)
