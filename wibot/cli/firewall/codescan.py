from wibot.cli.firewall.show_version import show_version
import re
import os
from tabulate import tabulate
import click


@click.group(help="Check ASA Software Code Version")
def codescan():
	pass

@codescan.command(help="Check ASA Software Code Version")
@click.option('--device')
def codescan(device):
	#PREDEFINING INVENTORY FOR ASA's 
	# Removing inventory

	if device:
		print("Overriding Scan across all Devices\nScanning device {} ...".format(device))
		net_inventory=[device]
	else:
		net_inventory = inventory_asa

	#print(net_inventory)
	#print(len(net_inventory))

	#small_inventory = ['sjc02-wxqa-asatest1.webex.com']
	#test_inventory = ['ams01-wxp00-asa02a.webex.com','ams01-wxp00-asa21a.webex.com','dfw01-wxp00-asacl01.webex.com']
	device_info = []
	sw_verlist = []
	sys_verlist = []
	table_net = []

	codeverscan_filedir ='/logs/'
	#print(codeverscan_filedir)
	codeverscan_file_name ='CodeVersion_log.txt'
	codeverscan_filepath = os.path.join(codeverscan_filedir, codeverscan_file_name)

	if os.path.exists(codeverscan_filepath):
		os.remove(codeverscan_filepath)

	f = open(codeverscan_filepath,'a+')
	for device in net_inventory:
		result = show_version(device)
		if result:
			device_info.append(device)
			data = result.splitlines()
			for line in data:
				search_key1 ='Software Version'
				search_key2 = 'System Version'
				if re.search(search_key1, line):
					sw_raw = line.split(search_key1,1)[1]
					sw_ver_un = sw_raw.split('<context>',1)[0]
					sw_ver = sw_ver_un.strip()
					sw_verlist.append(sw_ver)
					#print(sw_ver)
					#print(sw_verlist)
				elif re.search(search_key2, line):
					sys_raw = line.split(search_key2,1)[1]
					sys_ver = sys_raw.strip()
					sys_verlist.append(sys_ver)
					#print(sys_ver)
					#print(sys_verlist)
			table = [device,sw_ver,sys_ver]
			#print(table)
			table_net.append(table)
		else:
			print("Skipping device {} due to connectivity failure".format(device))


	#print(tabulate(table_net, headers = ["ASA Device","Software Version","System Version"]))
	if table_net:
		f.write(tabulate(table_net, headers = ["ASA Device","Software Version","System Version"]))
		f.close()
	else:
		f.write("This Code Version Log File is Empty Because the Device/Devices are unreachable")
		f.close()



