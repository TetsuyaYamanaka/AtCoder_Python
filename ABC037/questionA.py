# _*_ encoding: utf-8 _*_

a, b, c = map(int, raw_input().split())

mini = min(a, b)
sum = ret = 0

while True:
	sum += mini
	if sum > c:
		break
	else:
		ret += 1

print ret