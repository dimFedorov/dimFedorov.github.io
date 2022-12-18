# -*- coding: utf-8 -*-
"""
Created on Sat Dec 17 16:28:57 2022

@author: quasi
"""

import json 
from bs4 import BeautifulSoup

team_id = 712


with open('indexSeasons.html',encoding='utf-8') as index_file :
    indexFile = index_file.read()

  
indexSoup = BeautifulSoup(indexFile,'html.parser')

with open (f'team{team_id}.json',encoding='utf-8') as json_file :
    json_stat = json.load(json_file)

print( json_stat[0]['name'] )

gamesPlayed = 0
wins = 0
podiums = 0

for game in season['games']:
    if game == '':
        continue
    gamesPlayed += 1
    if int(game) > 90:
        author += 1
        authorPts += int(game)
    elif int(game) > 79 :
        podiums += 1
        if int(game) ==90:
            wins += 1


print('===== Summary =====')


                
# with open (f'team{team_id}.json',encoding='utf-8') as json_file :
#     json_stat = json.load(json_file)
