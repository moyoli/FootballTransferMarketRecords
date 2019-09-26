import bs4
import requests
from bs4 import BeautifulSoup
import pandas as pd
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}
page = "https://www.transfermarkt.co.uk/transfers/transferrekorde/statistik/top/plus/0/galerie/0?saison_id=2019"
pageTree = requests.get(page, headers=headers)
pageSoup = BeautifulSoup(pageTree.content, 'html.parser')
Players = pageSoup.find_all("a", {"class": "spielprofil_tooltip"})
Values=pageSoup.find_all("td", {"class": "rechts hauptlink"})
PlayersList = []
ValuesList = []
for i in range(0, 25):
    PlayersList.append(Players[i].text)
    ValuesList.append(Values[i].text)

players_df = pd.DataFrame({"Players": PlayersList, "Values": ValuesList})
players_df.head()