from lib.agents import user_agent
from lib.requests import Requests
from lib.text import *
import random

async def chess(email):
    URL = "https://www.chess.com/callback/email/exist?email={}"

    headers = {
        'user-agent': random.choice(user_agent())
    }

    r = await Requests(URL.format(email), headers).get()

    if r.status_code == 200:
        return f"\r{GREEN}✔️ Chess{WHITE}\n"

    elif r.status_code == 404:
        return f"\r{RED}❌ Chess{WHITE}\n"

    else:
        return f"\r{RED}❌ Chess{WHITE}\n"