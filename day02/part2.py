def parse_game(game):
	colors = [0, 0, 0]
	for data in game.lstrip().split(','):
		count,color = data.lstrip().split(' ')
		colors[['red', 'green', 'blue'].index(color.rstrip())] = int(count)
	return colors

def parseLine(line):
	game_id,games = line.split(':')
	game_id = int(game_id.split(' ')[1])
	games = map(parse_game, games.lstrip().split(';'))
	return (game_id, list(games))

def get_max(game):
	game_id,games = game
	colors = [0, 0, 0]
	for game in games:
		for i in range(3):
			colors[i] = max(colors[i], game[i])
	return (game_id, colors)

def get_power(game):
	game_id,(r,g,b) = game
	return r * g * b

f = open("input.txt", "r")
lines = f.readlines()
lines = map(parseLine, lines)
lines = map(get_max, lines)
lines = map(get_power, lines)
print(sum(lines))
f.close()