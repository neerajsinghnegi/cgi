#!/usr/bin/python3
import cgi
import subprocess

print("content-type: text/html")
print()

response = cgi.FieldStorage()

cname = response.getvalue("x")
iname = response.getvalue("y")
#print(value)
output = subprocess.getoutput("os.system('docker run -dit --name cname inam')")

print(output)
