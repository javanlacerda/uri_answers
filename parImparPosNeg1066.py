# coding: utf-8
# Javan Lacerda, UFCG

pos = 0
neg = 0
par = 0
impar = 0
for i in range(5):
	num = float(raw_input())
	if num % 2 == 0:
		par += 1
	
	else:
		impar += 1
		
	if num > 0:
		pos += 1
	
	elif num < 0:
		neg += 1			
		
print "%i valor(es) par(es)" % (par)
print "%i valor(es) impar(es)" % (impar)
print "%i valor(es) positivo(s)" % (pos)
print "%i valor(es) negativo(s)" % (neg)
