#|----------------------------------------------------------------|
#|Description    :    Time Program
#|----------------------------------------------------------------|
#|Author         :    ABHISHEK KUMAR, Computer Science Student
#|----------------------------------------------------------------|
#|Organization   :    NMAMIT, Nitte
#|----------------------------------------------------------------|
#|E-Mail         :    abhishekkumar8399@gmail.com
#|----------------------------------------------------------------|
# import time
# timestamp=time.strftime("%Y-%m-%d")
# print(timestamp)     #print Date
# timestamp=time.strftime("%H-%M-%S")
# print(timestamp)     #print Time
# timestamp=time.strftime("%H")
# print(timestamp)     #print Hour
# timestamp=time.strftime("%M")
# print(timestamp)     #print Minute
# timestamp=time.strftime("%S")
# print(timestamp)     #print Second
# #https://docs.python.org/3/library/time.html#time.strftime
import time
hour=int(time.strftime("%H"))
if hour<12:
    print("Good morning sir")
elif hour<16:
    print("Good Afternoon sir")
elif hour<19:
    print("Good Evening sir")
elif hour<24:
    print("Good Night sir")
