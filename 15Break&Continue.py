#|----------------------------------------------------------------|
#|Description    :    Break and continue Program
#|----------------------------------------------------------------|
#|Author         :    ABHISHEK KUMAR, Computer Science Student
#|----------------------------------------------------------------|
#|Organization   :    NMAMIT, Nitte
#|----------------------------------------------------------------|
#|E-Mail         :    abhishekkumar8399@gmail.com
#|----------------------------------------------------------------|
i=0
j=0
for i in range(12):
    if(i>=11):
        break
    print("5 X",i,"=",5*i)
print("----------------------------------------------------------------")
for j in range(15):
    if(j==11 or j==12 or j==13 or j==14):
        continue
    print("5 X",j,"=",5*j)

k=0
while True:
    print(k)
    k=k+1
    if(k%10==0):
        break