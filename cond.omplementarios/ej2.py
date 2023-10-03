# -*- coding: utf-8 -*-

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Complementario2: mostrar menor a mayor")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

print("Ingresar dos números: ")
a = int( input("Ingrese a: "))
b = int( input("Ingrese b: "))

print("\nSALIDA: ")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")
if a < b:
    print("Los números son:", a, b)
else:
    print("Los números son:", b, a)