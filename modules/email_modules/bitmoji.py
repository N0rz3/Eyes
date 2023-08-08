import random
from lib.requests import Requests
from lib.agents import user_agent
from lib.text import *


async def bitmoji(email):
    URL = "https://bitmoji.api.snapchat.com/api/user/find"

    headers = {
        'user-agent': random.choice(user_agent())
    }

    data = {
        'email': email
    }

    try:
        r = await Requests(URL, headers=headers, data=data).post()
    
        if '{"account_type":"snapchat"}' in r.text:
                return f"""\r✔️ {GREEN}Bitmoji{WHITE}\n"""

        else:
                return f"""\r❌ {RED}Bitmoji{WHITE}\n""" 

    except Exception:   
        return """\r🚧 Bitmoji\n"""