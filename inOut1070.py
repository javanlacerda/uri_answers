# coding: utf-8
# Javan Lacerda, UFCG

num = int(raw_input())

inn = 0
out = 0
for i in range(num):
	ent = int(raw_input())
	if 10 <= ent <= 20:
		inn += 1
	else:
		out += 1

print "%i in" % inn
print "%i out" % out	
