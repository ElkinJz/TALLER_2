#28. Un negocio hace descuentos en las ventas de sus productos. Si la compra es inferior a $100 el descuento es del 5%, si es mayor o igual a 100 y menor a 200 el descuento es del 10% sino será del 15%.Dado el precio de la venta mostrar el descuento realizado en pesos y el precio final con descuento. 
print("DESCUENTO POR VENTAS DE PRODUCTOS")
print(" ")

#Entradas
venta = float(input("Digite el Valor del Producto: "))
print(" ")


#proceso y salida
if venta < 100:
   descuento = venta * 0.05
   pfinal = venta - descuento  
   print("Su descuento fue de:$",descuento,"Mil Pesos")
   print("Precio Final con Descuento:$",pfinal,"Mil Pesos")

elif (venta >= 100) and (venta < 200):
    descuento = venta * 0.10
    pfinal = venta - descuento
    print("Su descuento fue de:$",descuento,"Mil Pesos")
    print("Precio Final con Descuento:$",pfinal,"Mil Pesos")
else:
    venta > 200
    descuento = venta * 0.15
    pfinal = venta - descuento
    print("Su descuento fue de:$",descuento,"Mil Pesos")
    print("Precio Final con Descuento:$",pfinal,"Mil Pesos")

