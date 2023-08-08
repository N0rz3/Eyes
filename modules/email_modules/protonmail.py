from lib.agents import user_agent
from lib.requests import Requests
from lib.text import *
import random
import re
from datetime import datetime

async def protonmail(email):
    URL = "https://api.protonmail.ch/pks/lookup?op=index&search={}"

    headers = {
        'user-agent': random.choice(user_agent())
    }

    try:
        r = await Requests(URL.format(email), headers=headers).get()

        if "info:1:0" in r.text:
            return f"\r❌ {RED}ProtonMail{WHITE}\n"

        elif "info:1:1" in r.text:
            pat1 = "2048:(.*)::"
            pat2 = "22::(.*)::"
            pat3 = "4096:(.*)::"

            regex_pat = [pat1, pat2, pat3]

            for regex in regex_pat:
                timestamp = re.search(regex, r.text)
                if timestamp:
                    dtimeobject = datetime.fromtimestamp(int(timestamp.group(1)))
                    return f"""\r✔️ {GREEN}ProtonMail{WHITE}
    └──Date of creation : {dtimeobject} 🌐 (UTC) \n"""
                else:
                    continue

        else:
            return f"\r❌ {RED}ProtonMail{WHITE}\n"

    except Exception:
        return "\r🚧 ProtonMail\n"