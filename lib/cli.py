import argparse
from .banner import *
from output import eyes_output
from .check_version import check_python_version


async def parser():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        'email',
        nargs='?',
        type=str,
        default=None,
        help='search information on the target email with modules, services...'
    )
    parser.add_argument(
        '-m', '--modules',
        action='store_true',
        help='gives you all the email modules used by Eyes'
    )

    args = parser.parse_args()

    if args.email:
        check_python_version()
        print(banner2)

        await eyes_output(args.email)
        exit()

    if args.modules:
        print(banner2)
        print(f"""
{YELLOW}[{GREEN}*{YELLOW}] 👀 Email modules : {WHITE}
 ├──{CYAN}Duolingo{WHITE}        # scrapable
 ├──{CYAN}GitHub{WHITE}          # scrapable
 ├──{CYAN}Gravatar{WHITE}        # scrapable
 ├──{CYAN}Imgur{WHITE}
 ├──{CYAN}Mail.ru{WHITE}
 ├──{CYAN}Pastebin{WHITE}        # links dump
 ├──{CYAN}Protonmail{WHITE}      # scrapable
 ├──{CYAN}Bitmoji{WHITE}
 ├──{CYAN}Instagram{WHITE}
 └──{CYAN}X (Twitter){WHITE}
""")
        exit()

    else:
        print(banner)
        exit()
