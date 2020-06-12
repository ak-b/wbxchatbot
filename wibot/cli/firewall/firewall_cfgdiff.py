import os
import csv
import html2text
import datetime
from datetime import date,datetime, timedelta
import click
import re
import requests 
from requests.auth import HTTPBasicAuth
from wibot.utils import get_config

configs = get_config()
NETDB_USERNAME = configs['NETDB_USERNAME']
NETDB_PASSWORD = configs['NETDB_PASSWORD']

@click.group(help = "ASA Configuration Changes in the past 24hrs")
def cfgdiff():
	pass

@cfgdiff.command(help= "ASA Configuration Changes in the past 24hrs")
def cfgdiff():
	netdb_url_diff= 'https://dfw01-netdb.webex.com/netdb/reports/cfgdiff/?fmt=csv&re=asa&cd=1&so=Last%20Commit&cmp[]=on&cmp[]=on'
	path_db = "/logs"
	file = "config_diff_netdb.csv"
	file_path = os.path.join(path_db,file)

	netdb_download = requests.get(netdb_url_diff,auth=HTTPBasicAuth(NETDB_USERNAME,NETDB_PASSWORD))
	#print(netdb_download.status_code)
	if netdb_download.status_code == 200:
		#print(netdb_download.text[:])
		##extract timestamp
		current = date.today()
		past = current - timedelta(days=1)
		open(file_path,'wb').write(netdb_download.content)
		with open(file_path,mode='r') as csv_file:
			csv_reader = csv.DictReader(csv_file)
			counter = 0
			for row in csv_reader:
				timefield=row["Last Commit"]
				datefield = timefield.split()[0]
				#print(datefield)
				if str(current) == datefield or str(past) == datefield:
					counter = counter + 1
					device= row["Device"]	
					if re.search("-cl-",device):
						pass
					else:	
						print("ASA CONFIGURATION DIFF IN THE PAST 24HRS\n")
						dev_diff_url='https://dfw01-netdb.webex.com/netdb/reports/cfgdiff/?dev={}&cd=0&rep='.format(device)
						dev_diff_download= requests.get(dev_diff_url,auth=HTTPBasicAuth(NETDB_USERNAME,NETDB_PASSWORD))
						if dev_diff_download.status_code == 200:
							content_html = dev_diff_download.text[:]
							content_text = html2text.html2text(content_html)
							#print(content_text)
							content = content_text.splitlines()
							click.echo(click.style("Device&Context: {}\n".format(device),bold='True'))
							print("ConfigChange:\n")
							for line in content:
								if re.search(">",line):
									print(line.replace('>',""))
			if counter == 0:
				print("No ASA Configuration Changes in the Past 24hrs") 
	else:
		print("Sorry! We are experiencing network connectivity issues, Please try again after sometime")

if __name__ == '__main__':
	cfgdiff()