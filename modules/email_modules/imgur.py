from lib.agents import user_agent
from lib.requests import Requests
from lib.text import *
import random


async def imgur(email):
    URL = "https://imgur.com/signin/ajax_email_available"

    headers = {
        'user-agent': random.choice(user_agent())
    }

    data = {
        'email': email
    }

    try:
        r = await Requests(URL, headers, data).post()

        if """{"data":{"available":false},"success":true,"status":200""" in r.text:
            return f"""\r✔️ {GREEN}Imgur{WHITE}\n"""

        else:
            return f"""\r{RED}❌ Imgur{WHITE}\n"""

    except Exception:
        return """\r🚧 Imgur\n"""
