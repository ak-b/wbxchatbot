import paramiko
from paramiko import SSHClient
import time
from wibot.utils import get_config

configs = get_config()
USERNAME = configs['BIGIP_USERNAME']
PASSWORD = configs['BIGIP_PASSWORD']
bigip_server= configs['BIGIP_SRVR']

try:
    ssh_client: SSHClient = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
except Exception as e1:
    print("main exception " + str(e1))

def lookup_ipi(ip_lookup):
	try:
		ssh_client.connect(bigip_server,username=USERNAME,password=PASSWORD)
		chan = ssh_client.invoke_shell()
		temp = chan.recv(1024).decode('ascii')
		chan.send("bash\n")
		time.sleep(1)
		temp = chan.recv(1024).decode('ascii')
		chan.send("iprep_lookup {}\n".format(ip_lookup))
		time.sleep(2)
		temp = chan.recv(5000).decode('ascii')
		#print(temp)
		data = temp.splitlines()
		for line in data[3:-1]:
			print(line)
		ssh_client.close()

	except paramiko.ssh_exception.AuthenticationException:
		print("Authentication Failure")

	except Exception as e:
		print("Unable to connect to DB, please try again later")

if __name__ == "__main__":
	#search_ipi('20.190.137.6')
	sys.exit()