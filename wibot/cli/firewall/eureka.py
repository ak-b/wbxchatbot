import requests
import json
import os
import re
import string
from tabulate import tabulate

from wibot.utils import get_config 

configs = get_config()

DEFAULT_USERNAME = configs['ACLSEARCH_USERNAME']
DEFAULT_PASSWORD = configs['ACLSEARCH_PASSWORD']

def get_aclsearch_token():
	aclsearch_uri =''
	api_payload = {
	'username': DEFAULT_USERNAME,
	'password': DEFAULT_PASSWORD,
	}
	api_headers = {
	'Content-Type':'application/json'
	}
	response = requests.post(aclsearch_uri,data = json.dumps(api_payload),headers = api_headers)
	json_data = json.loads(response.text)
	token = json_data['body']['token']
	return(token)

def remove_duplicates(sites):
	final_list = []
	for site in sites:
		if site not in final_list:
			final_list.append(site)
	return final_list

def lookup(srcIp,destIp,port,protocol):
	token= get_aclsearch_token()
	headers={
	    "Content-Type": "application/json",
        "Authorization": "Bearer {}".format(token),
	}
	
	search_url='<>?srcip=%s&dstip=%s&dstport=%s' %(srcIp,destIp,port) 
	response= requests.get(search_url, headers= headers)
	result = response.content 
	parsed = json.loads(result)
	sites = []
	rules = []
	ports = []
	count_ip = 0
	count_tcp = 0
	count_udp = 0
	for key, value in parsed.items():
		for attributes in value:
			if re.search('any',attributes['srcip']) and re.search('any',attributes['dstip']):
				pass
				
			elif attributes['dstport'] =='ip':
				count_ip=count_ip + 1
				if count_ip >=1:
					rules.append(attributes['rawrule'])
					sites.append(key)
					ports.append("ALL PORTS")
			elif count_ip<1 or re.search('autogen',attributes['dstipref']) or re.search('autogen',attributes['srcipref']) and protocol.lower == 'tcp':
				if re.search('tcp',attributes['dstport']) or re.search('tcp',attributes['srcport']):
					count_tcp=count_tcp + 1
					if count_tcp >=1:
						if key == 'ACL106':
							pass
						else:
							rules.append(attributes['rawrule'])
							sites.append(key)
						try:
							ports.append(attributes['dstportref'])
						except KeyError:
							pass
						ports.append(attributes['dstport'])
			elif count_ip<1 or re.search('autogen',attributes['dstipref']) or re.search('autogen',attributes['srcipref']) and protocol.lower == 'udp':
				if re.search('udp',attributes['dstport']) or re.search('udp',attributes['srcport']):
					count_udp=count_udp +1
					if count_udp >=1:
						if key == 'ACL106':
							pass
						else:
							rules.append(attributes['rawrule'])
							sites.append(key)
						try:
							ports.append(attributes['dstportref'])
						except KeyError:
							pass
						ports.append(attributes['dstport'])

	if count_ip>=1 or count_tcp>=1 or count_udp>=1:
		acl_sites=remove_duplicates(sites)
		acl_rules =remove_duplicates(rules)
		srv_ports = remove_duplicates(ports)

		for location in acl_sites:
			pass
		return acl_sites

	elif count_ip==0 and count_tcp==0 and count_udp==0:
		return ['Not Open']
		

if __name__== "__main__":
	sys.exit()





