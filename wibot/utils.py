'''
Function file
'''
# tested and working fix

import requests
import os
import json

def get_config():
    '''
    To get credentials
    '''
    result = {}
    script_path = os.path.dirname(os.path.realpath('application.properties'))
    configfile = os.path.join(script_path,"application.properties")
    with open(configfile) as f:
        for l in f:
            if not l.startswith('#'):
                items = l.strip().split(':', 1)
                if len(items) == 2:
                    result[items[0].strip()] = items[1].split('#')[0].strip()
    if os.path.exists('/var/run/secrets/boostport.com/vault-token'):
        with open('/var/run/secrets/boostport.com/vault-token') as f:
            vault_data = json.loads(f.read())
        headers = {"X-Vault-Token": vault_data['clientToken']}
        url = "{}v1/iaas-marvin/vault/secrets".format(vault_data['vaultAddr'])
        response = requests.get(url, headers=headers)
        result.update(response.json()['data'])
    return result
