# -*- coding: utf-8 -*-
#Decoración: Nombre del Algoritmo
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Ejercicio 8: CALCULAR PERÍMETRO Y SUPERFICIE DEL RECTÁNGULO")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

#Entradas
print("Ingrese la base y el alto: ")
BASE = float( input("Base: "))
ALTO = float( input("Alto: "))

#Proceso
SUP = BASE*ALTO
PER = 2*(BASE + ALTO)

#Salida
print("\nSALIDA: ")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Superficie:", SUP)
print("Perímetro:", PER)