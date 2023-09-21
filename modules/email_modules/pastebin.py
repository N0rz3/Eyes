"""
original code => https://github.com/KanekiWeb/Email-Osint/blob/main/modules/PastebinDump.py
"""
from ScrapeSearchEngine.SearchEngine import Google
from lib.requests import Requests


async def pastebin(email: str) -> list:
    search = ("site:pastebin.com \"{}\"".format(email))
    try:
        googleText, googleLink = Google(
            search=search, userAgent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")

        result_links = []

        for i in googleLink:
            try:
                link = str(i).replace("https://pastebin.com/",
                                      "https://pastebin.com/raw/")
                data = await Requests(link).get()

                if email.lower() in data.text.lower() or email in data.text or email.upper() in data.text.upper():
                    result_links.append(link)

            except:
                return ()

        return result_links

    except:
        return ()
