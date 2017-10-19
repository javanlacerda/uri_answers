# coding: utf-8

entrada = int(raw_input())

for j in range(entrada):
	ent = int(raw_input())

	cont = 0

	tiros = raw_input().split()

	acoes = raw_input()

	for i in range(ent):
		if int(tiros[i]) < 3 and acoes[i] == "S":
			cont += 1
			
		elif int(tiros[i]) >= 3 and acoes[i] == "J":
			cont += 1	
			
			
	print cont
