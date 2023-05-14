#|----------------------------------------------------------------|
#|Description    :    String Methods Program
#|----------------------------------------------------------------|
#|Author         :    ABHISHEK KUMAR, Computer Science Student
#|----------------------------------------------------------------|
#|Organization   :    NMAMIT, Nitte
#|----------------------------------------------------------------|
#|E-Mail         :    abhishekkumar8399@gmail.com
#|----------------------------------------------------------------|
str="Abhishek Kumar ! ! ! ! !"        #Strings are immutable
print(str.upper())          #is new String
print(str.lower()) 
print(str.rstrip("!"))      #Only Trailing Stripes are removed
print(str.replace("Abhishek","Unknown"))
print(str.split(" "))       #split from space 

Heading="hello world welcome!"
print(Heading.capitalize()) #capitalize  the first character and convert remaining character to lowercase 

str1="Welcome to the Console!!!"
print(len(str1)) #25
print(str1.center(50))
print(len(str1.center(50))) #50
print(str1.count("o")) #4
print(str1.endswith("!")) #True
print(str1.endswith("to",4,10)) #from 4 to 9 index is the sub string ending with "to"

str2="He's name is Den. he is the best person in the world"
print(str2.find("is")) #10
print(str2.find("isi")) #-1
# print(str2.index("isi")) #error

str3="IamaBoy00"      #[A-Z,a-z,0-9]
print(str3.isalnum()) #True should contain only #[A-Z,a-z,0-9]
print(str3.isalpha()) #False should contain only #[A-Z,a-z]
print(str3.islower())  #False
print(str3.isprintable()) #True
str3="IamaBoy00\n" 
print(str3.isprintable()) #False
str3="          " 
print(str3.isspace()) #True

str3="To Kill a Mocking bird"
print(str3.istitle()) #False
str3="To Kill A Mocking Bird"
print(str3.istitle()) #True
print(str3.startswith("T")) #True
print(str3.swapcase()) #swaps upper to lower and lower to upper
print(str3.title()) #Captalize 1st char of each word and remaining to lowercase
