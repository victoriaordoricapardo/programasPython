# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 12:41:36 2019
@author: psdist

Ej. 1.2: imprime los caracteres pares de una cadena.
"""

cad= input("Dame la cadena: ")

for i in range(0, len(cad), 2):
	print(cad[i])

