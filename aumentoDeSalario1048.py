# coding: utf-8
# Javan Lacerda, UFCG

money = float(raw_input())

if 0 <= money <= 400:
	percent, reajuste = 15, (0.15 * money)
	
elif 400 < money <= 800:
	percent, reajuste = 12, (0.12 * money)
	
elif 800 < money <= 1200:
	percent, reajuste = 10, (0.10 * money)
	
elif 1200 < money <= 2000:
	percent, reajuste = 7, (0.07 * money)	
	
else:
	percent, reajuste = 4, (0.04 * money)
	
print "Novo salario: %.2f" % (money + reajuste)
print "Reajuste ganho: %.2f" % (reajuste)
print "Em percentual: %i %%"	% (percent)
