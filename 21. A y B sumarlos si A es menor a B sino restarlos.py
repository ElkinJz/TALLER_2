#21. Dados dos números A y B sumarlos si A es menor a B sino restarlos.
print(
  "Suma o resta de dos numeros (Sumarlos si A es menor a B sino restarlos)")
print(" ")

#Entradas
a = int(input("Digite el Valor de A : "))
b = int(input("Digite el Valor de B : "))
print(" ")

#Proceso y salida
if a == b:
  print("No cumple con las condiciones del enunciado")

elif a < b:
  suma = (a + b)
  print("La sumatoria de los numeros es: ", suma)

else:
  resta = (a - b)
  print("La resta de los numeros es: ", resta)
