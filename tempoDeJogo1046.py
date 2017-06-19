# coding: utf-8

time = raw_input().split()

begin = int(time[0])
end = int(time[1])

if end > begin:
	print "O JOGO DUROU %i HORA(S)" % (end - begin)
	
else:
	print "O JOGO DUROU %i HORA(S)" % (24 - begin + end)	
