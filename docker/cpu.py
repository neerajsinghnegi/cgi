#!/usr/bin/python3
import cgi
import subprocess as sp

print("content-type: text/html")
print()


output = subprocess.getstatusoutput("sudo free -m")
status = output[0]
result = output[1]

if status == 0:
    print("Output: "+ result)
else:
    print("Error !!")
