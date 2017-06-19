# coding: utf-8
# Javan Lacerda, UFCG

time = raw_input().split()

beginh = int(time[0])
beginm = int(time[1])
endh = int(time[2])
endm = int(time[3])

if endh > beginh:
	horas = endh - beginh

else:
	horas = 24 - beginh + endh

if endm > beginm:
	mins = endm - beginm

else:
	mins = 60 - beginm + endm	
	horas -= 1
	if mins == 60:
		mins = 0
		horas += 1

print "O JOGO DUROU %i HORA(S) E %i MINUTO(S)" % (horas, mins)
