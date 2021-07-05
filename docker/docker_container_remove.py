#!/usr/bin/python3
import cgi
import subprocess

print("content-type: text/html")
print()

response = cgi.FieldStorage()


cname = response.getvalue("x")

#print(cname)
subprocess.getoutput("sudo docker stop "+ cname)
output = subprocess.getoutput("sudo docker rm "+ cname)
print(output +" removed.")
