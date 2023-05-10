#Escriba el código necesario para saber si un número es positivo o negativo.
print("Numeros positivos o negativos")
print(" ")

#Entradas
#Utilice la variable float por si el numero que digita el usuario tiene decimales ej: 2.3, 4.3
numero = float(input("Digite un Numero: "))
print(" ")

#Proceso y Salida
#Se realiza el proceso con el condicional if dejando como condicion si el numero es igual a cero que imprima que es neutral y sino que imprima si es positivo o negartivo
if numero == 0:
  print("El numero cero 0 Neutral")
elif numero > 0:
  print("El nummero", numero, "es Positivo")
else:
  print("El numero", numero, "es Negativo")
