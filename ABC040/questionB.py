def calc(h, w, mod):
	return abs(h - w) + mod
	
if __name__ == "__main__":
	n = int(raw_input())

	for h in range(1, n+1):
		for w in range(h, n/h+1):
			mod = n - h * w
			
			if h == 1:
				ans = calc(h, w, mod)
			else:
				ans = min(calc(h, w, mod), ans)
				
	print ans