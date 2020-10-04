import getpass
import sys
import telnetlib

HOST = "52.43.79.153"
user = input()
print("Enter Password")
try:
    p = getpass.getpass()
except Exception as error:
    print('ERROR', error)
else:
    print('Password entered:', p)

tn = telnetlib.Telnet(HOST)

tn.read_until("login: ")
tn.write(user + "\n")
if password:
    tn.read_until("Password: ")
    tn.write(password + "\n")

tn.write("ls\n")
tn.write("exit\n")

print(tn.read_all())