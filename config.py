#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6108435740:AAE_5IvUR2h07j3GJI9xCNyjAhJyaTqZ70Y")
    API_ID = int(os.environ.get("API_ID", "26178611"))
    API_HASH = os.environ.get("API_HASH", "93dd870eca0aebd9549775fdb97d3f61")
    AUTH_USERS = "5207969772"

