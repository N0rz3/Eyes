from lib.agents import user_agent
from lib.requests import Requests
from lib.text import *
import random


async def duolingo(email):
    URL = "https://www.duolingo.com/2017-06-30/users"

    headers = {
        'user-agent': random.choice(user_agent())
    }

    params = {
        'email': email
    }

    try:
        r = await Requests(URL, params=params, headers=headers).get()
    

        if """{"users":[]}""" in r.text:
                return f"""\r❌ {RED}Duolingo{WHITE}\n"""


        else:
                    return f"""\r✔️ {GREEN}Duolingo{WHITE}
    ├──Name : {r.json()['users'][0]['username']}
    ├──Bio : {r.json()['users'][0]['bio']}
    ├──Total XP : {r.json()['users'][0]['totalXp']}
    └──From Language : {r.json()['users'][0]['courses'][0]['fromLanguage']}\n"""

    except Exception:
        return """\r🚧 Duolingo"""