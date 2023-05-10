#23. numDia es una variable numérica que puede tomar 7 valores, ellos son 1, 2, 3, 4, 5, 6 o 7. Mostar el nombre el nombre del día de la semana que corresponde al valor de la variable numDia.  
print("mostra dia de la semana")
print(" ")

#Entradas
numDia = int(input("Digite un numero entre 1 y 7 que corresponda a un dia de la semana: "))

#proceso y salida
if numDia == 1:
    print("Su eleccion corresponde al dia: Lunes")
  
elif numDia == 2:
     print("Su eleccion corresponde al dia: Martes")

elif numDia == 3:
     print("Su eleccion corresponde al dia: Miercoles")

elif numDia == 4:
     print("Su eleccion corresponde al dia: Jueves")

elif numDia == 5:
     print("Su eleccion corresponde al dia: Viernes")

elif numDia == 6:
     print("Su eleccion corresponde al dia: Sabado")

elif numDia == 7:
     print("Su eleccion corresponde al dia: Domingo")

else:
  print("El numero digitado no corresponde a un dia de la semana")