import requests
import json
import os
from wibot.utils import get_config 

configs = get_config()

DEFAULT_USERNAME = configs['ACLSEARCH_USERNAME']
DEFAULT_PASSWORD = configs['ACLSEARCH_PASSWORD']
#DEFAULT_USERNAME = os.environ.get('ACLSEARCH_USERNAME')
#DEFAULT_PASSWORD = os.environ.get("ACLSEARCH_PASSWORD")

def get_aclsearch_token():
	aclsearch_uri ='http://10.252.252.247/user-management/login'
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

if __name__== "__main__":
	get_aclsearch_token()
