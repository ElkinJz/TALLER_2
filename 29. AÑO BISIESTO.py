#29. Realizar un algoritmo que determine si un año es bisiesto o no lo es. 
print("Determinar si el año es Bisiesto o no")
print(" ")

#Entradas
año = int(input("Digigue el Año a Verificar: "))
print(" ")


#Proceso y salida

if (año % 4 == 0) and (año % 100 != 0) or (año % 400 == 0):
    print("El Año es Bisiesto")

else:
    print("El Año no es Bisiesto")

                                          