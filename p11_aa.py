# coding: utf-8

saida = ""
ent = raw_input()

for i in ent:
	
	if not i.upper() in ["A","O","Y","E","U","I"]:
		saida += "." + i.lower()
	
print saida
