# coding: utf-8

vertebra = raw_input()
tipo = raw_input()
tipo1 = raw_input()


if vertebra == "vertebrado":
	if tipo == "ave":
		if tipo1 == "carnivoro":
			print "aguia"
		
		else:
			print "pomba"	
	
	else:
		if tipo == "onivoro":
			print "homem"
		
		else:
			print "vaca"			

else:
	if tipo == "inseto":
		if tipo1 == "hematofago":
			print "pulga"
		
		else:
			print "lagarta"	
	
	else:
		if tipo == "hematofago":
			print "sanguessuga"
		
		else:
			print "minhoca"			
