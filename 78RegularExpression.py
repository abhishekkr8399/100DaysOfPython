#|----------------------------------------------------------------|
#|Description    :    Regular Expression Program
#|----------------------------------------------------------------|
#|Author         :    ABHISHEK KUMAR, Computer Science Student
#|----------------------------------------------------------------|
#|Organization   :    NMAMIT, Nitte
#|----------------------------------------------------------------|
#|E-Mail         :    abhishekkumar8399@gmail.com
#|----------------------------------------------------------------|
import re
pattern=r"[A-Z]+yclone"
text='''lorem ipsum dolor sit amet, consect lorem ipsum dolor sit amet lorem ipsum dolor sit ametlore'''
match=re.search(pattern, text)
print(match)
match=re.finditer(pattern, text)
for mat in match:
    print(mat.span())
    print(text[mat.span()[0]:mat.span()[1]])