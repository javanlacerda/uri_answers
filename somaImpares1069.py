# coding: utf-8
# Javan Lacerda, UFCG

num = int(raw_input())
num2 = int(raw_input())

sums = 0
if num > num2:
	flag = 1
	num2 += 1
else:
	flag = -1
	num -= 1
	
for i in range(num2,num,flag):
	if i % 2 != 0:
		
		sums += i
	
print sums
