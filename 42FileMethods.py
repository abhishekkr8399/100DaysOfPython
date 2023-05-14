#|----------------------------------------------------------------|
#|Description    :    FileIO Methods Program
#|----------------------------------------------------------------|
#|Author         :    ABHISHEK KUMAR, Computer Science Student
#|----------------------------------------------------------------|
#|Organization   :    NMAMIT, Nitte
#|----------------------------------------------------------------|
#|E-Mail         :    abhishekkumar8399@gmail.com
#|----------------------------------------------------------------|
# f=open('myfile.txt','r')#r,w,a,rt,rb
# # print(f)
# i=0
# while True:
#     i+=1
#     line=f.readline()
#     if not line: 
#         print(line,type(line))
#         break
#     m1=line.split(",")[0]
#     m2=line.split(",")[1]
#     m3=line.split(",")[2]
#     print(f"Marks of student {i} in maths is:{m1}")
#     print(f"Marks of student {i} in science is:{m2}")
#     print(f"Marks of student {i} in English is:{m3}")
    
f=open('myfile2.txt','w')#r,w,a,rt,rb
# print(f)
f.writelines(['line 1\nline 2\nline 3\nline 4\nline 5'])
f.close()