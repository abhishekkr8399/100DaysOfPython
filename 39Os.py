#|----------------------------------------------------------------|
#|Description    :    Os Program
#|----------------------------------------------------------------|
#|Author         :    ABHISHEK KUMAR, Computer Science Student
#|----------------------------------------------------------------|
#|Organization   :    NMAMIT, Nitte
#|----------------------------------------------------------------|
#|E-Mail         :    abhishekkumar8399@gmail.com
#|----------------------------------------------------------------|
import os
if not os.path.exists("data"):
    os.mkdir("data")
for i in range(0,100):
    os.mkdir(f"data/Day{i+1}")