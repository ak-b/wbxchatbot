import sys
import paramiko
import time
import re
import socket
from paramiko import SSHClient
from wibot.cli.firewall.post_process import cpu_process

#Convert USERNAME, PASSWORD AND ENABLE_PASSWORD to environment variables
USERNAME = 'Marvinh'
PASSWORD = 'Tested@2020'
ENABLE_PASSWORD = 'T!m32G0Br0'

try:
    ssh_client: SSHClient = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
except Exception as e1:
    print("main exception " + str(e1))

def run_show(FW, context, type):
    try:
        ssh_client.connect(hostname=FW, username= USERNAME, password= PASSWORD,\
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

        chan.send("terminal page 0\n")
        chan.send("changeto system\n")
        time.sleep(1)
        temp = chan.recv(1024).decode('ascii')
        #print(temp)
        chan.send("changeto context %s\n" % context)
        time.sleep(5)
        temp = chan.recv(1024).decode('ascii')
        time.sleep(1)
        if type == 'CPU':
        	chan.send("show cpu\n")
        elif type == 'MEMORY':
        	chan.send('show memory\n')
        elif type == 'EMBCONN':
        	chan.send('show running-config policy-map\n') 
        time.sleep(5)
        temp = chan.recv(1024).decode('ascii')      
        ssh_client.close()
        print(temp)

    except paramiko.ssh_exception.AuthenticationException:
        print("Authentication Failure")
    except Exception as e:
        print("exception" + str(e))



