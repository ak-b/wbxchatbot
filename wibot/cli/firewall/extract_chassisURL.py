import sys
import os
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

def extract_rawurl(FW):
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
        chan.send('show chassis-management-url\n') 
        time.sleep(5)
        while chan.recv_ready():
            time.sleep(1)
            temp = chan.recv(1024).decode('ascii')
        #print(temp) 
        return(temp)               
        ssh_client.close()

    except paramiko.ssh_exception.AuthenticationException:
        print("Authentication Failure")
    except Exception as e:
        print("exception" + str(e))
        print("Unable to login to {}".format(FW))

def filtered_url(FW):
    
    sample =extract_rawurl(FW)
    if sample and sample.strip():
        lines = sample.splitlines()
        for line in lines:
            if line.startswith('https'):
                rawUrl= line 
        #print(rawUrl)
        search_key = re.search('//(.*):',rawUrl)
        filtered_url = search_key.group(1)
        #print(filtered_url)
        return(filtered_url)
    else:
        return -1

if __name__ == "__main__":
   sys.exit()