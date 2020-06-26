import requests
import json
import click

@click.group(help = "**Trigger NS FW MMP Config Push Globally**")
def enable_mmp():
	pass

@enable_mmp.command(help = "**Trigger NS FW MMP Config Push Globally**")
def enable_mmp():
	url_req = 'http://10.241.90.66/fwtemplateservice/api/v1/OnFWtemplateApprovedByCompoent/mmp'
	cfggen_req = requests.post(url_req)
	#print(cfggen_req.status_code)
	if cfggen_req.status_code == 200:	
		result = json.loads(cfggen_req.content.decode('utf-8'))
		taskID = result['data']['taskID']
		print("\nFirewall North-South Configuration for MMP is Successfully Processed\n")
		print("TaskID: {}".format(taskID))
		#DEV URL
		#http://10.240.214.60:7075/fwdevicemgmt/dryrun
		#PROD URL
		#http://10.240.214.60:7072/fwdevicemgmt/dryrun
		url_dryrun = 'http://10.240.214.60:7072/fwdevicemgmt/dryrun'
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