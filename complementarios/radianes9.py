# -*- coding: utf-8 -*-

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Complementario9: radianes a sexagesimales y centesimales")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

PI = 3.1416

print("Ingrese ángulo en radianes:")
x = float( input())
sex = x*180/PI
cen = x*200/PI

print("\nSALIDA: ")
print("--------------------------")
print("En sexagesimales es:", sex)
print("En centesimales es:", cen)