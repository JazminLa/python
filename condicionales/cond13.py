# -*- coding: utf-8 -*-

print("~~~~~~~~~~~~~~~~~~~~~~~~")
print("EjercicioN: año bisiesto")
print("~~~~~~~~~~~~~~~~~~~~~~~~")

año = int( input("Ingresar año: "))

print("\nSALIDA: ")
print("~~~~~~~~~~~~~~~~~~~~~")
if (año % 400 == 0) or (año % 4 == 0) and (año % 100 != 0):
    print("El año es BISIESTO")
else:
    print("El año NO es BISIESTO")