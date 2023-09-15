
contador = 0
total = 0
cantidad = int(input('\nIngrese un numero: '))
while cantidad != 0:
    contador = contador +1
    total = total + cantidad
    cantidad = int(input('Ingrese un numero: '))
    
    
print (f"\nEl total de numeros ingresados es {contador} y su promedio es {total/contador}" 
    if contador > 0 
     else "\nNo ingreso ningun numero."
)   
        