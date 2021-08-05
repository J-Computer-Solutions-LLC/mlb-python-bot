import requests
import json

url = 'https://baseballsavant.mlb.com/scoreboard-data'
api = 'https://mlb.jcompsolu.com/api/game'

def main_requests(url):
    r = requests.get(url)
    return r.json()

def get_games(response):
    games = len(response['games'])
    return games

def parse_json(response):
    for item in response['games']:
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
    return prediction

def send_api(prediction, api):
    send = requests.post(api, prediction)
    return send


data = main_requests(url)
print(get_games(data))
parse_json(data)
send_api(api)



