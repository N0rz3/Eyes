from lib.agents import user_agent
from lib.requests import Requests
import random
from lib.text import *


async def instagram(email):
    URL = "https://www.instagram.com/web/search/topsearch/?context=blended&query={}"

    headers = {
        'user-agent': random.choice(user_agent()),
    }

    try:
        r = await Requests(URL.format(email), headers).get()

        if r.status_code == 200:
            try:
                data = r.json()
                users = data.get('users', [])

                if not users:
                    print(f"\r❌ {RED}Instagram{WHITE}\n")
                else:
                    user_info = users[0].get('user', {})

                    username = user_info.get('username', '')
                    profile_pic_url = user_info.get('profile_pic_url', '')

                    if username and profile_pic_url:
                        print(f"""\r✔️ {GREEN}Instagram{WHITE}
    ├──Username: {username}
    └──Profile Picture: {profile_pic_url}\n""")
                    else:
                        print(f"\r❌ {RED}Instagram{WHITE}\n")

            except Exception:
                print(f"\r❌ {RED}Instagram{WHITE}\n")

    except Exception:
        print("\r🚧 Instagram\n")
