import os
import sys
import paramiko
import time
import re
import socket
from paramiko import SSHClient
from wibot.utils import get_config

configs = get_config()
USERNAME = configs['BOT_USERNAME']
PASSWORD = configs['BOT_PASSWORD']
ENABLE_PASSWORD = configs['ENABLE_PASSWORD']

try:
    ssh_client: SSHClient = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
except Exception as e1:
    print("main exception " + str(e1))

def scan_asa(FW):
    try:
        ssh_client.connect(hostname=FW, username=USERNAME, password=PASSWORD,\
            allow_agent=False, look_for_keys=False, timeout=10)
        chan = ssh_client.invoke_shell()
        time.sleep(1)
        chan.send("enable\n")
        time.sleep(2)
        temp = chan.recv(1024).decode('ascii')
        #print(temp)
        if re.search("Password:", temp):
            # print("***")
            chan.send("%s\n" % ENABLE_PASSWORD)
        else:
            sys.exit(1)
        chan.send("terminal pager 0\n")
        chan.send("changeto system\n")
        time.sleep(1)
        temp = chan.recv(1024).decode('ascii')
        time.sleep(1)
        chan.send('show environment power-supplies\n')
        time.sleep(1)
        temp = chan.recv(1024).decode('ascii')
        return(temp)
        '''
        while chan.recv_ready():
            time.sleep(2)
            temp = chan.recv(1024).decode('ascii')
            print(temp)
        '''                
        ssh_client.close()

    except paramiko.ssh_exception.AuthenticationException:
        print("Authentication Failure")
    except Exception as e:
        print("Unable to login to {}, possible migration/decom".format(FW))


if __name__ == "__main__":
    sys.exit()
    #scan_asa('ams01-wxp00-asa02a.webex.com')