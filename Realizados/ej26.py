# Escribir un programa que introduzca el número de un mes (1 a 12) y visualice el número de días
# de ese mes.
meses = [
    "Enero", 
    "Febrero", 
    "Marzo", 
    "Abril", 
    "Mayo", 
    "Junio", 
    "Julio",
    "Agosto",
    "Septiembre",
    "Octubre",
    "Noviembre",
    "Diciembre"
]
numMes = 0
while numMes < 1 or numMes > 12:
    try:
        numMes = int(input('\nIntroduce el numero del mes: '))
    except: 
        print("\nError - Ingrese un numero valido del 1 al 12.")
    
diasMes ={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
print(f"\nEl Mes {meses[numMes-1]} tiene {diasMes[numMes]} dias.\n")
     
