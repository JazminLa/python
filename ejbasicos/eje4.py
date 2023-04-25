#Decoracion: Nombre del Algoritmo
print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print ("ejercicio 4: puntaje total de partidos")
print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
#Entrada 
print ("ingrese cantidad de partidos ganados")
PG = int(input())
print ("ingrese cantidad de partidos empatados")
PE = int(input())
print ("ingrese cantidad de partidos perdidos")
PP = int(input())
#Proceso
PPG = PG*3
PPE = PE*1
PPP = PP*0
PF = PPG+PPE+PPP
#Salida
print ("/nSALIDA: ")
print ("~~~~~~~~~")
print ("Puntaje Final: ", PF)
