import requests
import json
import click

@click.group(help = "**Dryrun Global FW Configuration Changes**")
def dryrun():
	pass

@dryrun.command(help = "**Dryrun Global Configuration Changes**")
def dryrun():
	url_dryrun = 'http://10.240.214.60:7072/fwdevicemgmt/dryrun'
	#DEV URL
	#http://10.240.214.60:7075/fwdevicemgmt/dryrun
	#PROD URL
	#http://10.240.214.60:7072/fwdevicemgmt/dryrun
	req_body = {
"devicelist": [
    "AMS01-WXP00-ASACL01-Core",
    "DFW01-WXP00-ASACL01-Core",
    "DFW02-WXP00-ASACL01-Core",
    "IAD02-WXP00-ASACL01-Core",
    "JFK01-EDGE0-ASACL01-WEBEX",
    "LHR03-WXP00-ASACL01-Core",
    "NRT03-WXP00-ASACL01-Core",
    "SIN01-WXP00-ASACL01-Core",
    "SJC02-WXP00-ASACL01-Core",
    "SYD01-EDGE0-ASACL01-WEBEX"
    ]
}

	headers = {
		'Accept': 'application/json',
		'Content-Type':'application/json'
		}

	dryrun_req = requests.post(url_dryrun, data=json.dumps(req_body), headers=headers)
	#print(dryrun_req.status_code)
	if dryrun_req.status_code == 200:
		print("Dry Run Results for MMP NS FW Configurations")
		response = json.loads(dryrun_req.content.decode('utf-8'))
		iteration_devices = response['ciap-fwaction-output']['native']['device']
		#print(iteration_devices)
		for device in iteration_devices:
			print("***************")
			print("Device : {}.WEBEX.COM Context : {}".format(device['response']['device'], device['response']['context']))
			print("Configuration:")
			[print(config) for config in device['response']['config']]
			print("***************")
	else:
		print("Dry Run Encountered an Error, details down below:\n")
		print(dryrun_req.content)