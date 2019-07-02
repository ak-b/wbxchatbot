# -*- coding: utf-8 -*-

"""Console script for wisnow."""
from wisnow import wisnow
import pysnow
import click
import requests
import datetime
import os
from wiutil.pprint import print_table

DEFAULT_USERNAME = os.environ.get('SNOW_USERNAME')
DEFAULT_PASSWORD = os.environ.get('SNOW_PASSWORD')
DEFAULT_URL = os.environ.get('SNOW_SAML_URL')
DEFAULT_INSTANCE = os.environ.get('SNOW_INSTANCE')


@click.group(help='ServiceNow API commands')
def snow():
    pass


@snow.command(help="Fetches closed changes from a specific date (YYYY-MM-DD. Default - today.")
@click.argument('timestamp', required=False)
def changes(timestamp):
    e = wisnow.ESPToken(DEFAULT_INSTANCE, DEFAULT_URL, DEFAULT_USERNAME, DEFAULT_PASSWORD)
    token = e.get_token()

    s = requests.session()
    headers = {
        "accept": "application/json;charset=utf-8",
        "Authorization": "Bearer {}".format(token)
    }
    s.headers = headers

    if timestamp is None:
        time_end = datetime.datetime.today().replace(hour=23, minute=59)
    else:
        time_end = datetime.datetime.strptime(timestamp, '%Y-%m-%d').replace(hour=23, minute=59)
    time_start = (time_end - datetime.timedelta(days=1)).replace(hour=0, minute=0)

    qb = (
        pysnow.QueryBuilder()
        .field('state').equals('4')
        .AND()
        .field('sys_updated_on').between(time_start, time_end)
    )

    client = pysnow.Client(instance=e.instance, session=s)
    change = client.resource(api_path='/table/change_request')
    response = change.get(qb)

    print(response.all())

    output = list()
    for entry in response.all():
        node = {'Entry number': entry['number'], 'Closed at': entry['closed_at'],
                'Description': entry['short_description']}
        output.append(node)

    print_table(output)


@snow.command(help="Fetches incidents for a specified date (YYYY-MM-DD). Default - today.")
@click.argument('timestamp', required=False)
def incidents(timestamp):
    e = wisnow.ESPToken(DEFAULT_INSTANCE, DEFAULT_URL, DEFAULT_USERNAME, DEFAULT_PASSWORD)
    token = e.get_token()

    s = requests.session()
    headers = {
        "accept": "application/json;charset=utf-8",
        "Authorization": "Bearer {}".format(token)
    }
    s.headers = headers

    if timestamp is None:
        time_end = datetime.datetime.today().replace(hour=23, minute=59)
    else:
        time_end = datetime.datetime.strptime(timestamp, '%Y-%m-%d').replace(hour=23, minute=59)
    time_start = (time_end - datetime.timedelta(days=1)).replace(hour=0, minute=0)

    qb = (
        pysnow.QueryBuilder().field('sys_created_on').between(time_start, time_end)
    )

    client = pysnow.Client(instance=e.instance, session=s)
    incident = client.resource(api_path='/table/incident')
    response = incident.get(query=qb)

    output = list()
    for entry in response.all():
        node = {'Entry number': entry['number'], 'Created at': entry['sys_created_on'],
                'Resolved at': entry['resolved_at'],
                'Description': entry['short_description']}
        output.append(node)

    print_table(output)
