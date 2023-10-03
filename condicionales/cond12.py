# -*- coding: utf-8 -*-

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Ejercicio12: aumento sueldo")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

SUE = float( input("Ingresar Sueldo: "))

if SUE < 1000:
    AUM = SUE*0.15
    SUE = SUE + AUM

print("\nSALIDA: ")
print("~~~~~~~~~~~~~~~~~~~")
print("El sueldo es:", SUE)