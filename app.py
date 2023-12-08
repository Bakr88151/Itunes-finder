import sys
from colorama import Fore, Style
import json
import requests

if len(sys.argv) > 2:
    print(Fore.RED + 'Too many arguments' + Style.RESET_ALL)
    sys.exit(1)
elif len(sys.argv) < 2:
    print(Fore.RED + 'Too few arguments' + Style.RESET_ALL)
else:
    search = sys.argv[1]

search.replace(" ", '+')

res = requests.get(f"https://itunes.apple.com/search?term={search}").json()

if res['resultCount'] == 0:
    print("No results found!")
else:
    for item in res['results']:
        try:
            print(item['trackName'])
        except KeyError:
            pass
