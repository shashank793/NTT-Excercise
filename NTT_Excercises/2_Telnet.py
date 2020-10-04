import getpass
import telnetlib

HOST = "http://localhost:8000/"
user = raw_input("Enter your remote account: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until("login: ")
tn.write(user + "\n")
if password:
    tn.read_until("Password: ")
    tn.write(password + "\n")
n = int(input())

for i in n:
    tn.write("touch {0}_sample.txt".format(i))



tn.write("exit\n")

print(tn.read_all())