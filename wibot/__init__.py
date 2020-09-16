# -*- coding: utf-8 -*-
import os

"""Top-level package for wibot."""

# editing package used by wibot : akbansal
from wibot.utils import get_config

configs = get_config()
BOT_NAME = configs['BOT_NAME']
BOT_TOKEN = configs['BOT_TOKEN']

BOT_AUTH_HEADER = {
    'authorization': "Bearer {}".format(BOT_TOKEN),
    'content-type': "application/json",
    'cache-control': "no-cache",
}
