# questionB.py

inputL = raw_input()
dis1 = inputL.split(" ")
inputL = raw_input()
dis2 = inputL.split(" ")

if int(dis1[0]) == int(dis2[0]) or int(dis1[0]) == int(dis2[1]) or int(dis2[0]) == int(dis1[1]):
	print('YES')
else:
	print('NO')