# Los tramos impositivos para la declaración de la renta en un determinado país son los siguientes:

# Renta	Tipo impositivo
# Menos de 10000€	5%
# Entre 10000€ y 20000€	15%
# Entre 20000€ y 35000€	20%
# Entre 35000€ y 60000€	30%
# Más de 60000€	45%
# Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla el tipo impositivo que le corresponde.



rentaAnual = int(input("Ingreses su rental anual  :"))




if rentaAnual <10000:
    cantidadImpuesto = 5
elif rentaAnual >=10000 and rentaAnual <=20000:
    cantidadImpuesto = 15
elif rentaAnual >=20000 and rentaAnual <= 35000:
    cantidadImpuesto = 20
elif rentaAnual >=35000 and rentaAnual <=60000:
        cantidadImpuesto = 30
else : cantidadImpuesto = 45    

print(f"El impuesto es : {rentaAnual * cantidadImpuesto / 100} $ " )








