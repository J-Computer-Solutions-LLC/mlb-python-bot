When we first started trying to scrape baseball savant, I found the API endpoit on their website that was feeding all the live data to their website in real time.

This API gives us every statistic we need but we can only retrieve it during live games as they are being played.

Test.json is just an api call to that endpoint a few weeks ago in the middle of the gameday but if you upload test.json to:
https://jsonformatter.org/json-reader

You will be able to collapse all of the json points and it will give you a better understanding of what data is available per team currently playing. Looking inside you'll see that there is a WPA(Win Percentage Added) This is google statistical analysis on which team is likley to win and it is updated around 50 times per game. 
At the beginning of the game WPA for home team might be low but as the game plays on and the stats change the WPA changes in favor of the home team.
when uploading test.json to the website jsonformatter it makes it much easier to see these changes.

test.py is basically mlb.py without making a request to baseball savants api and is an example of a game day 2 weeks ago.