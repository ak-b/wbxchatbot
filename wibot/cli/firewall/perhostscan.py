import os
import time
import re
import paramiko
from paramiko import SSHClient
from wibot.utils import get_config

#USERNAME = os.environ.get('FW_USERNAME')
#PASSWORD = os.environ.get('FW_PASSWORD')
#ENABLE_PASSWORD = os.environ.get('PASSWORD')
#ENABLE_PASSWORD = os.environ.get('ENABLE_PASSWORD')

configs = get_config()
BOT_USERNAME = configs['BOT_USERNAME']
BOT_PASSWORD = configs['BOT_PASSWORD']
ENABLE_PASSWORD = configs['ENABLE_PASSWORD']

try:
    ssh_client: SSHClient = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
except Exception as e1:
    print("main exception " + str(e1))

def extract_contexts(FW):
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
		# add enable password once you test out prod devices
		if re.search("Password:", temp):
			chan.send("%s\n" % ENABLE_PASSWORD)
		chan.send("terminal page 0\n")
		temp = chan.recv(1024).decode('ascii')
		time.sleep(1)
		chan.send("changeto system\n")
		time.sleep(1)
		temp = chan.recv(1024).decode('ascii')
		chan.send("show run context | in context\n")
		time.sleep(2)
		temp = chan.recv(1024).decode('ascii')
		context_data = temp.splitlines()
		context=[]
		for item in context_data:
			if item.startswith('context'):
				context.append((item.split("context",1)[1]).strip())
		if context:
			context.remove('Management')
		ssh_client.close()
		return context

	except paramiko.ssh_exception.AuthenticationException:
		print("Authentication Failure")
		print("Device where exception occured %s" % FW)
	except Exception as e:
		print("exception" +str(e))
		print("Device where exception occured %s" % FW)

def emb_result(FW,ctx):
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
		# add enable password once you test out prod devices
		if re.search("Password:", temp):
			chan.send("%s\n" % ENABLE_PASSWORD)
		chan.send("terminal page 0\n")
		temp = chan.recv(1024).decode('ascii')
		time.sleep(1)
		chan.send("changeto system\n")
		time.sleep(1)
		temp = chan.recv(1024).decode('ascii')
		time.sleep(1)
		chan.send("changeto context %s\n" % ctx )
		time.sleep(1)
		chan.send("sh running-config | in connection embryonic-conn-max\n")
		time.sleep(1)
		temp = chan.recv(1024).decode('ascii')
		ssh_client.close()
		return temp

	except paramiko.ssh_exception.AuthenticationException:
		print("Authentication Failure")
	except Exception as e:
		print("exception" +str(e))
		print("Device %s" % FW)