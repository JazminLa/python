print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Complementario5: calcular suma de serie 2")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

S = 0

print ("Ingresar número de términos:")
N = int( input())

for x in range(1, N+1):
    if x % 2 == 0 :
        S = S - (1/x)
    else:
        S = S + (1/x)

print("\nSALIDA: ")
print("~~~~~~~~~~~~~~~~~~")
print ("La suma será:", S)