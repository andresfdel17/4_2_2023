# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 14:26:27 2023

@author: Andres Felipe Delgado
"""
# Ejercicios de Colecciones y cadenas

# ESTILO PERSONALIZADO

# Variables
# int_Nombre_variable = tipo_dato       ;   Variables del tipo entero
# float_Nombre_variable = tipo_dato     ;   Variables con decimales
# str_Nombre_variable = tipo_dato       ;   variables con Cadenas o caracteres
# bool_Nombre_variable = tipo_dato      ;   variables booleanas

# Constantes
# const_NOMBRE_CONSTANTE = tipo_dato    ;   Constante de cualquier tipo de datos
# NOMBRE_CONSTANTE = tipo_dato

# Colecciones
# list_Nombre_Lista = [dato1,dato2,...]         ;   Elementos de una lista
# tuple_Nombre_tupla = (dato1,dato2,...)        ;   Elementos de una tupla
# dic_Nombre_diccionario = {'clave':dato2,...}  ;   Elementos de un diccionario
#
################################################################################

# Manejo de Listas

# lista[INDICE]                         ;   Dato guardado en el INDICE
# lista = []                            ;   Lista vacia

# Particionado
#
# lista[INICIO:FIN]
# lista[INICIO:FIN:SALTO]
# lista[:]
# Lista[INDICE:]
# Lista[:FIN]
# Lista[::SALTO]

# Metododos de Listas
#
# lista.append(dato)                    ;   Agrega nuevos elementos
# lista.extend([dato1,dato2,...]        ;   Agregar uno a uno nuevos elementos
# len(lista)                            ;   Permite saber el tama?o de una lista
# lista.remove(dato)                    ;   Remueve un elemento que se le pase
#                                           como par?mentro de la lista a donde
#                                           se est? aplicando.
# lista.pop(indice)                     ;   Remueve un elemento por su indice
# lista.index(elemento)                 ;   Devuelve el n?mero de indice del
#                                           elemento pasado como par?metro
# list.count(elemento)                  ;   Se usa para saber las veces que se
#                                           repite un elemento dentro de la lista.
# lista.reverse()                       ;   Permite invertir los elementos  de
#                                           una lista.
#
################################################################################

# Manejo de Cadenas

# Datos dentro de una cadena
# %d                                    ;   Numero entero dentro de la cadena
# %f                                    ;   Numero Flotante Dentro de la cadena
# %s                                    ;   String dentro de la cadena

# Formateo de datos
# str(lista)                            ;   Lista Formateada como String
# str(Numero)                           ;   Dato Numerico formateado como string
# int(Cadena)                           ;   Cadena numerica formateada como Entero
# float(Cadena)                         ;   Cadena numerica Formateada como float

# Metodos de listas
#
# "X".join(lista)                       ;   Une los elementos de una lista donde
#                                       ;   "X" es el simbolo usado para la union
#                                       ;   de los elementos

# Cadena.split('X')                     ;   Separa los elementos de la cadena
#                                       ;   Cada vez que el interprete consiga
#                                       ;   El elemento separador X

# Substrings
# cadena[:FIN]
# cadena[INICIO:FIN]
# cadena[INDICE:]
#

################################################################################

# Metodos de cadenas

# cadena.count():   retorna el numero de veces que se repite un conjunto
#                   de caracteres especificado.

# cadena.find()  : Retornan la ubicacion en la que se encuentra el argumento
#                  indicado.

# cadena.index() : Retorna la ubicacion en la que se encuentra el argumento
#                  indicado.

# cadena.startswith("Subcadena"): Permite Saber si una cadena comienza con una
#                                 subcadena determinada.

# cadena.endswith("Subcadena")  : Permite Saber si una cadena finaliza con una
#                                 subcadena determinada.

# Cadena.isdigit() : Permite saber si una cadena es numerica
# Cadena.isalnum() : Permite saber si una cadena es alfanumericas
# Cadena.isalpha() : Permite saber si una cadena es alfabetica
# Cadena.isspace() : Permite saber si una cadena contiene solo espacios
#                    en blanco

# cadena.upper() : Permite Convertir una cadena a mayusculas
# cadena.lower() : Permite Convertir una cadena a minusculas

# cadena.replace("Cadena","Nuevacadena") : Permite reemplazar una cadena
#                                          por otras

# cadena.center(Longitud,Caracter_relleno): Devuelve una  cadena centrada

# cadena.ljust(Longitud,Caracter_relleno):  Devuelve una  cadena alineada a la
#                                           Izquierda.

# cadena.rjust(Longitud,Caracter_relleno):  Devuelve una  cadena alineada a la
#                                           derecha.
#
################################################################################

# Resultado final

# *****************************************************************************
# |       Producto       |     Descripcion      |  Cantidad   |      Precio   |
# *****************************************************************************
# |      SmartPhone      |  Iphone 12 Pro Max   |      1      |       2000    |
# |      SmartPhone      |  Iphone 11 Pro Max   |      1      |       1500    |
# |      SmartPhone      |  Iphone 10 Pro Max   |      1      |       1200    |
# |      SmartPhone      |  Iphone 09 Pro Max   |      1      |       1000    |
# *****************************************************************************
# |                                                  TOTAL    |       5700    |
# *****************************************************************************
# %% Forma 1
PRODUCTO = 3
DESCRIPCION = 2
CANTIDAD = 1
PRECIO = 0

CENTER = 18
TOTAL = 60

# Declaracion de variables y colecciones

list_Trama = ['Producto', 'Descripcion', 'Cantidad', 'Precio']

list_productos = [
    ['2000', '1', 'Iphone 12 Pro Max', 'Smartphone'],
    ['1500', '1', 'Iphone 11 Pro Max', 'Smartphone'],
    ['1200', '1', 'Iphone 10 Pro Max', 'Smartphone'],
    ['1000', '1', 'Iphone 09 Pro Max', 'Smartphone']
]

print("*".ljust(TOTAL, "*"))
print("|{}|{}|{}|{}|".format(list_Trama[0].center(15),list_Trama[1].center(20),list_Trama[2].center(10),list_Trama[3].center(10)))
print("*".ljust(TOTAL, "*"))
float_total=0
for el in list_productos:
    print("|{}|{}|{}|{}|".format(el[PRODUCTO].center(15), el[DESCRIPCION].center(
        20), el[CANTIDAD].center(10), el[PRECIO].center(10)))
    float_total += float(el[PRECIO])
list_total=["TOTAL", str(float_total)]
print("*".ljust(TOTAL, "*"))
print("|{}   |{}|".format(list_total[0].rjust(44), list_total[1].center(10)))
print("*".ljust(TOTAL, "*"))
