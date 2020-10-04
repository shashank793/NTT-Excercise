import ftplib
import subprocess
import pysftp
import sys

USERNAME = input("Enter Username : ")
HOST     = input("Enter Host Name : ")

def FTP(USERNAME,HOST):
    PASSWORD = input("Enter Password : ")
    source_file = input("Source File Path : ")
    destination_file = input("Destination File Path : ")
    session = ftplib.FTP(HOST,USERNAME,PASSWORD)
    file = open(source_file,'rb')
    session.storbinary('STOR {0}'.format(destination_file), file)
    print("FTP Done !")
    file.close()
    session.quit()
def SCP(USERNAME,HOST):
    source_file = input("Source File Path : ")
    destination_file = input("Destination File Path : ")
    subprocess.run(["scp", source_file, USERNAME+'@'+HOST])
    print("SCP Done")

def SFTP(USERNAME,HOST):
    PASSWORD = input("Enter Password : ")
    source_file = input("Source File Path : ")
    destination_file = input("Destination File Path : ")

    with pysftp.Connection(HOST, username=USERNAME, password=PASSWORD) as sftp:
        sftp.put(source_file, destination_file)

    print('Upload done.')

FTP(USERNAME,HOST)
SCP(USERNAME,HOST)
SFTP(USERNAME,HOST)