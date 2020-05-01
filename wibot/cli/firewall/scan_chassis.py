import os
import sys
import paramiko
import time
import re
import socket
from paramiko import SSHClient
from wibot.utils import get_config

#TO DO: Convert USERNAME, PASSWORD AND ENABLE_PASSWORD to VAULT(FOR LOCAL QA ONLY)


configs = get_config()
USERNAME = configs['BOT_USERNAME']
PASSWORD = configs['BOT_PASSWORD']


try:
    ssh_client: SSHClient = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
except Exception as e1:
    print("main exception " + str(e1))

def chassis_pwr(FW,cmd):
    try:
        ssh_client.connect(hostname=FW, username=USERNAME, password=PASSWORD,\
            allow_agent=False, look_for_keys=False, timeout=10)
        chan = ssh_client.invoke_shell()
        time.sleep(1)
        temp = chan.recv(1024).decode('ascii')
        chan.send("terminal length 511\n")
        #print(temp)
        chan.send("sh chassis environment {}\n".format(cmd)) 
        time.sleep(1)
        content=''
        while chan.recv_ready():
            time.sleep(1)
            temp = chan.recv(1024).decode('ascii')
            content = content + temp
        #print(temp) 
        return(content)               
        ssh_client.close()

    except paramiko.ssh_exception.AuthenticationException:
    	print("Authentication Failure")
    except Exception as e:
        print("Unable to login to {} possible migration/decom".format(FW))

if __name__ == "__main__":
	sys.exit()