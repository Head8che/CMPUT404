import requests

def versionCheck():
    print('Requests Version:', requests.__version__)

def get():
    response = requests.get("http://www.google.com/")
    print('\n GET Method (Google Homepage):', response.text)
    
def rawURL():
    url = "https://raw.githubusercontent.com/Head8che/CMPUT404/master/Labs/Lab_1/scripts.py"
    response = requests.get(url)
    print('\n Raw URL:', response.text)

versionCheck()
get()
rawURL()
