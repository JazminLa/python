# -*- coding: utf-8 -*-
#Decoración: Nombre del Algoritmo
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Ejercicio 10: CALCULAR ÁREA Y VOLUMEN DEL CILINDRO")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

#Constantes
PI = 3.1416

#Entradas
print("Ingrese el radio y el alto: ")
radio = float( input("Radio: "))
alto = float ( input("Alto: "))

#Proceso
vol = PI * radio**2 * alto
are = 2*PI*radio*(radio + alto)

#Salida
print("\nSALIDA: ")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Volumen:", vol)
print("área:", are)