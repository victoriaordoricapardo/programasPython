# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 11:31:51 2019

Ej. 1.10: manejo básico de diccionarios.
"""

"""
Función que recibe una cadena y entrega un diccionario con las palabras que
ahí aparecen y su cuenta.
"""
def palabrasCad(cad):
	dic= {}
	#Separa cada palabra y las entrega como una lista.
	listaPalabras= cad.split()
	
	#Recorre la lista y cuenta cada palabra usando el diccionario.
	for palabra in listaPalabras:
		if palabra in dic:
			dic[palabra] += 1	  #Si la palabra ya está en las claves de dic, 
		else:									       #incrementa su cuenta.
			dic[palabra]= 1			#La palabra es nueva.
	return dic

#Prog. principal.
cad= input("Dame la cadena:")
dicResul= palabrasCad(cad)
print("Resultado: ",dicResul)


















