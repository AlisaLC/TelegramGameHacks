import requests

# High scores may result in your ban
# Keep your score limit under 800 - 900
score = 500
# LumberJack is used as an example
# You can use any of other games in tbot.xyz like Corsairs and Math Battle
game_url = 'http://tbot.xyz/lumber/#your_unique_id'
unique_id = (''.join(game_url.split('#')[1:])).split('tgShareScoreUrl')[0][:-1]
data = {'data': unique_id, 'score': score}
url = 'http://tbot.xyz/api/setScore'
request = requests.post(url, data)
scores = request.json()
if 'scores' in scores:
    print('Hacking successful! :D')
else:
    print('Hacking failed :(')
