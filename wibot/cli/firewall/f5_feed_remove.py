import os
import re
import paramiko
from paramiko import SSHClient
from wibot.utils import get_config 

configs = get_config()

feed_server = configs['FEEDSERVER_IP']
username = configs['FEEDSERVER_USERNAME']
password = configs['FEEDSERVER_PASSWORD']

def remove_feed(search_key):
	try:
		ssh = paramiko.SSHClient()
		ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		ssh.connect(feed_server, username=username, password=password)
		sftp = ssh.open_sftp()
		dirname = '/var/www/html/iad02-ddos-ipifs'
		filename = 'F5-BL_WL-feed.txt'
		result = 0
		f = sftp.open(dirname + '/' + filename, 'r')
		new_f = f.readlines()
		f_create = sftp.open(dirname + '/' + filename, 'w')
		f.seek(0)
		if re.search('/',search_key):
			new_key = re.sub('/',',',search_key)
			for line in new_f:
				if new_key not in line:
					f_create.write(line)
				else:
					result=1
			f.close()
			f_create.close()
		else:
			for line in new_f:
				if search_key not in line:
					f_create.write(line)
				else:
					result=1
			f.close()
			f_create.close()
		return result
		ssh.close()

	except paramiko.ssh_exception.AuthenticationException:
		print("Authentication Failure")
	except Exception as e:
		print(e)
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
		print(e)
		print("Sorry! I am unable to connect to FeedServer,please try after sometime")

def ip_remove_feed_wl(ip,org):
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
			print("Searching for {}".format(ip))
			result=remove_feed(ip)
			if result == 1:
				print("Match Found")
				print("Removing IP {} from Whitelist".format(ip))
				print("Feed File Content After Removal")
				display_feed()

			elif result == 0:
				print("Match Not Found")

		elif match_sub:
			IPnet = ip.split('/')[0]
			mask = ip.split('/')[1]
			data = "{0},{1},wl,{2}\n".format(IPnet,mask,org)
			print("Searching for {}".format(ip))
			result=remove_feed(ip)
			if result == 1:
				print("Match Found")
				print("Removing Subnet {} from Whitelist".format(ip))
				print("Feed File Content After Removal")
				display_feed()
			elif result == 0:
				print("Match Not Found")

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
		print(e)
		print("Sorry! I am unable to connect to FeedServer,please try after sometime")

if __name__ == '__main__':
	#display_feed()
	#ip_remove_feed_wl('20.20.0.0/16','test6')
	sys.exit()