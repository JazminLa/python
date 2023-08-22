# -*- coding: utf-8 -*-
#Librerias
import math 
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Complementario7: calcular el tercer lado de un triangulo")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

PI = 3.1416

print("Ingresar lados del triángulo:")
b = float( input("Lado b: "))
c = float( input("Lado c: "))
print("Ingresar el ángulo en grados sexagesimales:")
alfa = float( input())

a = ( b**2 + c**2 - 2*b*c * math.cos( alfa*PI/180 ) )**0.50

print("\nSALIDA: ")
print("-----------------")
print("El lado a es:", a)