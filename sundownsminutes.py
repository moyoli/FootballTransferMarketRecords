import bs4
import requests
from bs4 import BeautifulSoup
import pandas as pd
headers2 = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}
page2 = "https://www.transfermarkt.co.uk/mamelodi-sundowns-fc/leistungsdaten/verein/6356"
pageTree2 = requests.get(page, headers=headers)
pageSoup2 = BeautifulSoup(pageTree2.content, 'html.parser')
Players2 = pageSoup2.find_all("a", {"class": "spielprofil_tooltip"})
Values2 = pageSoup2.find_all("td", {"class": "rechts"})
Players2List = []
Values2List = []
for i in range(0, 25):
    PlayerList.append(Players[i].text)
    MinutesList.append(Values[i].text)
players_df = pd.DataFrame({"Players": PlayerList, "Values": MinutesList})
players_df.head()