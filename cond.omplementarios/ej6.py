print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Complementario6: primer entero decide")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

print("Ingresar los 3 números:")
a = int( input("a: "))
b = int( input("b: "))
c = int( input("c: "))

if a < 0 :
    r = a*b*c
else:
    r = a + b + c

print("\nSALIDA: ")
print("~~~~~~~~~~~")
print(r)