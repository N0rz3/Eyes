import re
from .text import *

EMAIL_REGEX = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+.[a-zA-Z0-9-.]+$"

def decomp(email: str):
    name = email.split('@')[0]
    domain = email.split('@')[1]

    return name, domain

def regex_check(email):
    if re.match(EMAIL_REGEX, email):
        print(f"{GREEN}[+] Email valid !{WHITE}")

    else:
        print("[-] Email not valid !")
        exit()