#!/usr/bin/python3
import cgi
import subprocess as sp

print("content-type: text/html")
print()

response = cgi.FieldStorage()


cname = response.getvalue("x")
iname = response.getvalue("y")


output = sp.getstatusoutput("sudo docker commit {0} {1}".format(cname,iname))

status = output[0]
result = output[1]

if status == 0:
    print("Output: "+ result)
else:
    print("Error !!")
