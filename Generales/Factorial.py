# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 12:20:47 2019
@author: psdist

Ej. 1.1: cálculo iterativo del factorial
"""

n= int(input("Dame el número: "))

fac= 1
i= 1
while i<=n:
	fac= fac*i
	i += 1

print("El factorial (con while) de ",n," es: ",fac)

fac= 1
for i in range(1,n+1):
	fac= fac*i

print("El factorial (con for) de ",n," es: ",fac)
	
