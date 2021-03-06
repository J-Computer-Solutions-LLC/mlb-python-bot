
import mlbgame
import random
from datetime import date, timedelta
import requests

url = 'https://mlb.jcompsolu.com/api/game'

IN_PROGRESS = 'IN_PROGRESS'

todays_date = date.today() +  timedelta(days=1)
games = mlbgame.day(todays_date.year, todays_date.month, todays_date.day)
for game in games:
    if game.game_status != IN_PROGRESS:
        prob = random.random()
        win_team = ''
        if prob > 0.5:
            win_team = game.home_team
        else:
            win_team = game.away_team
        prediction = {}
        prediction['home_team'] = game.home_team
        prediction['away_team'] = game.away_team
        prediction['game_id'] = game.game_id
        prediction['win_percentage'] = random.uniform(51.0, 81.0)
        prediction['winning_predicted_team'] = win_team
        prediction['game_date'] = todays_date
        #send = requests.post(url, prediction)
        stats = mlbgame.players(prediction['game_id'])
        print(stats.__keys__)
