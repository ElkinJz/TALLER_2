#20. Calcular el sueldo de los empleados de una empresa. Para ello se deberá pedir el nombre del empleado, las horas normales trabajadas y las horas extras. Tener en cuenta que el valor de la hora es de $4 y que las horas extras se pagan doble
print("20. Calcular el sueldo de los empleados de una empresa")
print(" ")

#entradas
nombre = input("Digite Nombre del Empleado: ")
horas = int(input("Digite numero de horas trabajadas: "))
#hex = int(input("Digite las horas extras trabajadas: "))
valor_h = 4
valor_hex = (valor_h * 2)
sueldo = 0
horas_extras = 0
print(" ")

#proceso y salida
#sueldo = horas * valor_h
#horas_extras = hex * valor_hex


if horas == 0:
    print("El empleado no tienes horas acumuladas para cancelar")
  
elif sueldo == 0:
      sueldo = horas * valor_h
      print("Nombre de empleado", nombre)
      print("Sueldo a cancelar es de: ", sueldo)
else:
    print("El empleado no tienes horas acumuladas para cancelar")


print(" ")
hex = int(input("Digite numero de horas extras trabajadas: "))

if hex == 0:
    print("El empleado no tiene reportadas horas extras a cancelar")
elif horas_extras == 0:
     horas_extras = hex * valor_hex
     print("Horas extras a cancelar es de: ", horas_extras)
else:
   print("El empleado no tiene reportadas horas extras a cancelar")