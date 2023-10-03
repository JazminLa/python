# -*- coding: utf-8 -*-

print("~~~~~~~~~~~~~~~~~~~~")
print("Ejercicio14: funcion")
print("~~~~~~~~~~~~~~~~~~~~")

print("Ingresar valores: ")
NUM = int( input("Tipo de Calculo: "))
V = int( input("Ingresar V: "))

Funcion = {
    1 : 100*V,
    2 : 100**V,
    3 : 100/V
}

VAL = Funcion.get(NUM, 0)

print("\nSALIDA: ")
print("~~~~~~~")
print(VAL)