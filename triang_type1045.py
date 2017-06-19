# -*- coding: utf-8 -*-
# Javan Lacerda

entry = raw_input().split()

a = float(entry[0])
b = float(entry[1])
c = float(entry[2])

if a >= b + c or b >= c + a or c >= a + b:
	print "NAO FORMA TRIANGULO"
	
else:
	if a ** 2 == b ** 2 + c ** 2 or b ** 2 == c ** 2 + a ** 2 or c ** 2 == a ** 2 + b ** 2:
		print "TRIANGULO RETANGULO"
	
	elif a ** 2 > b ** 2 + c ** 2 or b ** 2 > c ** 2 + a ** 2 or c ** 2 > a ** 2 + b ** 2:	
		print "TRIANGULO OBTUSANGULO"
	
	elif a ** 2 < b ** 2 + c ** 2 or b ** 2 < c ** 2 + a ** 2 or c ** 2 < a ** 2 + b ** 2:	
		print "TRIANGULO ACUTANGULO"
		
	
	if a == b and b == c:
		print "TRIANGULO EQUILATERO"
	
	elif a == b and b != c or b == c and c != a or c == a and a != b:
		print "TRIANGULO ISOSCELES"		
