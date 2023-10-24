print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Complementario4: calcular suma de serie")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

print( "Ingresar el número de términos: ")
n = int( input())

s = 5
ser = 0

for a in range(1, n+1):
    s = s + 5
    ser = ser + s

print("\nSALIDA: ")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("La suma de la serie es:", ser)