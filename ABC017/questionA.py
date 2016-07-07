#coding:utf-8

sum = 0

for i in range(3):
	inputS = raw_input()
	l = inputS.split()
	
	score = int(l[0])
	eval = int(l[1])
	
	if(eval == 10):
		sum += score
	else:
		sum += int(score * eval * 0.1)
	
print sum