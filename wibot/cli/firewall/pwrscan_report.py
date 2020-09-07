import re
import os
from wibot.cli.firewall.extract_chassisURL import filtered_url
from wibot.cli.firewall.scan_chassis import chassis_pwr
from wibot.cli.firewall.scan_legacyasa import scan_asa

def report(device):

	inventory_asalegacy = []

	chassis_url_raw = []

	chassis4150_url = []
	

	## ADD inventory for 9300 and 4150 together because they need the exact same steps
	## for extraction of psu and fan health

	chassis = chassis_url_raw + chassis4150_url
	
	#print(chassis)
	#print(inventory_asalegacy)

	#STEPS IF THE USER SPECIFIES A INPUT DEVICE
	#1. DETERMINE THE TYPE OF DEVICE
	#2. IF ASA LEGACY DO NOTHING
	#3. IF ASA CLUSTER EXTRACT CHASSIS FPRA AND FPRB APPEND
	#4. IF ASA 21 EXTRACT CHASSIS FPR*
	
	#CREATE A MAP TO PICK either of one_asa, one_chassis_url and one_chassis4150_url
	#IF DEVICE DOESN'T EXIST THEN RUN ACROSS THE ENTIRE INVENTORY
	
	#print(device)
	
	if device:
		print("Overriding Scan across all Devices\nScanning device {} ...".format(device))
		chassis=[]
		inventory_asalegacy=[]
		if re.search("asacl",device.lower()):
			urlA= (filtered_url(device.lower()))
			if re.search('a.webex.com',urlA):
				urlB = urlA.replace('a.webex.com','b.webex.com')
			elif re.search('b.webex.com',urlA):
				urlB = urlA.replace('b.webex.com','a.webex.com')
			chassis.append(urlA)
			chassis.append(urlB)

		elif re.search("asa21",device.lower()):
			response = filtered_url(device.lower())
			if response != -1:
				url=filtered_url(device.lower()).lower()
				chassis.append(url)

		elif re.search("asa", device.lower()):
			inventory_asalegacy.append(device.lower())


	pwrscan_file_dir = '/logs/'
	#print(pwrscan_file_dir)
	pwrscan_file_name = 'PwrScan_log.txt'
	#print(pwrscan_file_name)
	pwrscan_filepath = os.path.join(pwrscan_file_dir,pwrscan_file_name)
	#print(pwrscan_filepath)
	if os.path.exists(pwrscan_filepath):
		os.remove(pwrscan_filepath)
		#print("Old file removed")
	pwrscan_file = open(pwrscan_filepath,'a+')

	## LOGIN TO EACH DEVICE CHASSIS AND CHECK FOR POWER SUPPLY
	if chassis:
		for device in chassis:
			pwrscan_file.write('Device:' + device + '\n')
			result1 = chassis_pwr(device,'fan')
			result2 = chassis_pwr(device,'psu')

			if result1:
				index1 = result1.find('511')
				result1_filtered = result1[index1+3:]
				pwrscan_file.write(result1_filtered + '\n')
			else:
				message = "Unable to scan device {} for fan health".format(device)
				pwrscan_file.write('\n' + message + '\n')
			if result2:
				index2 = result2.find('511')
				result2_filtered = result2[index2+3:]
				pwrscan_file.write(result2_filtered + '\n')
			else:
				message = "Unable to scan device {} for psu health".format(device)
				pwrscan_file.write('\n' + message + '\n')


	##LOGIN TO EACH LEGACY ASA AND CHECK FOR POWER SUPPLY HEALTH
	if inventory_asalegacy:	
		for device in inventory_asalegacy:
			pwrscan_file.write('Device:' + device + '\n')
			result = scan_asa(device)
			if result:
				#print(result)
				pwrscan_file.write('\n'+result+'\n')
			else:
				message = "Unable to scan device {} for psu and fan health".format(device)
				pwrscan_file.write('\n' + message + '\n')

		pwrscan_file.close()

