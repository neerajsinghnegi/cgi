#!/usr/bin/python3
import cgi
import subprocess

print("content-type: text/html")
print()

response = cgi.FieldStorage()


cname = response.getvalue("x")

#print(cname)

output = subprocess.getoutput("sudo docker attach "+ cname)
print(output +" attached.")
