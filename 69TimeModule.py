#|----------------------------------------------------------------|
#|Description    :    TIME MODULE Program
#|----------------------------------------------------------------|
#|Author         :    ABHISHEK KUMAR, Computer Science Student
#|----------------------------------------------------------------|
#|Organization   :    NMAMIT, Nitte
#|----------------------------------------------------------------|
#|E-Mail         :    abhishekkumar8399@gmail.com
#|----------------------------------------------------------------|
import time 
# def usingWhile():
#     i=0
#     while(i<5000):
#         i=i+1
#         print(i)

# def usingFor():
#     for i in range(5000):
#         print(i)

# init=time.time()
# usingFor()
# t1=time.time()-init
# init=time.time()
# usingWhile()
# print(time.time()-init)
# print(t1)


# print(1)
# time.sleep(1)
# print(2)
# time.sleep(2)
# print(3)
# time.sleep(3)
# print(4)
# time.sleep(4)


t=time.localtime()
formatted_time=time.strftime("%Y-%m-%d %H:%M:%S",t)
print(formatted_time)