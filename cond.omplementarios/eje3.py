# -*- coding: utf-8 -*-

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Complementario3: total del articulo")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

print("Ingresar el Costo del artículo: ")
costo = float( input())
print("Ingresar la marca: ")

m = input()

if costo >= 2000 and m == "NOSY" :
    pa = costo*0.90
    pt = pa*0.95
elif costo >= 200 and m != "NOSY" :
    pt = costo*0.90
elif costo < 2000 and m == "NOSY" :
    pa = costo*0.95
    pt = pa + pa*0.20
elif costo < 2000 and m != "NOSY" :
    pa = costo*1.20

print("\nSALIDA: ")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Usted pagara:", pt, "soles")