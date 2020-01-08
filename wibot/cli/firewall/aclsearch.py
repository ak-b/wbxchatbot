import click
import requests
import os
import json
import re
import string
from wibot.cli.firewall.aclsearch_token import get_aclsearch_token as get_token
from wibot.cli.firewall.aclsearch_token import remove_duplicates


@click.group(help='ACL search')
def aclsearch():
	pass

@aclsearch.command(help = 'Returns ACL search results')
@click.argument('srcip')
@click.argument('destip')
@click.argument('port')
@click.argument('protocol')
def lookup(srcip,destip,port,protocol):
	token= get_token()
	#print(token)
	headers={
	    "Content-Type": "application/json",
        "Authorization": "Bearer {}".format(token),
	}
	search_url='http://10.252.252.247/fwsearchproxy?srcip=%s&dstip=%s&dstport=%s' %(srcip,destip,port) 
	#print(search_url)
	response= requests.get(search_url, headers= headers)
	#print(response)
	result = response.content 
	parsed = json.loads(result)
	sites = []
	count_ip = 0
	count_tcp = 0
	count_udp = 0
	for key, value in parsed.items():
		for attributes in value:
			if re.search('any',attributes['srcip']) or re.search('any',attributes['dstip']):
				pass
			elif attributes['dstport'] =='ip':
				count_ip=count_ip + 1
				if count_ip >=1:
					#print(attributes['rawrule'])
					sites.append(key)
			elif count_ip<1 or re.search('autogen',attributes['dstipref']) or re.search('autogen',attributes['srcipref']) and protocol.lower == 'tcp':
				if re.search('tcp',attributes['dstport']) or re.search('tcp',attributes['srcport']):
					count_tcp=count_tcp + 1
					if count_tcp >=1:
						#print(attributes['rawrule'])
						sites.append(key)
			elif count_ip<1 or re.search('autogen',attributes['dstipref']) or re.search('autogen',attributes['srcipref']) and protocol.lower == 'udp':
				if re.search('udp',attributes['dstport']) or re.search('udp',attributes['srcport']):
					count_udp=count_udp +1
					if count_udp >=1:
						#print(attributes['rawrule'])
						sites.append(key)

	if count_ip>=1 or count_tcp>=1 or count_udp>=1:
		acl_sites=remove_duplicates(sites)
		print("ACL exists in site/s:")
		for location in acl_sites:
			print(location)
	elif count_ip==0 and count_tcp==0 and count_udp==0:
		print("ACL doesn't exist")