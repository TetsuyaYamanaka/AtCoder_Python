# _*_ encoding: utf-8 _*_

n, q = map(int, raw_input().split())

a = range(n)

for i in a:
	a[i] = 0

for i in range(q):
	l, r, t = map(int, raw_input().split())
	
	cList = range(r - l + 1)
	for j in cList:
		cList[j] = t
	
	a[l-1 : r] = cList

for i in a:
	print i