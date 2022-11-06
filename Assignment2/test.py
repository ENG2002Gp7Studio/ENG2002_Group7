import os
import datetime

def ums_encryption(ip):

        op = ""
        for i in range(0, len(ip)):
            op += chr(ord(ip[i]) + 129)

        return op

def ums(ip):

        op = ""
        for i in range(0, len(ip)):
            op += chr(ord(ip[i]) - 129)

        return op

print(datetime.datetime.timestamp(datetime.datetime.now()))