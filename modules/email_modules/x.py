from lib.agents import user_agent
from lib.requests import Requests
from lib.text import *
import random, json

# Twitter 

async def x(email):
    URL = "https://api.twitter.com/i/users/email_available.json?email={}"

    headers = {
        "user-agent": random.choice(user_agent())
    }

    try:
        r = await Requests(URL.format(email), headers).get()

        read = json.load(r)

        if read['taken'] == True:
                return f"""\r✔️ {GREEN}X (Twitter){WHITE}\n"""

        else:
                return f"""\r❌ {RED}X (Twitter){WHITE}\n"""

    except Exception:
        return """\r🚧 X (Twitter)\n"""