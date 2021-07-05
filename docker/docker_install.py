#!/usr/bin/python3
import cgi
import subprocess

print("content-type: text/html")
print()


def main():
  subprocess.getoutput("yum install docker-ce --nobest -y")
  subprocess.getoutput("systemctl start docker")
  subprocess.getoutput("systemctl enable docker")
  subprocess.getoutput("firewall-cmd --zone=public --add-masquerade --permanent")
  subprocess.getoutput("firewall-cmd --zone=public --add-port=80/tcp")
  subprocess.getoutput("firewall-cmd --zone=public --add-port=443/tcp")
  subprocess.getoutput("firewall-cmd --reload")
  subprocess.getoutput("systemctl restart docker")
  subprocess.getoutput("yum install httpd")
  subprocess.getoutput("systemctl enable httpd")
  print("Docker-CE successfully installed.")


if __name__ == "__main__":
    main()
