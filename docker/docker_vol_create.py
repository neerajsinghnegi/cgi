#!/usr/bin/python3
import cgi
import subprocess

print("content-type: text/html")
print()

response = cgi.FieldStorage()


vname = response.getvalue("x")


output = subprocess.getoutput("sudo docker volume create "+ vname)
print(output)
