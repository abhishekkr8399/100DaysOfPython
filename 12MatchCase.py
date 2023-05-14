#|----------------------------------------------------------------|
#|Description    :    Match Case Program
#|----------------------------------------------------------------|
#|Author         :    ABHISHEK KUMAR, Computer Science Student
#|----------------------------------------------------------------|
#|Organization   :    NMAMIT, Nitte
#|----------------------------------------------------------------|
#|E-Mail         :    abhishekkumar8399@gmail.com
#|----------------------------------------------------------------|
x=4
match x:
    case 0:
        print("x is zero")  #break not required
    case 4 if x % 2 == 0:
        print("x %2 == 0 and case is 4")
    case _ if x<10:
        print("x is < 10")
    case _:
        print("Default case")