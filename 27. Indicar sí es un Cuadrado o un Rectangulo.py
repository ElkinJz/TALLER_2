#27. Pidiendo el ingreso de la base y la altura de un cuadrilátero, indicar si es cuadrado o rectángulo. Para cualquiera de los dos casos mostrar el perímetro y el área de la figura. 
print("Indicar sí es un Cuadrado o un Rectangulo")
print(" ")

#Entrada
#area = L * L
#perimetro = L+L+L+L
#PERIMETRO RECTANGULO (BASE * 2) + (ALTURA * 2)
#AREA RECTANGULO BASE*ALTURA
base = float(input("Ingrese la base del triangulo  : "))
altura = float(input("Ingrese la altura del triangulo: " ))
print(" ")

#proceso y salida
if base == altura:
   print("Es un Cuadrado")
   print(" ")
   area = base * altura
   print("Su Area de de: ",area)
   perimetro = (base + altura) * 2
   print("Su Perimetro es de: ",perimetro)

else:
   print("Es un Rectangulo")
   print(" ")
   arearec = base * altura
   print("Su Area es de: ",arearec)
   perimetrorec = (base * 2) + ( altura * 2)
   print("Su Perimetro es: ",perimetrorec)