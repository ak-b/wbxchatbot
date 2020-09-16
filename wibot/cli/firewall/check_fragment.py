## Requirement is for an INC , this is a specific case/feature for bot
## FEATURES
# 1. Predefinition of the inventory in this case: 
# 2. Script takes no user input and returns the output for the Core context 
# on both firewalls in step 1.
# 3. Later add the feature to customise user input

import sys
import os
import time
import re
import paramiko 
from paramiko import SSHClient
from wibot.utils import get_config

configs = get_config()
BOT_USERNAME = configs['BOT_USERNAME']
BOT_PASSWORD = configs['BOT_PASSWORD']
ENABLE_PASSWORD = configs['ENABLE_PASSWORD']

try:
	ssh_client: SSHClient = paramiko.SSHClient()
	ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
except Exception as e1:
	print("main exception " + str(e1))

def frag(FW):
	try:
		ssh_client.connect(hostname=FW, username=BOT_USERNAME, password=BOT_PASSWORD,\
			allow_agent=False, look_for_keys=False, timeout=10)
		chan = ssh_client.invoke_shell()
		temp = chan.recv(1024).decode('ascii')
		#print("Logged in")
		#print(temp)
		chan.send("enable\n")
		time.sleep(2)
		temp = chan.recv(1024).decode('ascii')
		#print(temp)
		if re.search("Password:", temp):
			chan.send("%s\n" % ENABLE_PASSWORD)
		chan.send("terminal page 0\n")
		temp = chan.recv(1024).decode('ascii')
		time.sleep(1)
		chan.send("changeto system\n")
		time.sleep(1)
		temp = chan.recv(1024).decode('ascii')
		time.sleep(1)
		chan.send("changeto context Core\n")
		time.sleep(1)
		temp = chan.recv(1024).decode('ascii')
		chan.send("cluster exec show fragment\n")
		time.sleep(1)
		while chan.recv_ready():
			time.sleep(1)
			temp = chan.recv(1024).decode('ascii')
			print(temp)
		ssh_client.close()

	except paramiko.ssh_exception.AuthenticationException:
		print("Authentication Failure")
	except Exception as e:
		print("Exception" +str(e))
		print("Unable to login to Device %s" % FW)


if __name__ == "__main__":
	sys.exit()
