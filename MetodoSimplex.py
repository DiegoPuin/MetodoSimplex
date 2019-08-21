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
        if(i > 0 and j != var+1):
            matriz[i][j] = int(input("Ingrese el " + str(j+1) + " coeficiente de la " + str(i) + " restriccion: "))
        if(i > 0 and j == var+1):
            matriz[i][j] = int(input("Ingrese el valor del lado derecho de la " + str(i) + " restriccion: "))  