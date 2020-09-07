from wibot.cli.firewall.perhostscan import emb_result , extract_contexts
import click
from tabulate import tabulate
import datetime
from datetime import date
import os
import re

@click.group(help = "Check MAX Embryonic Connection and Per Host Settings")
def embaudit():
	pass

@embaudit.command(help = "Check MAX Embryonic Connection and Per Host Settings")
@click.option('--device')
def embaudit(device):

	#ASA_devices = get_inventory()
	device_inventory = []

	if device:
		device_inventory.append(device)
	else:
		ASA_predefined = []
		device_inventory = ASA_predefined

	embconaudit_filedir =  '/logs/'
	#print(embconaudit_filedir)
	#timestamp = datetime.datetime.now()
	embconaudit_file_name ='EmbConScan_log.txt'
	embcon_filepath = os.path.join(embconaudit_filedir, embconaudit_file_name)
	if os.path.exists(embcon_filepath):
		os.remove(embcon_filepath)

	f = open(embcon_filepath,'a+')
	table_net = []

	# number of rows in the table should match the count_check
	count_check = 0 

	for device in device_inventory:
		contexts = extract_contexts(device)
		if contexts:
			count_check = count_check + len(contexts)
			for ctx in contexts:
				raw_result_ctx = emb_result(device,ctx)
				if raw_result_ctx and re.search("set", raw_result_ctx):
					raw_lines = raw_result_ctx.splitlines()
					for line in raw_lines:
						format_line= line.strip()
						if format_line.startswith('set'):
							rawSetting = format_line
					raw_setting_aggr= rawSetting.split()
					setting_size = len(raw_setting_aggr)
					if setting_size == 4:
						embconn_max = raw_setting_aggr[3]
						embconn_perhost = 'NotSet'
					elif setting_size == 6:
						embconn_max = raw_setting_aggr[3]
						embconn_perhost = raw_setting_aggr[5]
				else:
					embconn_max = 'NotSet'
					embconn_perhost = 'NotSet'
				table = [device,ctx,embconn_max,embconn_perhost]
				#print(table)
				table_net.append(table)
		else:
			print("Skipping device {} because of connectivity issue".format(device))
	
	f.write(tabulate(table_net, headers = ["Device","Context","EmbConn_Max","EmbConn_PerHost"], colalign=("left","left","left","left")))
	f.close()

