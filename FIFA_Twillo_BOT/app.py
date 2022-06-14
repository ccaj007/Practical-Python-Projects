import requests

urls = {'group': 'https://worldcup.sfg.io/teams/group_results',
'country': 'https://worldcup.sfg.io/matches/country?fifa_code=',
'today': 'https://worldcup.sfg.io/matches/today',
'tomorrow': 'https://worldcup.sfg.io/matches/tomorrow'}

countries = ['KOR', 'PAN', 'MEX', 'ENG', 'COL', 'JPN', 'POL', 'SEN',
'RUS', 'EGY', 'POR', 'MAR', 'URU', 'KSA', 'IRN', 'ESP',
'DEN', 'AUS', 'FRA', 'PER', 'ARG', 'CRO', 'BRA', 'CRC',
'NGA', 'ISL', 'SRB', 'SUI', 'BEL', 'TUN', 'GER', 'SWE']

html = requests.get(urls['today']).json()
for match in html:
    print(match['home_team_country'], 'vs',
    match['away_team_country'], 'at',
    match['datetime'])
    