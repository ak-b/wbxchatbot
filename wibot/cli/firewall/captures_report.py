import sys 
import os
import time
import re
import paramiko 
from paramiko import SSHClient
from wibot.cli.firewall.fw_inventory import get_inventory
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
				context.append(item.split("context",1)[1])
		return context
		ssh_client.close()

	except paramiko.ssh_exception.AuthenticationException:
		print("Authentication Failure")
	except Exception as e:
		print("exception" +str(e))

def format_caps(data,ctx,FW):
	content = data.splitlines()
	#print("Inside each context")
	#print(content)
	for item in content:
		if item.startswith('capture'):
			#print(filedir)
			filedir = '/logs/'
			filename = 'report.txt'
			cap_file = os.path.join(filedir,filename)
			with open(cap_file,'a+') as f:
				f.write("Capture left running on context %s on device %s\n" % (ctx,FW))
				f.close()

def check_caps(FW):
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
		contexts = extract_contexts(FW)
		#print(contexts)
		for ctx in contexts:
			time.sleep(1)
			chan.send("changeto context %s\n" % ctx )
			time.sleep(1)
			if re.search('asacl',FW):
				chan.send("cluster exec show cap\n")
			elif re.search('asa',FW):
				chan.send("show capture\n")
			time.sleep(1)
			temp = chan.recv(1024).decode('ascii')
			#print(temp)
			format_caps(temp,ctx,FW)
		ssh_client.close()

	except paramiko.ssh_exception.AuthenticationException:
		print("Authentication Failure")
	except Exception as e:
		print("exception" +str(e))

if __name__== 'main':
	sys.exit()
