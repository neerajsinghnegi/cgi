#!/usr/bin/python3
import cgi
import subprocess

print("content-type: text/html")
print()

response = cgi.FieldStorage()


cname = response.getvalue("x")
iname = response.getvalue("y")

#print(cname)
#print(iname)

output = subprocess.getoutput("sudo docker run -dit  --name "+ cname +" "+ iname)

status = output[0]
result = output[1]

if status == 0:
    print("{0} container successfuly launced with image {1}".format(cname,iname))
else:
    print("Failed : {}".format(result))

