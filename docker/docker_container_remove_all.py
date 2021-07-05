#!/usr/bin/python3
import cgi
import subprocess

print("content-type: text/html")
print()

output = subprocess.getoutput("sudo docker rm -f $(sudo docker ps)")
print(output)

print("successfully removed all containers.")
