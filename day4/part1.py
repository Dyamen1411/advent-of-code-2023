def get_score(line):
	win,values = line.split(':')[1].split('|')
	count = len(set(map(int,win.split())) & set(map(int,values.split())))
	return int(2 ** (count - 1))

f = open("input.txt", "r")
lines = f.readlines()
print(sum(map(get_score, lines)))
f.close()