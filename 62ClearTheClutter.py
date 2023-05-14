#|----------------------------------------------------------------|
#|Description    :    Clear The Clutter Program
#|----------------------------------------------------------------|
#|Author         :    ABHISHEK KUMAR, Computer Science Student
#|----------------------------------------------------------------|
#|Organization   :    NMAMIT, Nitte
#|----------------------------------------------------------------|
#|E-Mail         :    abhishekkumar8399@gmail.com
#|----------------------------------------------------------------|
import os
# os.rename("clutter/6.txt","clutter/text.txt")/
files=os.listdir("clutter")
i=1
for f in files:
    if f.endswith(".png"):
        print(f)
        os.rename(f"clutter/{f}",f"clutter/{i}.png")
        i+=1