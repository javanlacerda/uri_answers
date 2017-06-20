# coding: utf-8
# Javan Lacerda, UFCG

num = int(raw_input())

for i in range(num):
	ent = int(raw_input())
	
	if ent % 2 == 0 and ent < 0:
		print "EVEN NEGATIVE"
	
	elif ent % 2 == 0 and ent > 0:
		print "EVEN POSITIVE"
	
	
	elif ent % 2 != 0 and ent < 0:
		print "ODD NEGATIVE"
	
	elif ent % 2 != 0 and ent > 0:
		print "ODD POSITIVE"
		
	else:
		print "NULL"	 			
	
		
		
		

