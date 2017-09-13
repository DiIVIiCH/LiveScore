teams = {1610612755:'76ers',
		1610612754:'Pacers',
		1610612751:'Nets',
		1610612738:'Celtics',
		1610612748:'Heat',
		1610612739:'Cavaliers',
		1610612741:'Bulls',
		1610612753:'Magic',
		1610612749:'Bucks',
		1610612766:'Hornets',
		1610612765:'Pistons',
		1610612764:'Wizards',
		1610612757:'Trailblazers',
		1610612759:'Spurs',
		1610612746:'Clippers',
		1610612745:'Rockets',
		1610612744:'Warriors',
		1610612762:'Jazz',
		1610612752:'Knicks',
		1610612761:'Raptors',
		1610612737:'Hawks',
		1610612743:'Nuggets',
		1610612760:'Thunder',
		1610612756:'Suns',
		1610612742:'Maverics',
		1610612758:'Kings',
		1610612763:'Grizzlies',
		1610612747:'Lakers',
		1610612750:'Timberwolves',
		1610612740:'Pelicans',
		1610616833: 'East NBA All Stars',
		1610616834: 'West NBA All Stars'}

HOME_TEAM_ID = 6
VISITOR_TEAM_ID = 7
LINESCORE_TEAM_ID = 3
GAME_STATUS_TEXT = 4
TEAM_CITY_NAME = 5
PTS = 21
base_url = 'http://stats.nba.com/stats/scoreboard/?GameDate='
leagueID = '00'
dayOffset = '0'
headers = {'user-agent': ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) '
		                          'AppleWebKit/537.36 (KHTML, like Gecko) '
		                          'Chrome/45.0.2454.101 Safari/537.36'),
		           'referer': 'http://stats.nba.com/scores/'}