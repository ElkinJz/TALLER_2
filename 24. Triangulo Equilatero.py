#24. Dadas las longitudes de los tres lados de un triángulo determinar si es equilátero o no. 
print("Deteminar si el triangulo es Equilatero")
print(" ")

#entradas
a = float(input("Digite la primera longitud del triangulo: "))
b = float(input("Digite la segunda longitud del triangulo: "))
c = float(input("Digite la tercera longitud del triangulo: "))
print(" ")

#proceso y salida
if a and b == c:
   print("EL triangulo es Equilatero")

else:
    print("El triangulo NO es equilatero")