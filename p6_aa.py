# coding: utf-8

while True:
	ent = int(raw_input())
	if ent == 0: break
	
	cord = raw_input().split()
	
	for i in range(ent):
		entra = raw_input().split()
		
		
		if int(entra[0]) == int(cord[0]) or int(entra[1]) == int(cord[1]):
			sai = "divisa"
		
		elif int(entra[0]) < int(cord[0]) and int(entra[1]) < int(cord[1]):
			sai = "SO"
		
		elif int(entra[0]) < int(cord[0]) and int(entra[1]) > int(cord[1]):
			sai = "NO"
			
		elif int(entra[0]) > int(cord[0]) and int(entra[1]) < int(cord[1]):
			sai = "SE"
		
		else:
			sai = "NE"
	
		print sai
		
