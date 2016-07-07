# _*_ encoding: utf-8 _*_

a, b = map(int, raw_input().split())

ans = b / a if b % a == 0 else b / a + 1

print ans