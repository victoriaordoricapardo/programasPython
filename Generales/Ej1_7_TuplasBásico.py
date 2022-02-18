# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 12:47:31 2019

Ej. 1.7: manejo básico de tuplas.

@author: psdist
"""
"""
Función que recibe una tupla como parámetro y regresa una tupla con
los elementos pares de la misma.
"""
def tuplaPares(t):
	resul= ()
	for i in range(0, len(t), 2):
		resul += (t[i],)
	return resul

#Versión 2.
def tuplaPares2(t):
	return t[::2]

#Prog. principal.
print("Tupla pares: ",
			tuplaPares(('Yo', 'mi', 'a', 'prueba', 'tupla')))
print("Tupla pares: ",tuplaPares(()))
print("Tupla pares: ",tuplaPares(("único",)))

#Usando la versión 2.
print("Tupla pares: ",
			tuplaPares2(('Yo', 'mi', 'a', 'prueba', 'tupla')))
print("Tupla pares: ",tuplaPares2(()))
print("Tupla pares: ",tuplaPares2(("único",)))

