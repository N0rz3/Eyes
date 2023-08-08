from modules.email_modules import duolingo, gravatar, imgur, protonmail, bitmoji, x, github, mailru, pastebin
from lib.text import WHITE, CYAN
from lib.maileye import decomp, regex_check


async def eyes_output(email):
    past = 0
    print("#" * 15 + CYAN + email + WHITE + "#" * 15 + "\n")

    regex_check(email)

    name, domain = decomp(email)
    print(f"-🙋 Name : {name}")
    print(f"-🔎 Domain : {domain}\n")

    print(await protonmail.protonmail(email))
    print(await mailru.mailru(email))
    print(await duolingo.duolingo(email))
    print(await gravatar.gravatar(email))
    print(await imgur.imgur(email))
    print(await bitmoji.bitmoji(email))
    print(await x.x(email))
    await github.github(email)
    print("[~] Paste :")
    for paste in await pastebin.pastebin(email):
        past += 1
        print("    ├──"+paste.replace('/raw', ''))
    if past == 0:
        print("[-] No paste found.")
    else:
        pass