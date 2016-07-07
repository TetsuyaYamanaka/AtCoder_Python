# _*_ encoding: utf-8 _*_

w, h = map(int, raw_input().split())

if w*3 == h*4:
	print('4:3')
else:
	print('16:9')