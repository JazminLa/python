# -*- coding: utf-8 -*-
import math #librería necesaria para usar funciones Matemáticas
#en este caso math.ceil(), que redondea un numero al Entero superior

#nombre del algoritmo
print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print ("Ejercicio 5: CANTIDAD DE MICRO DISCOS 3.5 NECESARIOS")
print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

#Entradas
print ("ingrese GB: ")
GB=float(input())

#Proceso
MG=GB*1024
MD=MG/1.44

#Salida
print ("n/SALIDA: ")
print ("~~~~~~~~~~~~~~~~~~~~~~~~~")
print (MD)
#En caso de Decimal Aproximar al siguiente entero
#Ya que la parte decimal debe ser almacenada en otro DISCO 3.5
print ("cantidad de Discos necesarios: ", math.ceil(MD))