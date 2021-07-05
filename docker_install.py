#!/usr/bin/python3
import cgi
import subprocess

print("content-type: text/html")
print()

def docker_install():
	os.system("yum install docker-ce --nobest -y")
	os.system("systemctl start docker")
	os.system("systemctl enable docker")
	os.system("firewall-cmd --zone=public --add-masquerade --permanent")
	os.system("firewall-cmd --zone=public --add-port=80/tcp")
	os.system("firewall-cmd --zone=public --add-port=443/tcp")
	os.system("firewall-cmd --reload")
	os.system("systemctl restart docker")
	os.system("yum install httpd")
	os.system("systemctl enable httpd")

print("Docker-CE successfully installed.")
