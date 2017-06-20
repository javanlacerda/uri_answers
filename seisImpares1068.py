# coding: utf-8
# Javan Lacerda, UFCG

num = int(raw_input())
i = 0
while i < 6:
	if num % 2 != 0:
		print num
		i += 1	
	num += 1
