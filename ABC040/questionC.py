N = int(raw_input())
a = map(int, raw_input().split())

dp = [0]
dp.append(abs(a[1] - a[0]))

for i in range(2, N):
	c1 = dp[i - 1] + abs(a[i] - a[i - 1])
	c2 = dp[i - 2] + abs(a[i] - a[i - 2])
	
	dp.append(min(c1, c2))

print dp[N - 1]