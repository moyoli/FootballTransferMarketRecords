import bs4
import requests
from bs4 import BeautifulSoup
import pandas as pd
headers_sun = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) '
                             'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}
page_sun = "https://www.transfermarkt.co.uk/mamelodi-sundowns-fc/leistungsdaten/verein/6356"
pageTree_sun = requests.get(page_sun, headers=headers_sun)
pageSoup_sun = BeautifulSoup(pageTree_sun.content, 'html.parser')
Players_sun = pageSoup_sun.find_all("a", {"class": "spielprofil_tooltip"})
Minutes_sun = pageSoup_sun.find_all("td", {"class": "rechts"})
PlayersList_sun = []
MinutesList_sun = []
for i in range(0, 25):
    PlayersList_sun.append(Players_sun[i].text)
    MinutesList_sun.append(Minutes_sun[i].text)
players_df_sun = pd.DataFrame({"Players": PlayersList_sun, "Values": MinutesList_sun})
players_df_sun.head()