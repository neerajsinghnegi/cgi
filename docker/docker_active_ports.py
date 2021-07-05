#!/usr/bin/python3
import cgi
import subprocess as sp

print("content-type: text/html")
print()


output = sp.getstatusoutput("sudo netstat -tnlp")

status = output[0]
result = output[1]

if status == 0:
    print("Output: "+ "<pre>"+ result +"</pre>")
else:
    print("Error !! ")
