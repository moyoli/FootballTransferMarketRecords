from lxml import html
import requests
import pandas as pd
import numpy as np
import re
#take site and structure html
page = requests.get('https://www.premierleague.com/clubs')
tree = html.fromstring(page.content)
#using page's css classes, extract all links pointing to a team
linkLocation = tree.cssselect('.indexItem')
#create an empty list for us to send each team's link to
teamLinks = []
#For each link
for i in range(0, 20):
    #...find the page the link is going to...
    temp = linkLocation[i].attrib['href']
    #...add the link to the website domain..
    temp = "https://www.premierleague.com/" + temp
    #...change link text so it ponts to squad list not page overview
    temp = temp.replace("overview", "squad")
    #...add the finished link to our Teamlinks list
    teamLinks.append(temp)

#create empty lists for player links
playerLink1 = []
playerLink2 = []
#for each team link page
for i in range(len(teamLinks)):
    #download team page and process html code
    squadPage = requests.get(teamLinks[i])
    squadTree = html.fromstring(squadPage.content)
    #extract player links
    playerLocation = squadTree.cssselect('.playerOverviewCard')
    #for each player link within the team page
    for i in range(len(playerLocation)):
        #save the link, complete with domain
        playerLink1.append("http://www.premierleague.com/" + playerLocation[i].attrib['href'])
        #for second link, change the page from player overview to stats
        playerLink2.append(playerLink1[i].replace("overview", "stats"))
#Create lists for each variable
Name = []
Team = []
Age = []
Apps = []
HeightCM = []
WeightKG = []
#Populate lists with each player
for i in range(len(playerLink1)):
    playerPage1 = requests.get(playerLink1[i])
    playerTree1 = html.fromstring(playerPage1.content)
    playerPage2 = requests.get(playerLink2[i])
    playerTree2 = html.fromstring(playerPage2.content)
    tempName = str(playerTree1.cssselect('div.name')[0].text_content())
    try:
        tempTeam = str(playerTree1.cssselect('.table:nth-child(1) .long')[0].text_content())
    except IndexError:
        tempTeam = str("BLANK")
    try:
        tempAge = playerTree1.cssselect('.pdcol2 li:nth-child(1) .info')[0].text_content()
    except IndexError:
        tempAge = float('NaN')
    try:
        tempApps = playerTree2.cssselect('.statappearances')[0].text_content()
        tempApps = int(re.search(r'\d+', tempApps).group())
    except IndexError:
        tempApps = float('NaN')
    try:
        tempHeight = playerTree1.cssselect('.pdcol3 li:nth-child(1) .info')[0].text_content()
        tempHeight = int(re.search(r'\d+', tempHeight).group())
    except IndexError:
        tempHeight = float('NaN')
    try:
        tempWeight = playerTree1.cssselect('.pdcol3 li+ li .info')[0].text_content()
        tempWeight = int(re.search(r'\d+', tempWeight).group())
    except IndexError:
        tempWeight = float('NaN')
#Now that we have players full details, add them to the lists
Name.append(tempName)
Team.append(tempTeam)
Age.append(tempAge)
Apps.append(tempApps)
HeightCM.append(tempHeight)
WeightKG.append(tempWeight)

#Create data frame from the lists
df = pd.DataFrame({'Name':Name,
     'Team':Team,
     'Age':Age,
     'Apps':Apps,
     'HeightCM':HeightCM,
     'WeightKG':WeightKG})
#Show me top 3 rows:
df.head()
#Show me Karius height
df[df['Name']=="Loris Karius"]["HeightCM"]
#Export to CSV
df.to_csv("EPLData.csv")