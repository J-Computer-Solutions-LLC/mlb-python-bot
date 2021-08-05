import json
import datetime

with open('test.json') as f:
    data = json.load(f)

def get_games(data):
    games = len(data['games'])
    return games

def parse_json(data):
    for item in data['games']:
        prediction = {}
        prediction['Away_Team'] = item['teams']['away']['name']
        prediction['Home_Team'] = item['teams']['home']['name']
        for stats in item['stats']['wpa']['gameWpa']:
            prediction['HomeTeam_WinPercentage'] = stats['homeTeamWinProbability']
            prediction['AwayTeam_WinPercentage'] = stats['awayTeamWinProbability']
            Winning_Team = ''
            if prediction['HomeTeam_WinPercentage'] > prediction['AwayTeam_WinPercentage']:
                Winning_Team = prediction['Home_Team']
            else:
                Winning_Team = prediction['Away_Team']
        prediction['Team_Predicted_ToWin'] = Winning_Team

        print(prediction)

        
            





print(get_games(data))
parse_json(data)