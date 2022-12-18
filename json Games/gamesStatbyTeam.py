# -*- coding: utf-8 -*-
"""
Created on Sun Dec 18 08:06:26 2022

@author: quasi
"""

import json
import os
import math

with open('games.json', encoding='utf-8') as json_game_file:
    json_all_games = json.loads( json_game_file.read() )

def getGameDate(gameId) :
    for game in json_all_games:
        if int(game['id']) == int(gameId):
            return game['date']

def getTimeGap(leadTime, teamTime):
    l = leadTime.split(':')
    t = teamTime.split(':')
    lSeconds = int(l[0])*3600 + int(l[1])*60 + int(l[2])
    tSeconds = int(t[0])*3600 + int(t[1])*60 + int(t[2])
    gSeconds = tSeconds - lSeconds
    gS = gSeconds%60
    gM = int( (gSeconds - gS)/60%60 )
    gH = math.floor(gSeconds/3600)    
    
    return f'{gH}h {gM}m {gS}s'
    
    

def printFirstGame (teamID):
    game_id = 1
    
    
    while game_id < 529 :
        file_name = f'game{game_id}.json'
        if not os.path.isfile(file_name):
            game_id += 1
            continue
        
        with open(file_name, encoding='utf-8') as json_game_file:
            json_game = json.loads( json_game_file.read() )
                    
        leader_time = json_game['teams'][0]['time']
        
        for team in json_game['teams']:
            if int( team['id'] ) == int(teamID):
                time_gap = getTimeGap(leader_time, team['time'])
                print( f'The first game of \"{team["name"]}\" is ' )
                print( json_game['name'] )
                print( getGameDate(json_game['id']) )
                print(f'Result: {team["place"]} place in {time_gap} behind a winner')
                return
        
        game_id += 1
    

printFirstGame(82)
