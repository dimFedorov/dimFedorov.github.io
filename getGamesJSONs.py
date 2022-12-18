# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 16:16:00 2022

@author: quasi
"""

import os
from bs4 import BeautifulSoup
import json




def stripDzrName (s) :
    return s.strip().replace('«','').replace('»','')

def isLite (s):
    return 'Лайт' in s

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
game_id = 1

while game_id < 529 :

    
    html_path = os.path.join(os.getcwd(),f'game{game_id}',f'game{game_id}.html')
    
    if os.path.isfile(html_path):
    
        with open(html_path,encoding='utf-8') as output_file:
            soup = BeautifulSoup(output_file,'html.parser')
            
        game={
              'id':game_id,
              'name': stripDzrName( soup.find('h1',{'id':'game-Title'}).string ),
              'type': '',
              'teams':[]
              }
        
        if isLite(game['name']):
            game['type'] = 'lite'
        else :
            game['type'] = 'hard'
            
            
        trs = soup.find('table',{'id':'suxx'}).find_all('tr')
        
        place = 0
        for team in trs :
            if team.has_attr('id'):
                continue
            place += 1
            aName = team.find('a',{'id':'tmname'})           
            time = team.find('td',{'id':'fulltime'})
            if time == None :
                 time = team.find('td',{'id':'vz'})
                 aName = team.find('a',{'id':'vz'})
                       
            try :
                team = {
                    'name': aName.string.strip(),
                    'id': aName['href'].split('=')[-1],
                    'place': place,
                    'time': time.string.strip()
                    }
            except :
                team = {
                    'name': aName('span')[0].string.strip(),
                    'id': aName['href'].split('=')[-1],
                    'place': place,
                    'time': time.string.strip()
                    }
    
            game['teams'].append(team)
            
        games.append(game)
        print(str(game_id) + " - " + games[-1]['teams'][0]['name'])
    
        json_path = os.path.join(os.getcwd(),'json Games',f'game{game_id}.json')
        with open(json_path,'w',encoding='utf-8') as json_file:
            json_file.write( json.dumps(game, ensure_ascii=False, indent=4) )
    
    
    game_id += 1
    
        
    

        
    
