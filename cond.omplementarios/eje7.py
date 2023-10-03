print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Complementario7: raices ecuacion cuadratica")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

print("Ingresar valores de la ecuación cuadrática:")
a = int( input("a: "))
b = int( input("b: "))
c = int( input("c: "))

d = b**2 - 4*a*c

print("\nSALIDA: ")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")
if d > 0 :
    x1 = ( (-b) + d**0.5 )/ 2*a
    x2 = ( (-b) - d**0.5 )/ 2*a
    print("Raíces reales:", x1, x2)
else:
    print("Raíces Irracionales")