#tres números enteros positivos, y que calcule e imprima en pantalla el menor y el mayor de todos
print("Calcular el numero mayor y menor de 3 numeros")
print(" ")

#Entradas
a = int(input("Digite el Primer Numero  : "))
b = int(input("Digite el Segundo Numero : "))
c = int(input("Digite el Tercer Numero  : "))

#proceso y salida
if a > b and a > c:
       print("El Numero Mayor es: ", a)
elif b > a and b > c:
    print("El Numero Mayor es: ", b)
elif c > a and c > b:
    print("El Numero Mayor es: ", c)
else:
    print("no se puede comprobar")

if a < b and a < c:
     print("El Numero Menor es: ", a)
    
elif b < a and b < c:
     print("El Numero Menor es: ", b)
elif c < a and c < b:
     print("El Numero Menor es: ", c)
else:
     print("no se puede comprobar")