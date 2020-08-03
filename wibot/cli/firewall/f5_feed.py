import os
import re
import paramiko
from paramiko import SSHClient
from wibot.utils import get_config 

configs = get_config()

feed_server = configs['FEEDSERVER_IP']
username = configs['FEEDSERVER_USERNAME']
password = configs['FEEDSERVER_PASSWORD']

def check_duplicates(search_string):
	"""
	Check for pre-existing entries in feedfile
	"""
	try:
		ssh = paramiko.SSHClient()
		ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		ssh.connect(feed_server, username=username, password=password)
		sftp = ssh.open_sftp()
		dirname = '/var/www/html/iad02-ddos-ipifs'
		filename = 'F5-BL_WL-feed.txt'
		f = sftp.open(dirname + '/' + filename, 'r')
		content = f.readlines()
		substring_search=search_string.split(',')
		#flag variable stores status 0 if the entry doesn't exist and status 1 if the entry exists

		flag=0

		#code an alternate solution that does an exact match 
		for line in content:
			data = line.strip('/n')
			if substring_search[1] == '':
				if re.search(substring_search[0],data):
					flag =1
					break
			elif substring_search[0] and substring_search[1]:
				if re.search(substring_search[0],data) and re.search(substring_search[1],data):
					flag = 1
					break
		return flag

	except paramiko.ssh_exception.AuthenticationException:
		print("Authentication Failure")
	except Exception as e:
		print("Sorry! I am unable to connect to FeedServer,please try after sometime")


def display_feed():
	"""
	Display Contents of Feed File
	"""
	try:
		ssh = paramiko.SSHClient()
		ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		ssh.connect(feed_server, username=username, password=password)
		sftp = ssh.open_sftp()
		dirname = '/var/www/html/iad02-ddos-ipifs'
		filename = 'F5-BL_WL-feed.txt'
		f = sftp.open(dirname + '/' + filename, 'r')
		try:
			for line in f:
				print(line.strip('\n'))
		finally:
			f.close()
		ssh.close()

	except paramiko.ssh_exception.AuthenticationException:
		print("Authentication Failure")
	except Exception as e:
		print("Sorry! I am unable to connect to FeedServer,please try after sometime")


def ip_feed_wl(ip,org):
	"""
	Usage: firewall feed-wl <IP> <org_name>
	Input format: 
	For subnets: a.b.c.x/n  eg:2.16.152.0/24 
	For individual IPs: a.b.c.d eg:165.225.112.210
	"""
	try:
		ssh = paramiko.SSHClient()
		ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		ssh.connect(feed_server, username=username, password=password)
		sftp = ssh.open_sftp()
		dirname = '/var/www/html/iad02-ddos-ipifs'
		filename = 'F5-BL_WL-feed.txt'

		#CHECK IF USER HAS INPUT A VALID IP ADDRESS
		regex_validIp =r"^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
		regex_validMask = r"\b([1,9]|[12][0-9]|3[0-2])\b"

		#regex_validSub = r"((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\/\b([1,9]|[12][0-9]|3[0-2])"
		'''unit tests
		#ip_check = "2.16.152.0/24"
		#ip_check = "10.0.024"
		#ip_check = "3...3"
		#ip_check = "-1.2.3.4"
	    #ip_check = "1.1.1.1."
		#ip_check = "192.168.1.256"
		#ip_check = "127.1"
		#ip_check = "165.225.112.2100"
		'''
		match_ip=[]
		match_sub=[]
		if re.search('/',ip):
			match_sub = re.compile(regex_validIp).findall(ip.split('/')[0]) and re.compile(regex_validMask).findall(ip.split('/')[1])
			#print("Checking if Valid Subnet")
			#print(match_sub)
		else:
			match_ip = re.compile(regex_validIp).findall(ip)
			#print("Checking if Valid IP")
			#print(match_ip)
		

		#CHECK IF SUBNET OR INDIVIDUAL IP ADDRESS and EXTRACT NETWORK AND SUBNET MASK
		if match_ip:
			data = "{0},,wl,{1}\n".format(ip,org)
			result = check_duplicates(data)
			if result == 0:
				print("Original Content of Feed File")
				display_feed()
				print("Going to add {}".format(data))
				f = sftp.open(dirname + '/' + filename, 'a+')
				f.write(data)
				f.close()
				print("Feed File Content After Addition")
				display_feed()
			elif result == 1:
				print("Please check your input (hint:{}),the entry you are tring to add already exists in the Feed File".format(ip))
				print("Current Content of Feed File")
				display_feed()

		elif match_sub:
			IPnet = ip.split('/')[0]
			mask = ip.split('/')[1]
			data = "{0},{1},wl,{2}\n".format(IPnet,mask,org)
			result = check_duplicates(data)
			
			if result == 0:
				print("Original Content of Feed File")
				display_feed()
				print("Going to add {}".format(data))
				f = sftp.open(dirname + '/' + filename, 'a+')
				f.write(data)
				f.close()
				print("Feed File Content After Addition")
				display_feed()
			elif result == 1:
				print("Please check your input (hint:{}),the entry you are tring to add already exists in the Feed File".format(ip))
				print("Current Feed File Content")
				display_feed()
			else:
				print("Duplicate module check failing ")


		else:
			print("Please check input,invalid IP/Subnet provided {}".format(ip))
			print("Input format:\n \
For subnets: a.b.c.x/n  eg:2.16.152.0/24 \n \
For individual IPs: a.b.c.d eg:165.225.112.210\n \
where a,b,c,d,x in range [0 to 255]\n \
and n in range [1 to 32]\n")

		ssh.close()


	except paramiko.ssh_exception.AuthenticationException:
		print("Authentication Failure")
	except Exception as e:
		print("Sorry! I am unable to connect to FeedServer,please try after sometime")

if __name__ == '__main__':
	sys.exit()


