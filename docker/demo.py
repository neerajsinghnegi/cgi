#!/usr/bin/python3
import cgi
import subprocess as sp

print("content-type: text/html")
print()

response = cgi.FieldStorage()


cname = response.getvalue("x")

output = sp.getstatusoutput(cname)
status = output[0]
result = output[1]

#print(status)
#print(result)

if status == 0:
    print("Output: "+ result)
else:
    print("Error !!")
