# %% Inicio
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 14:38:11 2023

@author: Andres Felipe Delgado
"""

# %% Ejercicio 1

trigo: int = 1

for i in range(1, 64):
    trigo *= 2

print("La cantidad de trigo es {}".format(trigo))

# %% Ejercicio 2
import time

def ValidateFormat(hora: list):
    if int(hora[0]) > 23 or int(hora[0]) < 0:
        print("La hora debe ser mayor a 0 y menor a 23")
        return False
    elif int(hora[1]) > 59 or int(hora[1]) < 0:
        print("Los minutos deben ser mayor a 0 y menor a 60")
        return False
    elif int(hora[2]) > 59 or int(hora[2]) < 0:
        print("Los segundos deben ser mayor a 0 y menor a 60")
        return False
    else:
        return True

horaStr: str = ""
hora: list = []
while True:
    horaStr = input("Ingrese la hora en format HH:MM:SS: \n")
    hora = horaStr.strip().split(":")
    if ValidateFormat(hora):
        break

while True:
    while int(hora[0]) < 24:
        while int(hora[1]) < 60:
            while int(hora[2]) < 60:
                print("{}:{}:{}".format(hora[0].zfill(2), hora[1].zfill(2), hora[2].zfill(2)))
                hora[2] = str(int(hora[2]) + 1)
                time.sleep(1)
            hora[2] = "00"
            hora[1] = str(int(hora[1]) + 1)
        hora[1] = "00"
        hora[0] = str(int(hora[0]) + 1)
    hora = ["00", "00", "00"]
    



# %% Ejercicio 3
# 3 4 6 5 - + * 6 +


def calculate(s):
    stack = []
    opers = ['+', '-', '*', '/']
    for c in s:
        if c not in opers:
            stack.append(int(c))
        else:
            top1 = stack.pop()
            top2 = stack.pop()
            if c == '+':
                stack.append(top2 + top1)
            elif c == '-':
                stack.append(top2 - top1)
            elif c == '*':
                stack.append(top2 * top1)
            elif c == '/':
                stack.append(int(top2 / top1))
    return stack.pop()

string: str = input("Ingrese la expresion:\n")
print("EL resultado es: {}".format(calculate(string.split())))