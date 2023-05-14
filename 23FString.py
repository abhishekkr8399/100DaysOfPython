#|----------------------------------------------------------------|
#|Description    :    fString Program
#|----------------------------------------------------------------|
#|Author         :    ABHISHEK KUMAR, Computer Science Student
#|----------------------------------------------------------------|
#|Organization   :    NMAMIT, Nitte
#|----------------------------------------------------------------|
#|E-Mail         :    abhishekkumar8399@gmail.com
#|----------------------------------------------------------------|
letter ="My name is {1} and I am From {0}"
country="India"
name="Abhishek"
print(letter.format(country,name))
print(f"My name is {name} and I am From {country}")
print(f"My name is {{name}} and I am From {{country}}")
price =49.99999
txt=f"For only {price:2f} dollars!"
print(txt)
print(type(f"{2*30}"))