#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7857373076:AAEc1bRSxPtIkwBZ6MjONfw9qCyOyDhAEKo")
    API_ID = int(os.environ.get("API_ID", "27333723"))
    API_HASH = os.environ.get("API_HASH", "e6bb00b44401cf8ac9f3fc83dd38b7cc")
    AUTH_USERS = "1411895712"

