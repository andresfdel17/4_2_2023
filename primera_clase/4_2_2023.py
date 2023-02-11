#%% Ejercicio

# -*- coding: utf-8 -*-
"""
Created on Sat Feb  4 13:58:32 2023

@author: Andrés Felipe Delgado 
@version Python 3.8.10
"""
import math;
import json;
# Area del cuadrado

def E1():
    # float_lado: float = lado del cuadrado
    float_lado = float(
        input("ingrese el  lado de un cuadrado para calcular el área: "))
    float_area = float_lado ** 2
    print("El área del cuadrado es:", float_area)
# Area del triangulo

def E2():
    float_base = float(
        input("ingrese la base del triangulo: "))
    float_altura = float(
        input("ingrese la altura del triangulo: "))
    float_area = (float_base * float_altura) / 2
    print("El área del triangulo es:", float_area)
# Area del circulo


def E3():
    float_radio = float(input("Ingrese el radio del circulo: "))
    print("El area del circulo es: ", (math.pi * float_radio ** 2))
    
#Grados °f a °C
def E4():
    float_grados = float(input("Ingrese los grados farenheit: "))
    float_c = ((float_grados * (5/9)) + 32);
    print(f"{float_grados} f en C es igual a {float_c} C")
def E5():
    numbers: list = [111111111, 222222222, 333333333, 333333333]
    suma : int = 0
    for i in range(0, len(numbers)):
        suma += numbers[i]
    entero: int = int(suma / 1000)
    decimal: int = suma % 1000
    print(f"La suma de los numeros es {entero}.{decimal}")

dict_ex = {
    1: "Calculo area del cuadrado",
    2: "Calculo area del triangulo",
    3: "Area de un circulo",
    4: "Grados °f a °C",
    5: ""
}
dict_ejercicios = {
    1: E1,
    2: E2,
    3: E3,
    4: E4,
    5: E5
}
print(json.dumps(dict_ex, indent=4))
int_ejercicio = int(input("Elija el ejercicio a resolver: "))
dict_ejercicios[int_ejercicio]()
