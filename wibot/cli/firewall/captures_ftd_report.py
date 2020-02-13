import sys
import os
import time
import paramiko
import re
from paramiko import SSHClient
from wibot.utils import get_config

configs = get_config()

FTD_USERNAME = configs['FTD_USERNAME']
FTD_PASSWORD = configs['FTD_PASSWORD']

try:
	ssh_client: SSHClient = paramiko.SSHClient()
	ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
except Exception as e1:
	print("main exception " + str(e1))

def show_caps(FTD,name):
	try:
		ssh_client.connect(hostname=FTD, username=FTD_USERNAME, password=FTD_PASSWORD,\
			allow_agent=False, look_for_keys=False, timeout=10)
		chan = ssh_client.invoke_shell() 
		temp = chan.recv(1024).decode('ascii')
		#print(temp)
		while not re.search("Firepower-module", temp):
			#print("not matched")
			temp = chan.recv(1024).decode('ascii')
			#print(temp)
		if re.search("Firepower-module", temp):
			#print("matched")
			chan.send("connect ftd\n")
		time.sleep(1)
		temp = chan.recv(1024).decode('ascii')
		#print(temp)
		while not re.search(">",temp):
			#print("prompt not reached")
			temp = chan.recv(1024).decode('ascii')
		#print(temp)
		if re.search(">",temp):
			chan.send("show capture\n")
		time.sleep(1)
		temp = chan.recv(1024).decode('ascii')
		#print(temp)
		chan.send("exit\n")
		chan.send("exit\n")
		capture_content = temp.splitlines()
		flag =0 
		for item in capture_content:
			if item.startswith('capture'):
				print('Capture exists on %s' % name)
				flag = 1
		if flag == 0:
			print("Capture doesn't exist on %s" % name)
        
		ssh_client.close()

	except paramiko.ssh_exception.AuthenticationException:
		print("Authentication Failure")
	except Exception as e:
		print("exception" +str(e))


if __name__ == '__main__':
	sys.exit()
	'''
	devices = get_inventory()
	for item in devices:
		print("Checking for FTD % s" % item['name'])
		show_caps(item['ip_address'],item['name'])
	'''

