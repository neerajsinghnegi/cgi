import subprocess

def main():
    output = subprocess.getoutput("date")

if __name__ == "__main__":
    main()

