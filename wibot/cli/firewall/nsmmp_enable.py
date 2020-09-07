import requests
import json
import click

@click.group(help = "**Trigger NS FW MMP Config Push Globally**")
def enable_mmp():
	pass

@enable_mmp.command(help = "**Trigger NS FW MMP Config Push Globally**")
def enable_mmp():
	url_req = '<>'
	cfggen_req = requests.post(url_req)
	if cfggen_req.status_code == 200:	
		result = json.loads(cfggen_req.content.decode('utf-8'))
		taskID = result['data']['taskID']
		print("\nFirewall North-South Configuration for MMP is Successfully Processed\n")
		print("TaskID: {}".format(taskID))
		url_dryrun = ''
		req_body = {
	"devicelist": [
	    ]
	}	
		headers = {
    		'Accept': 'application/json',
    		'Content-Type':'application/json'
    		}

		dryrun_req = requests.post(url_dryrun, data=json.dumps(req_body), headers=headers)
		if dryrun_req.status_code == 200:
			print("Below Mentioned FW Configurations are generated and scheduled to push during respective DC MW")
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


	else:
		print("MMP NS automation trigger unsuccessful details down below:\n")
		print(cfggen_req.content)



if __name__ == "__main__":
	enable_mmp()
