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
	#HARDCODING INVENTORY BECAUSE TOO MANY INVENTORY CHANGES AND MOST OF THEM ARE UNTRACKED IN NETDB
	#Updating inventory (recorded changes using inventory_update.py script locally), removed inventory
	devices = []    
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
	for item in ftd_devices:
		print("Checking on FTD % s" % item['name'])
		show_caps(item['ip_address'],item['name'])
