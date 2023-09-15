# 27. Cuatro enteros entre 0 y 100 representan las notas de un estudiante de un curso de informática.
# Escribir un programa para encontrar el promedio de estas notas y visualizar la calificación que le
# corresponde según la siguiente tabla:
iterar=1
acumulador=0
while iterar<=4:
    enteros = int(input('Ingrese un entero: '))
    acumulador += enteros
    iterar+=1   
acumulador=(acumulador/4)    
if acumulador>=90 and acumulador <=100:
   print(f"Su calificacion es A con un promedio de : {acumulador}") 
elif acumulador >=80 and acumulador <=89:
    print(f"Su calificacion es B con un promedio de :{acumulador} ")
elif acumulador >=70 and acumulador <=79:
    print(f"Su califiacion es C con un promedio de :{acumulador}")    
elif acumulador >=60 and acumulador <=69:
    print(f"Su calificacion es D con un promedio de : {acumulador}")
else : print(f"Su calificacion es E con un promedio de {acumulador}")    