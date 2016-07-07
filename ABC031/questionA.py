#coding: utf-8

function = lambda num1, num2: num1 if num1 >= num2 else num2

a, d = map(int, raw_input().split())

seki1 = (a + 1) * d
seki2 = a * (d + 1)

print function(seki1, seki2)