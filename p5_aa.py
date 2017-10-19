# coding: utf-8



venc = []


ent = raw_input().split()


plays = [0] * (int(ent[0]) + 1)


arms = raw_input().split()

jogs = int(raw_input())

preso = []

j = 1
for i in range(jogs):
	
	if j == int(ent[0]) + 1:
		j = 1
	
	elif j == int(ent[0]) +2:
		j = 2
			
	jog = raw_input().split()
	jogg = int(jog[0]) + int(jog[1])
	
	if j not in preso:
		plays[j] += jogg
		if plays[j] > int(ent[1]):
			venc.append(j)
		if plays[j] in arms:
			preso.append(j)
		j += 1
	else:
		plays[j+1] += jogg
		if plays[j+1] > int(ent[1]):
			venc.append(j+1)
		if plays[j+1] in arms:
			preso.append(j+1)
		
		preso.remove(j)
		j += 2
			
		
		
print venc
print plays
