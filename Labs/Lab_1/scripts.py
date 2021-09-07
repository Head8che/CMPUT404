import requests

def versionCheck():
    print(requests.__version__)

# 
def get():
    response = requests.get("http://www.google.com/")
    print(response.text)
    

def rawURL():
    url = "https://raw.githubusercontent.com/Head8che/CMPUT404/master/Labs/Lab_1/scripts.py"
    response = requests.get("http://www.google.com/")
    print(response.text)


rawURL()
