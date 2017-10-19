# coding: utf-8

def verifica_meio(array, meio):
	if array[meio] == array[meio + 1]:
			
		meio = verifica_meio(array, meio+1)
	
	return meio		
	
def busca_binaria(array, valor, inicio, fim):
	
	meio = (inicio + fim) / 2
	
	if valor < array[meio]:
		return busca_binaria(array, valor, inicio, meio)
	
	if valor > array[meio]:
		return busca_binaria(array, valor, meio, fim)
		
	
	if valor == array[meio]:
		
		meio = verifica_meio(array,meio)
			
		return meio
	
	return busca_binaria(array, valor-1, inicio, fim)		
		



ent = raw_input().split()

array1 = []
array2 = []

a1 = raw_input().split()
a2 = raw_input().split()

for i in range(int(ent[0])):
	a1[i] = int(a1[i])
	
a1 = sorted(a1)

for i in range(int(ent[1])):
	
	vez = int(a2[i])
	
	cont = 0
	while cont < busca_binaria(a1,vez,0,len(a1)):
		cont += 1
	
	array1.append(cont) 



print array1		







	
