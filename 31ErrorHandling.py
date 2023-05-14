#|----------------------------------------------------------------|
#|Description    :    Error Handling Program
#|----------------------------------------------------------------|
#|Author         :    ABHISHEK KUMAR, Computer Science Student
#|----------------------------------------------------------------|
#|Organization   :    NMAMIT, Nitte
#|----------------------------------------------------------------|
#|E-Mail         :    abhishekkumar8399@gmail.com
#|----------------------------------------------------------------|
a=input("Enter the number: ")
print(f"Multiplication table of {a} is: ")
try:
    for i in range(1,11):
        print(f"{int(a)} X {i} = {int(a)*i}")
except:
    print("Invalid input!")

print("Some other lines...")
print("End of program")



try:
    num=int(input("Enter an integer: "))
    a=[6,3]
    print(a[num])
except ValueError:
    print("Invalid input!")
except IndexError:
    print("Index Error!")