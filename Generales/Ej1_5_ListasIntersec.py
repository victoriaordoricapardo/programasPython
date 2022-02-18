# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 11:30:57 2019

Ej. 1.5: determina si dos listas se intersectan.

@author: dai
"""

#Cantidad de elementos de las listas.
print("Cant. de elementos en las listas: ")
n = int(input())

if 3<= n<= 6:
	#Crea las listas de n elementos colocando 0's en las mismas.
	a = [0]*n
	b = [0]*n
	c = False
	
	#Lectura de datos de las listas.
	print("Datos de  la lista 1:")
	for i in range(n):
		a[i] = int(input())
	print("Datos de  la lista 2:")	
	for i in range(n):
		b[i] = int(input())
	
	#Determina si se intersectan.
	for i in range(n):
		for j in range(n):
			if a[i] == b[j]:
				c = True
				break
	
	#Impresión del resultado.
	if c == True:
		print("Hay intersección")
	else: print("No hay intersección")
else:
	print("El valor entre [3,6]")

