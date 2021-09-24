#!/usr/bin/env python3
import os
import json


print('Content-Type: text/html')
print("<title>Test CGI</title>")
print("<p>This is a Test</p>")

print() 
print(os.environ)
# print(json.dumps(dict(os.environ)))

jsonObject = json.dumps(dict(os.environ), indent = 4)
print(jsonObject)

# Example HTTP GET request using a query string
quertString = "QUERY_STRING"

for param in os.environ.keys():
   if(param == quertString):
       print(f"<em>{param}</em> ={os.environ[param]}</li>")
       print("<b>%20s</b> %s<br>" % (param, os.environ[param]))
print(os.environ["QUERY_STRING"])


userAgent = "HTTP_USER_AGENT"
for param in os.environ.keys():
   if(param == userAgent):
       print(f"<em>{param}</em> ={os.environ[param]}</li>")
       print("<b>%20s</b> %s<br>" % (param, os.environ[param]))
print(os.environ["HTTP_USER_AGENT"])

