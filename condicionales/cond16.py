# -*- coding: utf-8 -*-

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Ejercicio16: determinar salida")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

A = int( input("Ingresar A: "))
B = int( input("Ingresar B: "))
C = int( input("Ingresar C: "))
print("\nSALIDA: ")
print("~~~~~~~~~~~~~~~~~~~~")

if A > B :
    if A > C:
        if B > C:
            print(A, B, C)
        else:
            print(A,C,B)
    else:
        print(C,A,B)
else:
    if B > C :
        if A > C :
            print(B,A,C)
        else:
            print(B,C,A)
    else:
        print(C,B,A)