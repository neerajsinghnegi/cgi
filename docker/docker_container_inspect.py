#!/usr/bin/python3
import cgi
import subprocess

print("content-type: text/html")
print()

response = cgi.FieldStorage()


cname = response.getvalue("x")


output = subprocess.getoutput("sudo docker inspect "+ cname)
print(output)
