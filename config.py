config = {
 'login_url': 'https://entgaming.net/forum/ucp.php',
 'games_url': 'https://entgaming.net/bans/games.php',
 'game_url': 'https://entgaming.net/bans/game.php',
 'rangeban_url': 'https://entgaming.net/bans/rangeban.php',
 'verbose': 0,
 'ent-user' : <Username>,
 'ent-pass' : <Password>
}

def getKey(key):
  return config[key]
  
def getUrl(key,params):
  return config[key]+'?'+params