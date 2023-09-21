from lib.agents import user_agent
from lib.requests import Requests
from lib.text import *
import random


async def mailru(email):
    URL = "https://account.mail.ru/api/v1/user/exists?email={}"

    headers = {
        'user-agent': random.choice(user_agent())
    }

    try:
        r = await Requests(URL.format(email), headers).get()

        try:
            if r.json()['body']['exists'] == True:
                return f"✔️ {GREEN}Mail.ru{WHITE}\n"

            else:
                return f"""❌ {RED}Mail.ru{WHITE}\n"""
        except:
            return f"{RED}❌ Mail.ru{WHITE}\n"

    except Exception:
        return """\r🚧 Mail.ru\n"""
