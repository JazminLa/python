print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Ejercicio4: determinar salida")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

print("Introducir un número: ")
N = int( input())
while N > 0 :
    RESTO = N % 10
    print(RESTO)
    N = N // 10 #División Entera, N/10, es una división decimal