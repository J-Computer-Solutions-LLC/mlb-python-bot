import requests
from datetime import date, timedelta
import json

todays_date = date.today() + timedelta(days=0)

url = f'https://baseballsavant.mlb.com/scoreboard-data?date={todays_date}'

def main_requests(url):
    r = requests.get(url)
    data = json.loads(r.text)
    return data

def get_games(response):
    games = len(response['games'])
    return games

def parse_json(response):
    for item in response['games']:
        prediction = {}
        prediction['Away_Team'] = item['teams']['away']['name']
        prediction['Game_Date'] = todays_date
        prediction['Home_Team'] = item['teams']['home']['name']
        for stats in item['stats']['wpa']['gameWpa']:
            Winning_Team = ''
            prediction['HomeTeam_WinPercentage'] = stats['homeTeamWinProbability']
            prediction['AwayTeam_WinPercentage'] = stats['awayTeamWinProbability']
            if prediction['HomeTeam_WinPercentage'] > prediction['AwayTeam_WinPercentage']:
                Winning_Team = prediction['Home_Team']
            else:
                Winning_Team = prediction['Away_Team']
            prediction['Team_Predicted_ToWin'] = Winning_Team
            send = requests.post('https://mlb.jcompsolu.com/api/game', prediction)
        print(send)

data = main_requests(url)
print(get_games(data))
prediction = parse_json(data)
