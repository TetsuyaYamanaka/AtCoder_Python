a, b, c, d = map(int, raw_input().split())

tWin = float(b) / a
aWin = float(d) / c

if tWin > aWin:
	print'TAKAHASHI'
elif tWin < aWin:
	print 'AOKI'
else:
	print 'DRAW'