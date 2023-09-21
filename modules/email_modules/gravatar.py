from lib.agents import user_agent
from lib.requests import Requests
from lib.text import *
import random


async def gravatar(email):
    URL = "https://en.gravatar.com/{}.json"

    headers = {
        'user-agent': random.choice(user_agent())
    }

    try:
        r = await Requests(URL.format(email), headers).get()

        if "User not found" in r.text:
            return f"""\r❌ {RED}Gravatar{WHITE}\n"""

        else:
            if r.json()['entry'][0]['displayName'] != None or '':
                return f"""\r{GREEN}✔️ Gravatar{WHITE}
    └──Name : {r.json()['entry'][0]['displayName']}
                    """

            else:
                return f"""\r{GREEN}✔️ Gravatar{WHITE}\n"""

    except Exception:
        return """\r🚧 Gravatar\n"""
