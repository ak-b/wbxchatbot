from wibot.cli.firewall.fw_inventory import get_inventory
from wibot.cli.firewall.captures_report import check_caps
from wibot.cli.firewall.ftd_db import ftd_devices
from wibot.cli.firewall.captures_ftd_report import show_caps
import click
import os

@click.group(help='Check Captures')
def captures():
	pass

@captures.command('asa',help = 'Return ASA devices where captures are running')
def asa():
	#devices = ['ams01-wxp00-asa02a.webex.com']
	#devices = get_inventory()
	#HARDCODING INVENTORY BECAUSE TOO MANY INVENTORY CHANGES IN NETDB
	#Updating inventory (recorded changes using inventory_update.py script locally)
	devices = ['ams01-wxp00-asa02a.webex.com', 'ams01-wxp00-asa02b.webex.com',\
	'ams01-wxp00-asa04a.webex.com', 'ams01-wxp00-asa04b.webex.com',\
	'ams01-wxp00-asa21a.webex.com', 'ams01-wxp00-asa21b.webex.com',\
	'ams01-wxp00-asacl01.webex.com', 'ams01-wxvc-asacl01.webex.com',\
	'dfw01-wxp00-asa02a.webex.com', 'dfw01-wxp00-asa02b.webex.com',\
	'dfw01-wxp00-asa03a.webex.com', 'dfw01-wxp00-asa03b.webex.com',\
	'dfw01-wxp00-asa04a.webex.com', 'dfw01-wxp00-asa04b.webex.com',\
	'dfw01-wxp00-asacl01.webex.com', 'dfw02-wxp00-asa03a.webex.com',\
	'dfw02-wxp00-asa03b.webex.com', 'dfw02-wxp00-asa04a.webex.com',\
	'dfw02-wxp00-asa04b.webex.com', 'dfw02-wxp00-asacl01.webex.com',\
	'dfw02-wxp00-asacl02.webex.com', 'dfw02-wxvc-asa01a.webex.com',\
	'dfw02-wxvc-asa01b.webex.com', 'dfw02-wxvc-asa02a.webex.com',\
	'dfw02-wxvc-asa02b.webex.com', 'dfw02-wxvc-asacl01.webex.com',\
	'iad02-wxp00-asa04a.webex.com', 'iad02-wxp00-asa04b.webex.com',\
	'iad02-wxp00-asacl01.webex.com', 'jfk01-edge0-asacl01.webex.com',\
	'jfk01-svc00-asacl01.webex.com', 'lhr03-wxp00-asa02a.webex.com',\
	'lhr03-wxp00-asa02b.webex.com', 'lhr03-wxp00-asa04a.webex.com',\
	'lhr03-wxp00-asa04b.webex.com', 'lhr03-wxp00-asacl01.webex.com',\
	'lhr03-wxvc-asacl01.webex.com', 'nrt03-wxp00-asa04a.webex.com',\
	'nrt03-wxp00-asa04b.webex.com', 'nrt03-wxp00-asa21a.webex.com',\
	'nrt03-wxp00-asa21b.webex.com', 'nrt03-wxvc-asa01a.webex.com',\
	'nrt03-wxvc-asa01b.webex.com', 'ord10-wxp00-asa21a.webex.com',\
	'sin01-wxp00-asa04a.webex.com', 'sin01-wxp00-asa04b.webex.com',\
	'sin01-wxp00-asa21a.webex.com', 'sin01-wxp00-asa21b.webex.com',\
	'sin01-wxp00-asacl01.webex.com', 'sin01-wxvc-asa01a.webex.com',\
	'sin01-wxvc-asa01b.webex.com', 'sjc02-wxp00-asa02a.webex.com',\
	'sjc02-wxp00-asa02b.webex.com', 'sjc02-wxp00-asa03a.webex.com',\
	'sjc02-wxp00-asa03b.webex.com', 'sjc02-wxp00-asa04a.webex.com',\
	'sjc02-wxp00-asa04b.webex.com', 'sjc02-wxp00-asa21a.webex.com',\
	'sjc02-wxp00-asa21b.webex.com', 'sjc02-wxp00-asacl01.webex.com',\
	'sjc02-wxvc-asa01a.webex.com', 'sjc02-wxvc-asa01b.webex.com',\
	'sjc02-wxvc-asa02a.webex.com', 'sjc02-wxvc-asa02b.webex.com',\
	'sjc02-wxvc-asacl01.webex.com', 'syd01-edge0-asacl01.webex.com',\
	'syd01-svc00-asacl01.webex.com', 'yyz01-wxp00-asa01a.webex.com',\
	'yyz01-wxp00-asa01b.webex.com']
    #print(devices)
    
	for hosts in devices:
		check_caps(hosts)
	filedir = '/logs/'
	filepath = os.path.join(filedir,'report1.txt')
	if os.path.exists(filepath):
		f = open(filepath, 'r')
		contents = f.read()
		print(contents)
		os.remove(filepath)
	else:
		print("No captures exist")

@captures.command('ftd', help = 'Return FTD devices where captures are running')
def ftd():
	#print(ftd_devices)
	for item in ftd_devices:
		print("Checking on FTD % s" % item['name'])
		show_caps(item['ip_address'],item['name'])