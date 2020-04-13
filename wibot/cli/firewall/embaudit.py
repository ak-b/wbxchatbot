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

	## to use predefined list till we come up with another function that does inventory
	## this script can work on invnetory specified in ASA_devices which pulls device informartion from netdb
	## and take into account the fact that some devices may be decommed/migrated

	device_inventory = []

	if device:
		device_inventory.append(device)
	else:
		ASA_predefined = ['ams01-wxp00-asa02a.webex.com', 'ams01-wxp00-asa02b.webex.com',\
		 'ams01-wxp00-asa04a.webex.com', 'ams01-wxp00-asa04b.webex.com', 'ams01-wxp00-asa21a.webex.com',\
		 'ams01-wxp00-asa21b.webex.com', 'ams01-wxp00-asacl01.webex.com',\
		 'ams01-wxvc-asacl01.webex.com', 'dfw01-wxp00-asa02a.webex.com',\
		 'dfw01-wxp00-asa02b.webex.com', 'dfw01-wxp00-asa03a.webex.com', 'dfw01-wxp00-asa03b.webex.com',\
		 'dfw01-wxp00-asa04a.webex.com', 'dfw01-wxp00-asa04b.webex.com', 'dfw01-wxp00-asacl01.webex.com',\
		 'dfw02-wxp00-asa03a.webex.com', 'dfw02-wxp00-asa03b.webex.com', 'dfw02-wxp00-asa04a.webex.com',\
		 'dfw02-wxp00-asa04b.webex.com', 'dfw02-wxp00-asa21a.webex.com', 'dfw02-wxp00-asa21b.webex.com',\
		 'dfw02-wxp00-asacl01.webex.com', 'dfw02-wxvc-asa01a.webex.com', 'dfw02-wxvc-asa01b.webex.com',\
		 'dfw02-wxvc-asa02a.webex.com', 'dfw02-wxvc-asa02b.webex.com', 'dfw02-wxvc-asacl01.webex.com',\
		 'iad02-wxp00-asa04a.webex.com', 'iad02-wxp00-asa04b.webex.com',\
		 'iad02-wxp00-asacl01.webex.com', 'jfk01-edge0-asacl01.webex.com',\
		 'jfk01-svc00-asacl01.webex.com', 'lhr03-wxp00-asa02a.webex.com', 'lhr03-wxp00-asa02b.webex.com',\
		 'lhr03-wxp00-asa04a.webex.com', 'lhr03-wxp00-asa04b.webex.com',\
		 'lhr03-wxp00-asacl01.webex.com',\
		 'lhr03-wxvc-asacl01.webex.com',\
		 'nrt03-wxp00-asa04a.webex.com', 'nrt03-wxp00-asa04b.webex.com',\
		 'nrt03-wxp00-asa21a.webex.com', 'nrt03-wxp00-asa21b.webex.com', 'nrt03-wxvc-asa01a.webex.com',\
		 'nrt03-wxvc-asa01b.webex.com', 'ord10-wxp00-asa21a.webex.com', 'ord10-wxp00-asa21b.webex.com',\
		 'sin01-wxp00-asa04a.webex.com',\
		 'sin01-wxp00-asa04b.webex.com', 'sin01-wxp00-asa21a.webex.com', 'sin01-wxp00-asa21b.webex.com',\
		 'sin01-wxvc-asa01a.webex.com', 'sin01-wxvc-asa01b.webex.com', 'sjc02-wxp00-asa02a.webex.com',\
		 'sjc02-wxp00-asa02b.webex.com', 'sjc02-wxp00-asa03a.webex.com', 'sjc02-wxp00-asa03b.webex.com',\
		 'sjc02-wxp00-asa04a.webex.com', 'sjc02-wxp00-asa04b.webex.com', 'sjc02-wxp00-asa21a.webex.com',\
		 'sjc02-wxp00-asa21b.webex.com', 'sjc02-wxp00-asacl01.webex.com', 'sjc02-wxvc-asa01a.webex.com',\
		 'sjc02-wxvc-asa01b.webex.com', 'sjc02-wxvc-asa02a.webex.com', 'sjc02-wxvc-asa02b.webex.com',\
		 'sjc02-wxvc-asacl01.webex.com', 'syd01-edge0-asacl01.webex.com', 'syd01-svc00-asacl01.webex.com',\
		 'yyz01-wxp00-asa01a.webex.com', 'yyz01-wxp00-asa01b.webex.com']
	 
		#test_ASA = ['sjc02-wxqa-asatest1.webex.com']
		#small_inventory = ['ams01-wxp00-asa02a.webex.com','dfw01-wxp00-asacl01.webex.com','sin01-wxp00-asa21a.webex.com']
		#test_device = ['lhr03-wxvc-asacl01.webex.com']
		test_device = ['dfw01-wxp00-asa04a.webex.com','dfw01-wxp00-asa02a.webex.com','dfw01-wxp00-asa02b.webex.com']
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
		#print(device)
		contexts = extract_contexts(device)
		#print(contexts)
		#print(len(contexts))
		if contexts:
			count_check = count_check + len(contexts)
			for ctx in contexts:
				raw_result_ctx = emb_result(device,ctx)
				#print(raw_result_ctx)
				if raw_result_ctx and re.search("set", raw_result_ctx):
					raw_lines = raw_result_ctx.splitlines()
					for line in raw_lines:
						format_line= line.strip()
						if format_line.startswith('set'):
							rawSetting = format_line
							#print(rawSetting)
					raw_setting_aggr= rawSetting.split()
					#print(raw_setting_aggr)
					#print("number of items:",len(raw_setting_aggr))
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
		#print(table_net)

	#print(count_check)
	#if len(table_net) < 10:
	#	print(tabulate(table_net, headers = ["Device","Context","EmbConn_Max","EmbConn_PerHost"], colalign=("left","left","left","left")))
	
	f.write(tabulate(table_net, headers = ["Device","Context","EmbConn_Max","EmbConn_PerHost"], colalign=("left","left","left","left")))
	f.close()

