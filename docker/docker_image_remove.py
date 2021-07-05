#!/usr/bin/python3
import cgi
import subprocess

print("content-type: text/html")
print()

response = cgi.FieldStorage()


iname = response.getvalue("x")

#print(cname)

output = subprocess.getoutput("sudo docker rmi "+ iname)
print(output)
