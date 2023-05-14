#|----------------------------------------------------------------|
#|Description    :    Command Line Utilities Program
#|----------------------------------------------------------------|
#|Author         :    ABHISHEK KUMAR, Computer Science Student
#|----------------------------------------------------------------|
#|Organization   :    NMAMIT, Nitte
#|----------------------------------------------------------------|
#|E-Mail         :    abhishekkumar8399@gmail.com
#|----------------------------------------------------------------|
#curl
import argparse
import requests
def download(url,local):
    if local is "None":
        local=url.split('/')[-1]
    with requests.get(url,stream=True) as r:
        r.raise_for_status()
        with open(local,'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    return local
parser = argparse.ArgumentParser()
parser.add_argument("url",help="URL of file to download")
# parser.add_argument("output",help="Name by Which do you want to save the file")
parser.add_argument("-o", "--output",help="Name of the file",default=None)

args=parser.parse_args()
print(args.url)
print(args.output)
download(args.url,args.output)