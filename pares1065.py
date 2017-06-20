# coding: utf-8
# Javan Lacerda, UFCG

positivos = []
for i in range(5):
	num = float(raw_input())
	if num % 2 == 0:
		positivos.append(num)
		
print "%i valores pares" % (len(positivos))
	
	
