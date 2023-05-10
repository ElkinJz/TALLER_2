# Escribir un programa en Python que lea dos números del teclado y diga cuál es el mayor y cual el menor.  
print("Numero Mayor y Menor")
print(" ")

#Entradas
#a y b son variables de entrada
a = int(input("Digite El Primer Numero : "))
b = int(input("Digite El Segundo Numero: "))
print(" ")

#Proceso y Salida
#se utiliza el condicional if para determninar el numero mayor y menor utilizando el operador > (mayor que)
if a == b:
  print("Los Numeros Son Iguales")

elif a > b:
  print("EL Numero Mayor es: ", a)
  print("El NUmero Menor es: ", b)
  
else:
  print("El Numero Mayor es: ", b)
  print("El Numero Menor es: ", a)