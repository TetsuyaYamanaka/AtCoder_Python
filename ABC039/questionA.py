# _*_ encoding:utf-8 _*_

a, b, c = map(int, raw_input().split())

ret = 2*(a*b + a*c + b*c)

print ret