import requests
import json
import click

@click.group(help = "**Dryrun Global FW Configuration Changes**")
def dryrun():
	pass

@dryrun.command(help = "**Dryrun Global Configuration Changes**")
def dryrun():
	url_dryrun = ''
#masked code
	req_body = ''

	headers = {
		'Accept': 'application/json',
		'Content-Type':'application/json'
		}

	dryrun_req = requests.post(url_dryrun, data=json.dumps(req_body), headers=headers)
	if dryrun_req.status_code == 200:
		print("Dry Run Results for MMP NS FW Configurations")
		response = json.loads(dryrun_req.content.decode('utf-8'))
		iteration_devices = response['ciap-fwaction-output']['native']['device']
		for device in iteration_devices:
			print("***************")
			print("Device : {}.WEBEX.COM Context : {}".format(device['response']['device'], device['response']['context']))
			print("Configuration:")
			print(config) for config in device['response']['config']]
			print("***************")
	else:
		print("Dry Run Encountered an Error, details down below:\n")
		print(dryrun_req.content)
