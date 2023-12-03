LINE_LENGTH = 140

def get_number(x, line):
	bounds = [x, x + 1]
	while line[bounds[0] - 1].isdigit():
		bounds[0] -= 1
	while line[bounds[1]].isdigit():
		bounds[1] += 1
	return int(line[bounds[0]:bounds[1]])

def get_ratio(x, y, lines):
	gears = []

	line = lines[y - 1]
	q = set()
	if line[x - 1].isdigit():
		q.add(get_number(x - 1, line))
	if line[x].isdigit():
		q.add(get_number(x, line))
	if line[x + 1].isdigit():
		q.add(get_number(x + 1, line))
	gears += list(q)

	line = lines[y]
	if line[x - 1].isdigit():
		gears.append(get_number(x - 1, line))
	if line[x + 1].isdigit():
		gears.append(get_number(x + 1, line))

	line = lines[y + 1]
	q = set()
	if line[x - 1].isdigit():
		q.add(get_number(x - 1, line))
	if line[x].isdigit():
		q.add(get_number(x, line))
	if line[x + 1].isdigit():
		q.add(get_number(x + 1, line))
	gears += list(q)

	if len(gears) != 2:
		return 0
	return gears[0] * gears[1]

def get_gears(lines):
	s = 0
	for y,line in enumerate(lines[1:-1]):
		for x,c in enumerate(line):
			if c == '*':
				s += get_ratio(x, y + 1, lines)
	return s

f = open("input.txt", "r")
lines = ['.'*(LINE_LENGTH + 2)] + list(map(lambda x:'.'+x[:-1]+'.',f.readlines())) + ['.'*(LINE_LENGTH + 2)]
print(get_gears(lines))
f.close()