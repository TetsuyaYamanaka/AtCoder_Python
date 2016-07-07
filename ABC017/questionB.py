i = 0

inputL = raw_input()
len = len(inputL)

while i < len:
	if inputL[i] == 'o' or inputL[i] == 'k' or inputL[i] == 'u':
		i += 1
	elif i + 1 < len:
		if inputL[i] == 'c' and inputL[i + 1] == 'h':
			i += 2
		else:
			break
	else:
		break

print('YES' if i == len else 'NO')