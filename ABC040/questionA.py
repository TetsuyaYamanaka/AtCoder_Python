n, x = map(int, raw_input().split())

ans = x - 1 if x <= (n + 1)/2 else n - x

print ans