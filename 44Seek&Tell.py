#|----------------------------------------------------------------|
#|Description    :    Seek() & Tell() and Truncate() Program
#|----------------------------------------------------------------|
#|Author         :    ABHISHEK KUMAR, Computer Science Student
#|----------------------------------------------------------------|
#|Organization   :    NMAMIT, Nitte
#|----------------------------------------------------------------|
#|E-Mail         :    abhishekkumar8399@gmail.com
#|----------------------------------------------------------------|
with open('file.txt', 'r') as f:
    print(type(f))
    f.seek(10)
    print(f.tell())
    data=f.read(5)
    print(data)

with open('sample.txt', 'w') as f:
    f.write('Hello World!')
    f.truncate(5)
with open('sample.txt', 'r') as f:
    print(f.read())