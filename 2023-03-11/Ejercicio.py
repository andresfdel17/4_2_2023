# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 14:44:38 2023

@author: Andres Felipe Delgado G
"""
#%% Ejercicio 1
# Calcular ls suma de los divisores de los numeros ingresados por terminal
LINES = "".center(50, "-")
print(LINES)
print("Ejercicio1: Calcula la suma de divisores")
print(LINES)
while True:
    number: int = int(input("Ingresa un numero, y para acabar uno negativo:\nNum: "));
    suma: int = 0;
    if(number < 0):
        break;
    for k in range(1,number + 1):
        if number % k == 0:
            suma+= k;
    print("Salida:")
    print(LINES)
    print("La suma de los divisores del numero {} es {}".format(number, suma))

#%% Ejercicio 2

# Calcular los numeros primos entre 1 y 100
LINES = "".center(50, "-")
maxN: int = 101;

print(LINES)
print("Ejercicio2: Numeros primos entre 1 y {}".format(maxN))
print(LINES)

numerosPrimos: list = [];
for k in range(2, maxN):
    list_div: list = [];
    for l in range(1, k + 1):
        if(k % l == 0):
            list_div.append(l)
    if(len(list_div) == 2):
        numerosPrimos.append(k)
print("Salida:")
print(LINES)
print("La lista de numeros primos entre 1 y 100 es {}".format(numerosPrimos))
print("Entre 1 y {} hay {} numeros primos".format(maxN - 1, len(numerosPrimos)))