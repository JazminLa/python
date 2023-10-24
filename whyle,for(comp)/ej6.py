print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Complementario6: invertir num")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

aux = 0
aux2 = 0

print("Ingresar un número: ")
n = int( input())

i = 10
#TODO: REPORTAR COMO ERROR
while i <= n:
    aux = n%10
    n = n // 10
    aux2 = aux2*10 + aux
aux2 = aux2*10 + n

print("\nSALIDA: ")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("El número invertido será:", aux2)