#|----------------------------------------------------------------|
#|Description    :    Finally Program
#|----------------------------------------------------------------|
#|Author         :    ABHISHEK KUMAR, Computer Science Student
#|----------------------------------------------------------------|
#|Organization   :    NMAMIT, Nitte
#|----------------------------------------------------------------|
#|E-Mail         :    abhishekkumar8399@gmail.com
#|----------------------------------------------------------------|
try:
    l=[1,5,6,7]
    i=int(input("Enter the index: "))
    print(l[i])
except:
    print("Some Error Occured")
finally:     #used if it is in function
    print("I always runs")

def func1():
    try:
        l=[1,5,6,7]
        i=int(input("Enter the index: "))
        print(l[i])
    except:
        print("Some Error Occured")
    finally:     #used if it is in function
        print("I always runs")

    x=func1()
    print(x)