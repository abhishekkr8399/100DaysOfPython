#|----------------------------------------------------------------|
#|Description    :    Generators Program
#|----------------------------------------------------------------|
#|Author         :    ABHISHEK KUMAR, Computer Science Student
#|----------------------------------------------------------------|
#|Organization   :    NMAMIT, Nitte
#|----------------------------------------------------------------|
#|E-Mail         :    abhishekkumar8399@gmail.com
#|----------------------------------------------------------------|
def my_gen():
    for i in range(100):
        yield i

gen=my_gen()

for j in gen:
    print(j)