# -*- coding: utf-8 -*-

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Complementario3: cambio de soles a euros y dolares")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~}")

EU = 3.84
DO = 2.28

print("Ingresar la cantidad de soles:")
s = float( input())

d = s/DO
e = s/EU

print("\nSALIDA: ")
print("-----------------------------------")
print("En", s, "soles hay ", e, "euros")
print("En", s, "soles hay ", d, "dólares")