# -*- coding: utf-8 -*-

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Ejercicio1: calcular el interes")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

C = -1
I = 0
M = 0

while (C<0) or (I<=0) or (I>=100) or (M <=0):
    print("Introducir el capital, el interés y el tiempo apropiados")
    C = int( input("Capital: "))
    I = int( input("Interés: "))
    M = int( input("Tiempo en Años: "))

for i in range(M):
    C = C*( 1 + I/100)

print("\nSALIDA: ")
print("~~~~~~~~~~~~~~~~~~~~")
print ("Tienes", C , "soles")