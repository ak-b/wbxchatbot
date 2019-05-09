# -*- coding: utf-8 -*-
import os

"""Top-level package for wibot."""

__author__ = """Vishal Patil"""
__email__ = 'vpatil3@cisco.com'
__version__ = '0.1.0'

BOT_NAME = os.environ.get('BOT_NAME')
BOT_TOKEN = os.environ.get('BOT_TOKEN')
BOT_AUTH_HEADER = {
    'authorization': "Bearer {}".format(BOT_TOKEN),
    'content-type': "application/json",
    'cache-control': "no-cache",
}

SOLIDFIRE_USERNAME = os.environ.get('SOLIDFIRE_USERNAME')
SOLIDFIRE_PASSWORD = os.environ.get('SOLIDFIRE_PASSWORD')

NETAPP_USERNAME = os.environ.get('NETAPP_USERNAME')
NETAPP_PASSWORD = os.environ.get('NETAPP_PASSWORD')

PURE_USERNAME = os.environ.get('PURE_USERNAME')
PURE_PASSWORD = os.environ.get('PURE_PASSWORD')

JIRA_USERNAME = os.environ.get('JIRA_USERNAME')
JIRA_PASSWORD = os.environ.get('JIRA_PASSWORD')
