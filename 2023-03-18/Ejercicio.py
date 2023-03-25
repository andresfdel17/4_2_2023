# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 14:57:47 2023

@author: Andres felipe Delgado
"""

# %% Velocidad de Radar
# Incompleto

LINES = "".center(70, "-")

print(LINES)
print("RADAR DE VELOCIDAD")
print(LINES)


def sec2Hour(sec: int):
    return (sec / 3600)


less_f: float = ((1 / (2.00000004 * (10 ^ 10))) - (1 / (2 * (10 ^ 10))))
plus_f: float = ((1 / (2.00000004 * (10 ^ 10))) + (1 / (2 * (10 ^ 10))))
speed: float = ((6.685 * (10 ^ 8)) * less_f) / plus_f

print(">>> La velocidad es: {} millas por hora.".format(str(speed)))
print(LINES)

# %% Distancia recorrida MRU
LINES = "".center(70, "-")

print(LINES)
print("DISTANCIA DE UN MOVIL".center(70))
print(LINES)

speed: float = float(input(">>> Ingrese la velocidad : "))
time: float = float(input(">>> Ingrese el tiempo : "))

print(LINES)
print("DISTANCIA: {:.2f} Metros".center(70).format(speed*time))
print(LINES)

# %% Velocidad Movil

LINES = "".center(70, "-")

print(LINES)
print("VELOCIDAD DE UN MOVIL".center(70))
print(LINES)

dist: float = float(input(">>> Ingrese la Distancia : "))
time: float = float(input(">>> Ingrese el tiempo : "))

print(LINES)
print("Velocidad: {:.2f} m/s".center(70).format(dist/time))
print(LINES)

# %% Tiempo de encuentro
import sys;

LINES = "".center(70, "-")

print(LINES)
print("VELOCIDAD DE UN MOVIL".center(70))
print(LINES)

dist: float = float(input(">>> Distancia de separacion : "))
print(LINES)
speed1: float = float(input(">>> Velocidad del vehiculo 1 : "))
speed2: float = float(input(">>> Velocidad del vehiculo 2 : "))

if speed1 <= 0 and speed2 <= 0:
    print("Ambas velocidades no pueden ser iguales o menores a 0")
    sys.exit()
print(LINES)
print("TIEMPO: {:.2f} m/s".center(70).format(dist/(speed1 + speed2)))
print(LINES)
#%% Distancia entre 2 puntos
import math;

LINES = "".center(70, "-")

print(LINES)
print("DISTANCIA ENTRE 2 PUNTOS EN EL PLANO".center(70))
print(LINES)

coordAx: float = float(input(">>> Ingrese la coordenada Ax: "))
coordAy: float = float(input(">>> Ingrese la coordenada Ay: "))
print(LINES)
coordBx: float = float(input(">>> Ingrese la coordenada Bx: "))
coordBy: float = float(input(">>> Ingrese la coordenada By: "))
print(LINES)
distancia: float = math.sqrt(((coordAx - coordBx) ** 2) + ((coordAy - coordBy) ** 2))
print("Distancia: {:.2f}".center(70).format(distancia))
print(LINES)
