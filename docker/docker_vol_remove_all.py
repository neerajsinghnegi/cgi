#!/usr/bin/python3
import cgi
import subprocess

print("content-type: text/html")
print()

response = cgi.FieldStorage()




output = subprocess.getoutput("sudo docker volume prune -f")
print(output)
