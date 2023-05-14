#|----------------------------------------------------------------|
#|Description    :    FileIO Program
#|----------------------------------------------------------------|
#|Author         :    ABHISHEK KUMAR, Computer Science Student
#|----------------------------------------------------------------|
#|Organization   :    NMAMIT, Nitte
#|----------------------------------------------------------------|
#|E-Mail         :    abhishekkumar8399@gmail.com
#|----------------------------------------------------------------|
# f=open('myfile.txt','r')#r,w,a,rt,rb
# # print(f)
# text=f.read()
# print(text)
# f.close()

# f=open('myfile.txt','w')#r,w,a,rt,rb
# # print(f)
# f.write('Hello ji Kya hal chal')
# f.close()

# f=open('myfile.txt','a')#r,w,a,rt,rb
# # print(f)
# f.write(' Hello ji Kya hal chal')
# f.close()

with open('myfile.txt','w')as f:
    f.write('Hello World')