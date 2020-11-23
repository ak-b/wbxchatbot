import click
from wibot import CONTEXT_SETTINGS


@click.group(context_settings=CONTEXT_SETTINGS, help="Documentation: docs -h")
def docs():
    pass


@docs.command(name="firewall-incident-triage", help="Firewall incident triage")
@click.argument("admin", nargs=1, required=False, type=bool)
def fw_incident_triage(admin):
    pass


@docs.command(name="misc", help="URL for test-systems")
@click.argument("admin", nargs=1, required=False, type=bool)
def misc(admin):
    pass


'''
import os
import requests
import pprint
import json
API_URL = "https://api.ciscospark.com/v1/messages"
MAX_MSG_SIZE = 4096
BOT_NAME = os.environ.get('BOT_NAME')
BOT_TOKEN = os.environ.get('BOT_TOKEN')
BOT_AUTH_HEADER = {
    'authorization': "Bearer {}".format(BOT_TOKEN),
    'content-type': "application/json",
    'cache-control': "no-cache",
}


def send_card_response(roomid: str, card_response: str):
    json_data = {
        'roomId': roomid,
        'markdown': 'x',
        'attachments': [json.loads(card_response)],
    }
    response = requests.request('POST', API_URL, json=json_data, headers=BOT_AUTH_HEADER)
    pprint.pprint(response.json())

'''