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
