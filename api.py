#!/usr/bin/python3
import cgi
import os

print("content-type: text/html")
print()

form = cgi.FieldStorage()
x = form.getvalue('x')
output = subprocess.getstatusoutput('sudo ' + x)
status = output[0]
cmdoutput = output[1]
db = {"output": cmdoutput, "status": status}
final0 = json.dump(db)
print(finalo)
