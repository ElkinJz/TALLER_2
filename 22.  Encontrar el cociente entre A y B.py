#22. Dados dos números A y B encontrar el cociente entre A y B. Recordar que la división por cero no está definida, en ese caso debe aparecer una leyenda anunciando que la división no es posible.  
print("Encontrar cociente entre A y B")
print(" ")

#Entradas
a = int(input("Digite el valor de A: "))
b = int(input("Digite el valor de B: "))
print(" ")

#Proceso y salida
if b == 0:
   print("la división no es posible")

else:
   cociente = (a / b)
   print("El Cociente de la Division es: ", cociente)