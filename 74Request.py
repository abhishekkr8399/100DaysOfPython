#|----------------------------------------------------------------|
#|Description    :    Request Module Program
#|----------------------------------------------------------------|
#|Author         :    ABHISHEK KUMAR, Computer Science Student
#|----------------------------------------------------------------|
#|Organization   :    NMAMIT, Nitte
#|----------------------------------------------------------------|
#|E-Mail         :    abhishekkumar8399@gmail.com
#|----------------------------------------------------------------|
import requests
from bs4 import BeautifulSoup
# response = requests.get("https://www.google.com")
# print(response.text)

# url="https://jsonplaceholder.typicode.com/posts"
# data={
#     "title": "harry",
#     "body": "bhai",
#     "userId": "12",
# }
# headers={
#     'Content-Type': 'application/json;charset=utf-8',
# }
# response=requests.post(url,headers=headers,json=data)
# print(response.text)

url="http://www.google.com"
r=requests.get(url)
soup=BeautifulSoup(r.text,'html.parser')
print(soup.prettify())


















