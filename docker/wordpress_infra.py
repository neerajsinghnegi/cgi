#!/usr/bin/python3
import cgi
import subprocess

print("content-type: text/html")
print()

def main():
  subprocess.getoutput(' curl -L "https://github.com/docker/compose/releases/download/1.25.5/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose')
  subprocess.getoutput("chmod +x /usr/local/bin/docker-compose")
  subprocess.getoutput("cp docker-compose.yml /") 
  subprocess.getoutput("cd / ")
  subprocess.getoutput("mkdir /infrastructure")
  subprocess.getoutput("cd /infrastructure/")
  subprocess.getoutput("pwd")
  subprocess.getoutput("mv ../docker-compose.yml .")
  a =subprocess.getoutput("docker-compose up -d")
  print(a + " Wordpress is ready to use. Run Wordpress in browser with Base OS IP and port no. : 8080. for ex- 192.168.43.139:8080")

if __name__ = "__main__":
    main()

