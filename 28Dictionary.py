#|----------------------------------------------------------------|
#|Description    :    Dictionary Program
#|----------------------------------------------------------------|
#|Author         :    ABHISHEK KUMAR, Computer Science Student
#|----------------------------------------------------------------|
#|Organization   :    NMAMIT, Nitte
#|----------------------------------------------------------------|
#|E-Mail         :    abhishekkumar8399@gmail.com
#|----------------------------------------------------------------|
dic={
    "Good":"Accha",
    "Bad":"Bura"
}
print(dic["Good"])    #throw error if not present
print(dic.get("Bad"))
print(dic.keys())
print(dic.values())
print(dic.items())
for key in dic.keys():
    print(dict[key])
for value in dic.values():
    print(dict[value])
for key,value in dic.items():
    print(key,value)