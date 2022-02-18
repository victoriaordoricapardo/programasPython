# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 11:30:57 2019

Ej. 1.5: Intersección de listas.
@author: dai
"""

n = int(input())

if 3<= n<= 6:
	 a = [0]*n
	   b = [0]*n
    c = False
		
		#Lectura de datos.
		print("Datos de lista 1:")
    for i in range(n):
        a[i] = int(input())

		print("Datos de lista 2:")
    for i in range(n):
        b[i] = int(input())
				
		#Determina si hay intersección.
    for i in range(n):
        for j in range(n):
            if a[i] == b[j]:
                c = True
                break
		
		#Imprime el resultado.
    if c == True: 
        print("Hay intersección")
    else:
        print("No hay intersección")
else:
    print("no hay valor necesario")
        