# coding: utf-8


mapa = {1: "A", 2:"B", 3: "C", 4: "D", 5: "E"}


magic_num = 127

while True:	
	n = int(raw_input())
	if n == 0: break

	for i in range(n):
		var = 0
		ent = raw_input().split()
			
		sai = "*"
		for j in range(len(ent)):
			
			if int(ent[j]) <= magic_num:
				
				var += 1
				if var <= 1:
				
					sai = mapa[int(j)+1]
				
				else: 
					sai = "*"
		
		print sai			
