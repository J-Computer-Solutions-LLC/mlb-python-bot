from __future__ import print_function
import json
import datetime
import mlbgame

with open('test.json') as f:
    data = json.load(f)

def get_games(data):
    games = len(data['games'])
    return games

def parse_json(data):
    predictions = []
    for item in data['games']:
        prediction = {}
        prediction['Away_Team'] = item['teams']['away']['name']
        prediction['Home_Team'] = item['teams']['home']['name']
        prediction['gameID'] = item['gamePk']
        print(prediction)
        predictions.append(prediction)
    return predictions

def print_team_stats(predictions):
    for prediction in predictions:
        stats = mlbgame.players(prediction['gameID'])
        print(stats)
        
    
        
        #for stats in item['stats']['wpa']['gameWpa']:

    
print(get_games(data))
predictions = parse_json(data)
print_team_stats(predictions)