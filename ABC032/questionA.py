# encoding: utf-8

a = int(raw_input())
b = int(raw_input())
n = int(raw_input())

while(True):
	if(n % a == 0 and n % b == 0):
		break
	else:
		n += 1
	
print n
