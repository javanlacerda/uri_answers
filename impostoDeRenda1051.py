# coding: utf-8
# Javan Lacerda, UFCG

ent = float(raw_input())

taxa = 0 
if ent > 4500:
	taxa += 0.08 * 1000
	taxa += 0.18 * 1500
	taxa += 0.28 * (ent - 4500)
	print "R$ %.2f" % (taxa)
	
elif ent > 3000:
	taxa += 0.08 * 1000
	taxa += 0.18 * (ent - 3000)
	print "R$ %.2f" % (taxa)
	
elif ent > 2000:
	taxa += 0.08 * (ent - 2000)	
	print "R$ %.2f" % (taxa)
	
else:
	print "Isento"
		
	
