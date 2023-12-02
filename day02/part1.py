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

def filter_game(game):
	_,colors = game
	return colors[0] <= 12 and colors[1] <= 13 and colors[2] <= 14

def get_game_id(game):
	return game[0]

f = open("input.txt", "r")
lines = f.readlines()
lines = map(parseLine, lines)
lines = map(get_max, lines)
lines = filter(filter_game, lines)
lines = map(get_game_id, lines)
print(sum(lines))
f.close()