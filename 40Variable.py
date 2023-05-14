#|----------------------------------------------------------------|
#|Description    :    Variable Program
#|----------------------------------------------------------------|
#|Author         :    ABHISHEK KUMAR, Computer Science Student
#|----------------------------------------------------------------|
#|Organization   :    NMAMIT, Nitte
#|----------------------------------------------------------------|
#|E-Mail         :    abhishekkumar8399@gmail.com
#|----------------------------------------------------------------|
x=4
print(x)
def hello():
    global x
    x=5
    print(f"The Local Variable is {x}")
    print("Hello Abhishek")
print(f"The global variable is {x}")
hello()
print(f"The global variable is {x}")