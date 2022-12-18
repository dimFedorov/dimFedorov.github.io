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

with open("games.json", encoding='utf-8') as outfile:
    jsonGames = json.load( outfile )
    

    
with open("seasons.json", encoding='utf-8') as outfile:
    jsonSeasons = json.load( outfile )
    
    print( jsonSeasons )