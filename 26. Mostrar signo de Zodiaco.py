#26. Pidiendo el día y el mes de nacimiento mostrar el signo. 
print("Mostrar signo de Zodiaco")
print(" ")

#Entradas
print("Digitar Dia y Mes de Nacimiento")
print(" ")
dia = int(input("Digite su Dia de Nacimiento: "))
print(" ")
print(" 1 = ENERO")
print(" 2 = FEBRERO")
print(" 3 = MARZO")
print(" 4 = ABRIL")
print(" 5 = MAYO")
print(" 6 = JUNIO")
print(" 7 = JULIO")
print(" 8 = AGOSTO")
print(" 9 = SEPTIEMBRE")
print("10 = OCTUBRE")
print("11 = NOVIEMBRE")
print("12 = DICIEMBRE")
print(" ")
mes = int(input("Digite su Mes de Nacimiento: "))

#Proceso y salida
if ((dia >= 21) and (mes == 3)) or ((dia <= 20) and (mes == 4)):
    print("Su Signo es ::: ARIES")

elif ((dia >= 21) and (mes == 4)) or ((dia <= 20) and (mes == 5)):
    print("Su Signo es ::: TAURO")

elif ((dia >= 21) and (mes == 5)) or ((dia <= 20) and (mes == 6)):
    print("Su Signo es ::: GEMINIS")

elif ((dia >= 21) and (mes == 6)) or ((dia <= 22) and (mes == 7)):
    print("Su Signo es ::: CANCER")

elif ((dia >= 23) and (mes == 7)) or ((dia <= 23) and (mes == 8)):
    print("Su Signo es ::: LEO")

elif ((dia >= 24) and (mes == 8)) or ((dia <= 22) and (mes == 9)):
    print("Su Signo es ::: VIRGO")

elif ((dia >= 23) and (mes == 9)) or ((dia <= 23) and (mes == 10)):
    print("Su Signo es ::: LIBRA")

elif ((dia >= 24) and (mes == 10)) or ((dia <= 22) and (mes == 11)):
    print("Su Signo es ::: ESCORPION")

elif ((dia >= 23) and (mes == 11)) or ((dia <= 21) and (mes == 12)):
    print("Su Signo es ::: SAGITARIO")

elif ((dia >= 22) and (mes == 12)) or ((dia <= 20) and (mes == 1)):
    print("Su Signo es ::: CAPRICORNIO")

elif ((dia >= 21) and (mes == 1)) or ((dia <= 19) and (mes == 2)):
    print("Su Signo es ::: ACUARIO")

elif ((dia >= 20) and (mes == 2)) or ((dia <= 20) and (mes == 3)):
    print("Su Signo es ::: PISCIS")

else:
  print("El Signo no Existe")







