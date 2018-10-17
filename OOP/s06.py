import ftplib
import os
import socket

HOST = "ftp.acc.umu.se"
DIR = "Public/EFLIB"
FILE = "README"

try:
    f = ftplib.FTP()
    f.set_debuglevel(2)
    f.connect(HOST)

except Exception as e:
    print(e)
    exit()

print("***Connect to host {0}".format(HOST))


try:
    f.login()

except Exception as e:
    print(e)
    exit()

print("***Logged in as anonymous")

try:
    f.cwd(DIR)
except Exception as e:
    print(e)
    exit()

print("***Change dir to {0}".format(DIR))

try:
    f.retrbinary("RETR {0}".format(FILE),open(FILE,"wb").write())

except Exception as e:
    print(e)
    exit()

f.quit()


