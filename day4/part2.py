def get_score(line):
	win,values = line.split(':')[1].split('|')
	count = len(set(map(int,win.split())) & set(map(int,values.split())))
	return [1, count]

f = open("input.txt", "r")
lines = f.readlines()
f.close()
lines = list(map(get_score, lines))
l = len(lines)
count = 0
for i in range(l):
	multiplier, score = lines[i]
	count += multiplier
	print(multiplier)
	for j in range(score):
		if i + j + 1 >= l:
			break
		lines[i + j + 1][0] += multiplier
print(count)
