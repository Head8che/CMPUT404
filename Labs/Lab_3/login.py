#!/usr/bin/env python3
import cgi, cgitb
import os, json
from templates import login_page, secret_page, after_login_incorrect
from secret import Username, Password
from http.cookies import SimpleCookie

# print("Content-Type: text/html")

form = cgi.FieldStorage()

username = form.getvalue('username')
password = form.getvalue('password')


cookie = SimpleCookie(os.environ["HTTP_COOKIE"])
if cookie.get("username"):
    cookieUsername = cookie.get("username").value
else:
    None
if cookie.get("password"):
    cookiePassword= cookie.get("username").value
else:
    None


if (not username and not password):
    print(login_page())

elif (Username == username and Password == password):
        print("Successful Login")
        print("Set-Cookie: username={};".format(Username))
        print("Set-Cookie: password={};".format(Password))
        print(secret_page(username, password))

else:
    print("Incorrect credentials")
    print(after_login_incorrect())
    print("username = ", username)
    print("password = ", password)

    