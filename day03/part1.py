LINE_LENGTH = 141

def is_ok(nr, i, lines):
	up = list(filter(lambda x: x != '.', lines[i - 1][nr[0] - 1:nr[1] + 1]))
	down = list(filter(lambda x: x != '.', lines[i + 1][nr[0] - 1:nr[1] + 1]))
	left = list(filter(lambda x: x != '.', lines[i][nr[0] - 1]))
	right = list(filter(lambda x: x != '.', lines[i][nr[1]]))
	return up != [] or down != [] or left != [] or right

def get_packs(lines):
	res = 0
	for i in range(1, len(lines) - 1):
		is_parsing = False
		nr = [0,0]
		line = lines[i]
		for j in range(1, LINE_LENGTH + 1):
			if not line[j].isdigit():
				if not is_parsing:
					continue
				n = line[nr[0]:nr[1]]
				if n != "" and is_ok(nr, i, lines):
					res += int(n)
				nr = [0,0]
				is_parsing = False
				continue
			if not is_parsing:
				nr[0] = j
				nr[1] = j + 1
				is_parsing = True
			else:
				nr[1] += 1
	return res

f = open("input.txt", "r")
lines = ['.'*(LINE_LENGTH + 2)] + list(map(lambda x:'.'+x[:-1]+'.',f.readlines())) + ['.'*(LINE_LENGTH + 2)]
lines = get_packs(lines)
print(lines,sep='\n')
f.close()