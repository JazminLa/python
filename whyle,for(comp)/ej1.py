print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Complementario1: nums pares")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")

c = 0

print("Ingresar 10 números: ")
for i in range(1, 10 + 1):
    num = int( input("Ingresar Número: "))
    if num % 2 == 0 :
        c = c + 1

print("\nSALIDA: ")
print("~~~~~~~~~~~~~~~~~~~~~~~")
print("Hay", c, "números pares")