from lib.agents import user_agent
from lib.requests import Requests
import random
from lib.text import *
from lib import venom
from lib.image import get_hashed, fetch_img

async def github(email):
        URL = "https://api.github.com/search/users?q={}+in:email"

        headers = {
            'user-agent': random.choice(user_agent()),
            # optional but better results 'authorization': 'token YOUR_API_TOKEN'
        }

        try:
            r = await Requests(URL.format(email), headers).get()

            if '"total_count": 0' in r.text:
                print(f"""\r❌ {RED}GitHub{WHITE}\n""")

            else:
                try:
                    items = r.json()['items']
                    if not items:
                        pass

                    name = items[0]['login']
                    avatar = items[0]['avatar_url']

                    default = "https://github.com/identicons/{}.png".format(name)

                    img = await fetch_img(avatar)
                    img_hashed = get_hashed(img)

                    default_img = await fetch_img(default)
                    deufault_hashed = get_hashed(default_img)

                    if img_hashed == deufault_hashed:
                        print(f"""\r✔️ {GREEN}GitHub{WHITE}
    ├──Name : {name}
    └──Avatar : {avatar}
       └──✖️ Default profile picture\n""")

                    else:
                        print(f"""\r✔️ {GREEN}GitHub{WHITE}
    ├──Name : {name}
    └──Avatar : {avatar}
       └──🤳 No default profile picture\n""")

                        await venom.Face.facial(url=avatar, name=name, output_path=f"facial_recognition/venom_output_{name}.jpg")


                except Exception:
                    print(f"""\r❌ {RED}GitHub{WHITE}\n""")
        except Exception:
            print("\r🚧 GitHub\n")