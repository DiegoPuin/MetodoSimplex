# -*- coding: utf-8 -*-
"""
Editor de Spyder
Este es un archivo temporal
"""

var = int(input('¿Cuántas variables de decisión tiene el problema? '))
res = int(input('¿Cuántas restricciones? '))

matriz = []
for i in range(res+1):
    matriz.append([])
    for j in range(var+1):
        matriz[i].append(None)

for i in range(res+1):
    for j in range(var+1):
        if(i == 0 and j != var):
            matriz[i][j] = int(input("Ingrese el " + str(j+1) + " coeficiente de la funcion objetivo: "))
        if(i > 0 and j != var):
            matriz[i][j] = int(input("Ingrese el " + str(j+1) + " coeficiente de la " + str(i) + " restriccion: "))
        if(i > 0 and j == var):
            matriz[i][j] = int(input("Ingrese el valor del lado derecho de la " + str(i) + " restriccion: "))  

tableroSimplex = []
for i in range(res+2):
    tableroSimplex.append([])
    for j in range((2 * var)+1):
        tableroSimplex[i].append(0)
        
for i in range(res+2):
    for j in range((2 * var)+1):
        if(j < var):
            tableroSimplex[i][j] = matriz[i][j]
        if(j >= var and j != (2 * var)):
            tableroSimplex[var+i][j] = 1    
            
            