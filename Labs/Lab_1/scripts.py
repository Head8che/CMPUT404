import requests

def versionCheck():
    print(requests.__version__)

# 
def get():
    r = requests.get("http://www.google.com/")
    print(r.text)
    

def rawURL():
    url = ""


get()
versionCheck()