#|----------------------------------------------------------------|
#|Description    :    MultiProcessing Program
#|----------------------------------------------------------------|
#|Author         :    ABHISHEK KUMAR, Computer Science Student
#|----------------------------------------------------------------|
#|Organization   :    NMAMIT, Nitte
#|----------------------------------------------------------------|
#|E-Mail         :    abhishekkumar8399@gmail.com
#|----------------------------------------------------------------|
import multiprocessing
import concurrent.futures
import requests
def downloadFile(url,name):
    response = requests.get(url)
    open(f"files/file{name}.jpg","wb").write(response.content)

url="https://picsum.photos/2000/3000"
# pros=[]
# for i in range(5):
#     # downloadFile(url,i)
#     p=multiprocessing.Process(target=downloadFile,args=[url,i])
#     p.start()
#     pros.append(p)

# for p in pros:
#     p.join()

with concurrent.futures.ProcessPoolExecutor() as executer:
    l1=[url for i in range(60)]
    l2=[i for i in range(60)]
    result = executer.map(downloadFile, l1, l2)
    for r in result:
        print(r)