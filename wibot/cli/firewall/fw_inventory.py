import csv
import re
import os 

def get_inventory():
	filedir = os.path.dirname(__file__)
	filepath = os.path.join(filedir,'format_devices.csv')
	with open(filepath, mode='r') as csv_file:
		csv_reader = csv.DictReader(csv_file)
		device_list = []
		for row in csv_reader:
			if re.search('asa',row["Device"]) and not re.search('qa',row["Device"]):
				asa_device = row["Device"]
				counter = asa_device.count('-')
				if counter == 2:
					device_list.append(asa_device)
		return(device_list)

if __name__ == '__main__':
	sys.exit()
