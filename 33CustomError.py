#|----------------------------------------------------------------|
#|Description    :    Custom Error  Program
#|----------------------------------------------------------------|
#|Author         :    ABHISHEK KUMAR, Computer Science Student
#|----------------------------------------------------------------|
#|Organization   :    NMAMIT, Nitte
#|----------------------------------------------------------------|
#|E-Mail         :    abhishekkumar8399@gmail.com
#|----------------------------------------------------------------|
a=int(input("Enter any value between 5 and 9: "))
if (a<5 or a>9):
    raise ValueError("Value must be between 5 and 9")
