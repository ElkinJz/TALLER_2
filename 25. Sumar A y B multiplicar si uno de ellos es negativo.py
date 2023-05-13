#Dados dos números A y B sumarlos si al menos uno de ellos es negativo en caso contrario multiplicarlos. 
print(" A y B sumarlos si uno de los # es negativo MOtiplicarlos")
print(" ")

#Entradas
a = int(input("Digite el Primer Numero : "))
b = int(input("Digite el Segundo Numero: "))
print(" ")

#proceso y salida
if a and b == 0:
    print("No cumple con las condiciones del enunciado")

elif a and b > 0:
     suma = (a + b)
     print("EL resultado de la Suma es: ",suma)

else:
    a or b < 0
    multiplicar = (a * b)
    print("El resultado de la multiplicacion es: ",multiplicar)