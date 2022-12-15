# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 16:16:00 2022

@author: quasi
"""

import os
from bs4 import BeautifulSoup
import json


def stripDzr (s) :
    return s.split('\n')[1].strip()

def convertDzrDate(s) :
    s = stripDzr(s)
    date = s.split(' ')
    day = date[0]
    month = date[1]
    year = date[2]
    monthes = { 'января': "01", 'февраля': "02", 'марта': "03", 'апреля': "04",
               'мая': "05", 'июня': "06", 'июля': "07", 'августа': "08",
               'сентября': "09", 'октября': "10", 'ноября': "11", 'декабря': "12"
        }

    return year + '-' + monthes[month] + '-' + day

games = []

hostDir = os.getcwd()
for gameFolder in os.walk(hostDir):

    if -1 == gameFolder[0].find('game') :
        continue;
    
    for fileName in gameFolder[2]:
        
        if -1 == fileName.find('game') :
            continue;
            
        with open( os.path.join(hostDir, gameFolder[0],fileName),encoding='utf-8' ) as file:

            soup = BeautifulSoup(file, "html.parser")
            gameid = int(fileName.strip('game').split('.')[0])
            game_Name = stripDzr(soup.find('h1',{'id':'game-Title'}).text)
            game_Name = game_Name.replace('«','').replace('»','')
            game_date = convertDzrDate(soup.find('div',{'id':'date'}).text)
            game = {
                'name' : game_Name,
                'id': gameid,
                'link' : './game' + str(gameid) + '/' + fileName,
                'date' : game_date
                }
            games.append(game)
            

json_object = json.dumps(games,ensure_ascii=False).encode('utf-8')

with open("games.json", "w", encoding='utf-8') as outfile:
    outfile.write(json_object.decode())