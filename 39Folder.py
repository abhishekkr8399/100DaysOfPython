#|----------------------------------------------------------------|
#|Description    :    Folder Program
#|----------------------------------------------------------------|
#|Author         :    ABHISHEK KUMAR, Computer Science Student
#|----------------------------------------------------------------|
#|Organization   :    NMAMIT, Nitte
#|----------------------------------------------------------------|
#|E-Mail         :    abhishekkumar8399@gmail.com
#|----------------------------------------------------------------|
import os
folders=os.listdir("data")
print(os.getcwd())
os.chdir("/Users")
print(os.getcwd())
for f in folders:
    print(f)
    print(os.listdir(f"data/{f}"))