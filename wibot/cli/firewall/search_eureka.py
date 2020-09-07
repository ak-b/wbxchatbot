import click
import requests
import os
import json
import re
import string
from tabulate import tabulate
from wibot.cli.firewall.eureka import lookup

@click.group(help="Search if Eureka Ports are Open")
def search_eureka():
	pass
@search_eureka.command(help= "Search if Eureka Ports are Open")
@click.argument('subnet')
def search_eureka(subnet):
	print("***********************************************************")
	print("Mapping NS FW Eureka Template for subnets in STAP.WEBEX.COM")
	print("***********************************************************")
	template = {'tcp':[],'udp':[]}
	print(template)
	print("\nFirewalls with an ACL(/s) allowing internet to webex access for Eureka\n")
	flat_list = []
	another_list = []
	table_templ=[]
	table_templ.append([str(subnet)])
	for key,value in template.items():
		for port in value:
			table_templ.append(lookup('0.0.0.0/0',subnet,port,key))
	flat_list=[item for sublist in table_templ for item in sublist]
	another_list.append(flat_list)
	print(tabulate(another_list, headers = ['SUBNET','TCP','UDP']))
