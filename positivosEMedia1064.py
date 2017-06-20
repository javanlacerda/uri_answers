# coding: utf-8
# Javan Lacerda, UFCG

positivos = []
for i in range(6):
	num = float(raw_input())
	if num > 0:
		positivos.append(num)
		
print "%i valores positivos" % (len(positivos))
print "%.1f" % (sum(positivos) / len(positivos))		
	
