# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 11:29:53 2019

Ej. 1.4: ejemplo del manejo de listas.
@author: psdist
"""
import random

#Genera la lista de califs. de manera aleatoria.
#Los valores se guardan como float.
n= 5
califs= []

for i in range(n):
	calif= float(random.randint(6,10))
	califs= califs + [calif]
print("Califs: ",califs)

#Porcentajes para el promedio ponderado.
porcents= [0.10, 0.20, 0.23, 0.30, 0.17]

#Calcula el promedio ponderado.
prom= 0
for i in range(n):
	prom += califs[i] * porcents[i]

print("Promedio con decimales: "+str(prom))
print("Promedio redondeado: ",round(prom))
















