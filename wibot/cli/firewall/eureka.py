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
	aclsearch_uri ='http://10.252.252.247/user-management/login'
	#print(DEFAULT_USERNAME)
	#print(DEFAULT_PASSWORD)
	api_payload = {
	'username': DEFAULT_USERNAME,
	'password': DEFAULT_PASSWORD,
	}
	api_headers = {
	'Content-Type':'application/json'
	}
	response = requests.post(aclsearch_uri,data = json.dumps(api_payload),headers = api_headers)
	json_data = json.loads(response.text)
	#print(json_data)
	token = json_data['body']['token']
	#print(token)
	return(token)

def remove_duplicates(sites):
	final_list = []
	for site in sites:
		if site not in final_list:
			final_list.append(site)
	return final_list

def lookup(srcIp,destIp,port,protocol):
#def lookup(destIp,port,protocol):
	token= get_aclsearch_token()
	headers={
	    "Content-Type": "application/json",
        "Authorization": "Bearer {}".format(token),
	}
	#search_url='http://10.252.252.247/fwsearchproxy/fwsearchproxy?dstip=%s&dstport=%s' %(destIp,port) 
	search_url='http://10.252.252.247/fwsearchproxy/fwsearchproxy?srcip=%s&dstip=%s&dstport=%s' %(srcIp,destIp,port) 
	#print(search_url)
	response= requests.get(search_url, headers= headers)
	#print("Request Response Code")
	#print(response.status_code)
	result = response.content 
	parsed = json.loads(result)
	#print(parsed.items())
	sites = []
	rules = []
	ports = []
	count_ip = 0
	count_tcp = 0
	count_udp = 0
	for key, value in parsed.items():
		for attributes in value:
			#print(attributes)
			#made one change or to and to filter for internet based ACLs
			#if re.search('any',attributes['srcip']) or re.search('any',attributes['dstip']):
			if re.search('any',attributes['srcip']) and re.search('any',attributes['dstip']):
				pass
				
			elif attributes['dstport'] =='ip':
				count_ip=count_ip + 1
				if count_ip >=1:
					#print(attributes['rawrule'])
					rules.append(attributes['rawrule'])
					sites.append(key)
					ports.append("ALL PORTS")
			elif count_ip<1 or re.search('autogen',attributes['dstipref']) or re.search('autogen',attributes['srcipref']) and protocol.lower == 'tcp':
				if re.search('tcp',attributes['dstport']) or re.search('tcp',attributes['srcport']):
					count_tcp=count_tcp + 1
					if count_tcp >=1:
						#print(attributes['rawrule'])
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
						#print(attributes['rawrule'])
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
		#print(rules)
		acl_rules =remove_duplicates(rules)
		srv_ports = remove_duplicates(ports)
		#print(acl_rules)
		#print("ACL exists in sites:")
		#print("==========")
		for location in acl_sites:
			#print(location)
			pass
		return acl_sites

	elif count_ip==0 and count_tcp==0 and count_udp==0:
		#print("ACL doesn't exist")
		return ['Not Open']
	
	#print(json.dumps(parsed, indent=2, sort_keys= True))
	

if __name__== "__main__":
	sys.exit()





